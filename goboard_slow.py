#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Bryan Ghahremani
Python Version: 3.7.3
Copyright: GNU GPLv3

This will contain the rules and gamestate of a go game

"""

import copy
from go-hana.gotypes import Player

class Move():
	"""
	Move describes the allowable actions for a player,
	they can play (place a stone), pass or resign.
	"""
	
	def __init__(self, point=None, is_pass=False, is_resign=False):
		assert(point is not None) ^ is_pass ^ is_resign
 		self.point = point
 		self.is_play = (self.point is not None)
 		self.is_pass = is_pass
 		self.is_resign = is_resign

 	@classmethod
 	def play(cls, point):
 		return Move(point=point)
 	
 	@classmethod
 	def pass_turn(cls):
 		return Move(is_pass=True)

 	@classmethod
 	def resign(cls):
 		return Move(is_resign=True)

class GoString():
	"""
	In Go the term string referst to a string of connected stones, so we will 
	build a GoString class to encapsulate this
	"""

	def __init__(self, color, stones, liberties):
		self.color = color
		self.stones = set(stones)
		self.liberties = set(liberties)

	def remove_liberty(self, point):
		self.liberties.remove(point)
	
	def add_liberty(self, point):
		self.liberties.add(point)

	def merged_with(self, go_string):
		assert go_string.color == self.color
		combined_stones = self.stones | go_string.stones
		return GoString(
			self.color,
			combined_stones,
			(self.liberties|go_string.liberties) - combined_stones)
	
	@property
	def num_liberties(self):
		return len(self.liberties)
	
	def __eq__(self, other):
		return isinstance(other, GoString) and \
			self.color == other.color and \
			self.stones == other.stones and \
			self.liberties == other.liberties

class Board():
	"""
	This describes the board including the number of rows and columns, how to
	place a stone, and stones currently on the board
	"""
	
	def __init__(self, num_rows, num_cols):

		self.num_cols = num_cols
		self.num_rows = num_rows
		self._grid = {}

	def place_stones(self, player, point):
		assert self.is_on_grid(point)
		assert self._grid.get(point) is None
		adjacent_same_color = []
		adjacent_opposite_color = []
		liberties = []
		#First examinethe direct neighbors of this point
		for neighbor in point.neighbors():
			if not self.is_on_grid(neighbor):
				continue
			neighbor_string = self._grid.get(neighbor)
			if neighbor_string is None:
				liberties.append(neighbor)
			elif neighbor_string.color == player:
				if neighbor_string not in adjacent_same_color:
					adjacent_same_color.append(neighbor_string)
			else:
				if neighbor_string not in adjacent_opposite_color:
					adjacent_opposite_color.append(neighbor_string)
		new_string = GoString(player, [point], liberties)
		#Now we do 3 things
		#merge with adjacent same color strings
		for same_color_string in adjacent_same_color:
			new_string = new_string.merged_with(same_color_string)
		#set the 'owner string' on grid to new string
		for new_string_point in new_string.stones:
			self._grid[new_string_point] = new_string
		#reduce liberties of any adjacent strings of opposite color 
		for other_color_string in adjacent_opposite_color:
			other_color_string.remove_liberty(point)
		#remove any opposite color strings with no liberties
		for other_color_string in adjacent_opposite_color:
			if other_color_string.num_liberties == 0:
				self._remove_string(other_color_string)


	def is_on_grid(self, point):
		return 1 <= point.row <= self.num_rows and \
			1 <= point.col <= self.num_cols
	def get(self, point)
		string = self._grid.get(point)
		if string is None:
			return None
		return string.color
	def get_go_string(self, point):
		string = self._grid.get(point)
		if string is None:
			return None
		return string
	def _remove_string(self, string):
		for point in string.stones:
			for neighbor in point.neighbors():
				neighbor_string = self._grid.get(neighbor)
				if neighbor_string is None:
					continue
				if neighbor_string is not string:
					neighbor_string.add_liberty(point)
			self._grid[point] = None

