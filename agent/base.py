#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Bryan Ghahremani
Python Version: 3.7.3
Copyright: GNU GPLv3

This contains the base interface for an agent

"""

class  Agent:
	""""""
	def __init__(self):
		pass

	def select_move(self,game_state):
		raise NotImplementedError()
