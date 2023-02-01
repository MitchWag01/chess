# creating the gameboard itself, chess board is 8x8 pieces
from gamePiece import *


class GameBoard(object):
    """
    """
    def __init__(self):
        # self.white_team = Team()
        # self.black_team = Team()
        self.board = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]

    # def get_white_team(self):
    #     return self.white_team
    #
    # def get_black_team(self):
    #     return self.black_team
    #
    # def black_lose(self):
    #     return self.black_team.get_king() == 0
    #
    # def white_lose(self):
    #     return self.white_team.get_king() == 0

    def start_new_game(self):
        # setting all white pieces to their original position excluding pawns
        self.board[0][0] = Rooke("white", 0, 0)
        self.board[0][1] = Knight("white", 1, 0)
        self.board[0][2] = Bishop("white", 2, 0)
        self.board[0][3] = Queen("white", 3, 0)
        self.board[0][4] = King("white", 4, 0)
        self.board[0][5] = Rooke("white", 5, 0)
        self.board[0][6] = Knight("white", 6, 0)
        self.board[0][7] = Bishop("white", 7, 0)

        # setting all white and black pawns on the board to starting position
        for i in range(8):
            self.board[1][i] = Pawn("white", i, 1)
            self.board[6][i] = Pawn("black", i, 6)

        # setting all empty board pieces to None to indicate empty
        for i in range(8):
            self.board[2][i] = None
            self.board[3][i] = None
            self.board[4][i] = None
            self.board[5][i] = None

        # setting all black pieces to their original position excluding pawns
        self.board[7][0] = Rooke("black", 0, 7)
        self.board[7][1] = Knight("black", 1, 7)
        self.board[7][2] = Bishop("black", 2, 7)
        self.board[7][3] = Queen("black", 3, 7)
        self.board[7][4] = King("black", 4, 7)
        self.board[7][5] = Rooke("black", 5, 7)
        self.board[7][6] = Knight("black", 6, 7)
        self.board[7][7] = Bishop("black", 7, 7)

    def get_piece(self, x, y):
        """
        Purpoes - Gets the piece object that is stored at the specidic x, y co-ordinate

        :parameter
            x - x index on board
            y - y index on board


        TODO -- when board is complete will likely need to change from index value to the board location
        """
        return self.board[y][x]

    def move_pawn(self, pawn, new_x, new_y):
        x = pawn.get_x()
        y = pawn.get_y()
        # make sure that white pawns only move forward and black pawns only move backwards
        if pawn.get_team() == "white":
            if new_y <= y or new_y > y + 2:
                return False

            # for the white team checking move foraward 2-pieces
            if y == 1 and new_x == x:
                print("Moving forward 2")

                # check for pieces blocking path
                if new_y == y + 2:
                    if (self.get_piece(x, y+1) is not None) or self.get_piece(x, y+2) is not None:
                        print("there is a piece in the way you cannot move")
                        return False

            # checking a single move forward from start
            if new_y == y + 1 and new_y == 2:
                if self.board[y + 1][x] is not None:
                    print("there is a piece in the way you cannot move")
                    return False

            # moving a pawn that is not on the start position
            if y != 1 and new_x == x:
                print("moving forward 1")

                # checking single move forward when not in the start position
                if self.board[y + 1][x] is not None:
                    print("there is a piece in the way you cannot move")
                    return False
                elif new_y != y + 1:
                    print("you can only move 1 spot forward if you are not on starting position")
                    return False

            # checking for proper pawn piece taking
            if (new_x == x + 1 or new_x == x - 1) and new_y == y + 1:
                print("taking piece")
                if self.board[new_y][new_x] is None:
                    print("cannot take empty piece")
                    return False

        # checking for black chess piece
        if pawn.get_team() == "black":
            if new_y >= y or new_y < y - 2:
                return False

            # if the pawn is on its starting piece it is allowed to move 2 forward
            if y == 6 and new_x == x:
                print("moving forward 2")

                # check to make sure that there are no pieces in front on 2 spaced move
                if new_y == y - 2:
                    if self.board[y - 1][x] is not None or self.board[y - 2][x] is not None:
                        print("there is a piece in the way you cannot move")
                        return False

            # checking single move forward from start
            if new_y == y - 1 and y == 6:
                if self.board[y - 1][x] is not None:
                    print("there is a piece in the way you cannot move")
                    return False

            # moving a pawn that is not on the start position
            if y != 6 and new_x == x:
                print("moving forward 1")

                # chcking single move forward
                if self.board[y - 1][x] is not None:
                    print("there is a piece in the way you cannot move")
                    return False
                elif new_y != y + 1 or new_y != y - 1:
                    print("you can only move 1 spot forward if you are not on starting position")
                    return False

            # checking for proper pawn piece taking
            if (new_x == x + 1 or new_x == x - 1) and new_y == y - 1:
                print("taking piece")

                # if the piece we are trying to take is None we cannot take
                if self.board[new_y][new_x] is None:
                    print("cannot take empty piece")
                    return False

        pawn.set_x(new_x)
        pawn.set_y(new_y)
        self.board[new_y][new_x] = self.board[y][x]
        self.board[y][x] = None

    def get_board(self):
        return self.board
