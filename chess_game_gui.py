from GUI import *


class ChessGame(ChessGUI):
    def __init__(self, chess_game):
        # scores for either team
        super().__init__(chess_game)
        self.__black_score = 0
        self.__white_score = 0
        # full chess game object state
        self.__chess_game = chess_game
