#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Bryan Ghahremani
Python Version: 3.7.3
Copyright: GNU GPLv3

This is the naive, absolute beginner go bot, it will randomly select moves
that do not fill its own eyes, thats it.

Just for clarity's sake, this bot will not learn. It will play randomly no 
matter what you do (or an opponenet bot does). At this point its mainly a 
way to test our setup
"""

import random
from go-hana.agent.base import Agent
from go-hana.agent.helpers import is_point_an_eye
from go-hana.goboard_slow import Move
from go-hana.gotypes import Point

class RandomBot(Agent):
	"""
	This go bot extends the agent interface
	"""
	def select_move(self, game_state):
		"""
		select a random move that doesn't fill eyes
		"""
		candidates = []
		for r in range(1, game_state.board.num_rows + 1):
			for c in range(1, game_state.board.num_cols + 1):
				candidate = Point(row=r, col=c)
				if game_state.is_valid_move(Move.play(candidate)) and \
						not is_point_an_eye(game_state.board,
											candidate,
											game_state.next_player):
					candidates.append(candidate)
		if not candidates:
			return Move.pass_turn()
		return Move.play(random.choice(candidates))