"""
	File name: tictactoe_ui.py
	Author: Joseph Kim
	Date created: 7/12/18
	Date last modified: 7/12/18
	Python Version: 3.6.6
"""

class TicTacToeAI():
"""This class is the 'brain' of the computer AI."""


	def getMoves(self, state):
		"""Gets the available moves.
		Returns:
			A list of the indexes coorresponding to the open spaces to move.
		"""
		open_moves = []
		for i, move in enumerate(list(state)):
			if move == 0:
				open_moves.append(i)
		return open_moves

	def minimax(self, state, depth, Maximizer):
		
