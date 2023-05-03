# creating the game-board itself, chess board is 8x8 pieces
from gamePiece import *


def square(v1, v2):
    return v1 * v2


# noinspection PyTypeChecker
class GameBoard:
    """
    """

    def __init__(self):
        super().__init__()

        self.__board = [[Rooke("white", 0, 0), Knight("white", 1, 0), Bishop("white", 2, 0), Queen("white", 3, 0),
                         King("white", 4, 0), Bishop("white", 5, 0), Knight("white", 6, 0), Rooke("white", 7, 0)],
                        [Pawn("white", 0, 1), Pawn("white", 1, 1), Pawn("white", 2, 1), Pawn("white", 3, 1),
                       Pawn("white", 4, 1), Pawn("white", 5, 1), Pawn("white", 6, 1), Pawn("white", 7, 1)],
                        [EmptySpace(), EmptySpace(), EmptySpace(), EmptySpace(), EmptySpace(), EmptySpace(), EmptySpace(),
                       EmptySpace()],
                        [EmptySpace(), EmptySpace(), EmptySpace(), EmptySpace(), EmptySpace(), EmptySpace(), EmptySpace(),
                       EmptySpace()],
                        [EmptySpace(), EmptySpace(), EmptySpace(), EmptySpace(), EmptySpace(), EmptySpace(), EmptySpace(),
                       EmptySpace()],
                        [EmptySpace(), EmptySpace(), EmptySpace(), EmptySpace(), EmptySpace(), EmptySpace(), EmptySpace(),
                       EmptySpace()],
                        [Pawn("black", 0, 6), Pawn("black", 1, 6), Pawn("black", 2, 6), Pawn("black", 3, 6),
                       Pawn("black", 4, 6), Pawn("black", 5, 6), Pawn("black", 6, 6), Pawn("black", 7, 6)],
                        [Rooke("black", 0, 7), Knight("black", 1, 7), Bishop("black", 2, 7), Queen("black", 3, 7),
                       King("black", 4, 7), Bishop("black", 5, 7), Knight("black", 6, 7), Rooke("black", 7, 7)]]

    def get_piece(self, x, y):
        """
        Purpose - Gets the piece object that is stored at the specific x, y co-ordinate

        parameter
            x - x index on board
            y - y index on board
        """
        return self.__board[y][x]

    def get_board(self):
        """
        Purpose:
            Gets Game board object
        Return
            GameBoard Type - current state of the board
        """
        return self.__board

    def set_board(self, new_board):
        self.__board = new_board

    def move_pawn(self, pawn, new_x, new_y):
        x = pawn.get_x()
        y = pawn.get_y()
        if new_y == y and new_x == x or self.get_piece(new_x, new_y).get_team() == pawn.team:
            return False
        pawn.set_x(new_x)
        pawn.set_y(new_y)
        self.__board[new_y][new_x] = self.__board[y][x]
        self.__board[y][x] = EmptySpace()
        return True

    def move_rook(self, rook, new_x, new_y):
        x = rook.get_x()
        y = rook.get_y()
        if new_y == y and new_x == x or self.get_piece(new_x, new_y).get_team() == rook.team:
            return False
        rook.set_x(new_x)
        rook.set_y(new_y)
        self.__board[new_y][new_x] = self.__board[y][x]
        self.__board[y][x] = EmptySpace()
        return True

    def move_knight(self, knight, new_x, new_y):
        x = knight.get_x()
        y = knight.get_y()
        if new_y == y and new_x == x or self.get_piece(new_x, new_y).get_team() == knight.team:
            return False
        knight.set_x(new_x)
        knight.set_y(new_y)
        self.__board[new_y][new_x] = self.__board[y][x]
        self.__board[y][x] = EmptySpace()
        return True

    def move_bishop(self, bishop, new_x, new_y):
        x = bishop.get_x()
        y = bishop.get_y()
        if new_y == y and new_x == x or self.get_piece(new_x, new_y).get_team() == bishop.team:
            return False
        bishop.set_x(new_x)
        bishop.set_y(new_y)
        self.__board[new_y][new_x] = self.__board[y][x]
        self.__board[y][x] = EmptySpace()
        return True

    def move_queen(self, queen, new_x, new_y):
        x = queen.get_x()
        y = queen.get_y()
        if new_y == y and new_x == x or self.get_piece(new_x, new_y).get_team() == queen.team:
            return False
        queen.set_x(new_x)
        queen.set_y(new_y)
        self.__board[new_y][new_x] = self.__board[y][x]
        self.__board[y][x] = EmptySpace()
        return True

    def move_king(self, king, new_x, new_y):
        x = king.get_x()
        y = king.get_y()
        if new_y == y and new_x == x or self.get_piece(new_x, new_y).get_team() == king.team:
            return False
        king.set_x(new_x)
        king.set_y(new_y)
        self.__board[new_y][new_x] = self.__board[y][x]
        self.__board[y][x] = EmptySpace()
        return True

    # def move_rook(self, rook, new_x, new_y):
    #     """
    #     Purpose:
    #         To move the rook to the desired new location
    #     PreConditions:
    #         new_x - int - new x location on the board
    #         new_y - int - new y position on the board
    #     PostConditions:
    #         chess board object changed so rook is in new position
    #     return:
    #         True if successful move, False otherwise
    #     """
    #     x = rook.get_x()
    #     y = rook.get_y()
    #
    #     # if piece is moved off x or y invalid location
    #     if x == new_x and y == new_y:
    #         print("Invalid Location Must move piece")
    #         return False
    #     if y != new_y and x != new_x:
    #         print("Cannot move both x and y positions")
    #
    #     if new_x != x and new_y == y:
    #         # checking if there is a piece in the way of the rook preventing move --> x direction
    #         for j in range(1, abs(new_x - x) - 1):
    #
    #             # checking positive x direction moves
    #             if new_x > x:
    #
    #                 # if there is a piece in the way return False
    #                 if type(self.board[y][x + j]) is not EmptySpace:
    #                     print(self.board[y][x + j])
    #                     print("Error Cannot move with piece in the way 1")
    #                     return False
    #
    #             # checking negative x direction
    #             if new_x < x:
    #
    #                 # if there is a piece in the way return false
    #                 if type(self.board[y][x - j]) is not EmptySpace:
    #                     print("Error Cannot move with piece in the way 2")
    #                     return False
    #
    #     elif new_y != y and new_x == x:
    #
    #         # checking if there is a piece in the way of the rook preventing move --> y direction
    #         for j in range(1, abs(new_y - y) - 1):
    #
    #             # checking positive y direction moves
    #             if new_y > y:
    #
    #                 # if there is a piece in the way return False
    #                 if self.board[y + j][x] is not EmptySpace:
    #                     print("Error Cannot move with piece in the way 3")
    #                     return False
    #
    #             # checking negative y direction
    #             if new_y < y:
    #
    #                 # if there is a piece in the way return false
    #                 if type(self.board[y][x - j]) is not EmptySpace:
    #                     print("Error Cannot move with piece in the way 4")
    #                     return False
    #     else:
    #         print("Unexpected Position Error")
    #         return False
    #
    #     # checking move on final spot to see if it's the same colour piece.
    #     if self.get_piece(new_x, new_y).get_team() == self.get_piece(x, y).get_team():
    #         print("Failed attempted to take piece on the same team.")
    #         return False
    #
    #     # move piece
    #     rook.set_x(new_x)
    #     rook.set_y(new_y)
    #     self.board[new_y][new_x] = self.board[y][x]
    #     self.board[y][x] = EmptySpace()
    #     return True
    #
    # def move_bishop(self, bishop, new_x, new_y):
    #     x = bishop.get_x()
    #     y = bishop.get_y()
    #
    #     # check to see if it's a possible move
    #
    #     # check to see if they are taking a piece on their own team
    #
    #     # check to see if there is a piece in the way
    #
    #     # move piece
    #
    #     # move piece
    #     bishop.set_x(new_x)
    #     bishop.set_y(new_y)
    #     self.board[new_y][new_x] = self.board[y][x]
    #     self.board[y][x] = EmptySpace()
    #     return True

    # def move_pawn(self, pawn, new_x, new_y):
    #     """
    #     Purpose:
    #         Moves a pawn type to a new location on the board
    #     """
    #     x = pawn.get_x()
    #     y = pawn.get_y()
    #
    #     # make sure that white pawns only move forward and black pawns only move backwards
    #     if pawn.get_team() == "white":
    #         if new_y <= y or new_y > y + 2:
    #             return False
    #
    #         # for the white team checking move forward 2-pieces
    #         if y == 1 and new_x == x:
    #
    #             # check for pieces blocking path
    #             if new_y == y + 2:
    #                 if (type(self.get_piece(x, y + 1)) is not EmptySpace) and self.get_piece(x,
    #                                                                                          y + 2).get_team() == \
    #                         "white":
    #                     print("there is a piece in the way you cannot move 1")
    #                     return False
    #
    #         # checking a single move forward from start
    #         if new_y == y + 1 and new_y == 2:
    #             if self.board[y + 1][x] is not EmptySpace:
    #                 print("there is a piece in the way you cannot move")
    #                 return False
    #
    #         # moving a pawn that is not on the start position
    #         if y != 1 and new_x == x:
    #             print("moving forward 1")
    #
    #             # checking single move forward when not in the start position
    #             if self.board[y + 1][x] is not EmptySpace:
    #                 print("there is a piece in the way you cannot move")
    #                 return False
    #             elif new_y != y + 1:
    #                 print("you can only move 1 spot forward if you are not on starting position")
    #                 return False
    #
    #         # checking for proper pawn piece taking
    #         if (new_x == x + 1 or new_x == x - 1) and new_y == y + 1:
    #             print("taking piece")
    #             if self.board[new_y][new_x] is EmptySpace:
    #                 print("cannot take empty piece")
    #                 return False
    #
    #     # checking for black chess piece
    #     if pawn.get_team() == "black":
    #         if new_y >= y or new_y < y - 2:
    #             return False
    #
    #         # if the pawn is on its starting piece it is allowed to move 2 forward
    #         if y == 6 and new_x == x:
    #             print("moving forward 2")
    #
    #             # check to make sure that there are no pieces in front of 2 spaced move
    #             if new_y == y - 2:
    #                 if self.board[y - 1][x] is not EmptySpace and self.board[y - 2][x].get_team() == "black":
    #                     print("there is a piece in the way you cannot move")
    #                     return False
    #
    #         # checking single move forward from start
    #         if new_y == y - 1 and y == 6:
    #             if self.board[y - 1][x] is not EmptySpace:
    #                 print("there is a piece in the way you cannot move")
    #                 return False
    #
    #         # moving a pawn that is not on the start position
    #         if y != 6 and new_x == x:
    #             print("moving forward 1")
    #
    #             # checking single move forward
    #             if self.board[y - 1][x] is not EmptySpace:
    #                 print("there is a piece in the way you cannot move")
    #                 return False
    #             elif new_y != y + 1 or new_y != y - 1:
    #                 print("you can only move 1 spot forward if you are not on starting position")
    #                 return False
    #
    #         # checking for proper pawn piece taking
    #         if (new_x == x + 1 or new_x == x - 1) and new_y == y - 1:
    #             print("taking piece")
    #
    #             # if the piece we are trying to take is None we cannot take
    #             if self.board[new_y][new_x] is EmptySpace:
    #                 print("cannot take empty piece")
    #                 return False
    #             if self.board[new_y][new_x].get_team() == pawn.get_team():
    #                 print("Cannot take pawn on the same team")
    #                 return False
    #         pawn.set_x(new_x)
    #         pawn.set_y(new_y)
    #         self.board[new_y][new_x] = self.board[y][x]
    #         self.board[y][x] = EmptySpace()
    #         return True
