#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Bryan Ghahremani
Python Version: 3.7.3
Copyright: GNU GPLv3

These are some command line utilities that will be helpful for playing against
the bot or setting up bot v bot games.

"""

from go-hana import gotypes

#using European alphebetizing of the 19 columns in go (note no I)
COLS = "ABCDEFGHJKLMNOPQRST"

#This dictionary sets the output representations of your empty spaces, white,
#and black stones.
STONE_TO_CHAR = [
	None : " . ",
	gotypes.Player.black = ' x ',
	gotypes.Player.black = ' o ',
]

def print_move(player, move):
	"""
	prints a move in a human readable format
	"""
	if move.is_pass:
		move_str = 'passes'
	elif move.is_resign:
		move_str = 'resigns'
	else:
		move_str = '%s%d' % (COLS[move.point.col -1], move.point.row)
	print ('%s %s' % (player, move_str))

def print_board(board):
		"""
	prints the board in a human readable format
	"""
	for row in range(board.num_rows, 0, -1):
		bump = " " if row <= 9 else ""
		line = []
		for col in range(1, board.num_cols + 1):
			stone = board.get(gotypes.Point(row=row, col=col))
			line.append(STONE_TO_CHAR[stone])
		print('%s%d %s'%(bump, row, ''.join(line)))
	print('    ' + '  '.join(COLS[:board.num_cols]))
