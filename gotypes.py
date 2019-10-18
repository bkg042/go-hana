#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Bryan Ghahremani
Python Version: 3.7.3
Copyright: GNU GPLv3

This will contain the classes and data types necessary for our go bot to play.

"""

import enum
from collections import namedtuple

class Player(enum.Enum):
	"""
	This  class represents a Player
	"""
	black = 1
	white = 2

	@property
	def other(self):
		return Player.black if self == Player.white else Player.white
	

class Point(namedtuple('Point', 'row col')):
	"""
	This class represents points on a go board
	"""

	def neighbors(self):
		return[
			Point(self.row-1, self.col),
			Point(self.row+1, self.col),
			Point(self.row, self.col-1),
			Point(self.row, self.col+1),
		]