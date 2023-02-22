# creating the gameboard itself, chess board is 8x8 pieces
from gamePiece import *


class GameBoard(object):
    """
    """
    def __init__(self):

        self.board = [[Piece, Piece, Piece, Piece, Piece, Piece, Piece, Piece], [Piece, Piece, Piece, Piece, Piece, Piece, Piece, Piece], [Piece, Piece, Piece, Piece, Piece, Piece, Piece, Piece],
                      [Piece, Piece, Piece, Piece, Piece, Piece, Piece, Piece], [Piece, Piece, Piece, Piece, Piece, Piece, Piece, Piece], [Piece, Piece, Piece, Piece, Piece, Piece, Piece, Piece],
                      [Piece, Piece, Piece, Piece, Piece, Piece, Piece, Piece], [Piece, Piece, Piece, Piece, Piece, Piece, Piece, Piece]]

    def start_new_game(self):
        """
        Purpose:
            Resets the game board positions to their original condition
        Return:
            None
        """
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
            self.board[2][i] = Piece
            self.board[3][i] = Piece
            self.board[4][i] = Piece
            self.board[5][i] = Piece

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
        """
        return self.board[y][x]

    def is_empty(self, x, y):
        """
        Purpose:
            Determines if location has any pieces or not
        Pre-Conditions:
            x - int - x location of board to check if there are any pieces
            y - int - y location on board to check if there are any pieces
        Post-Conditions:
            None
        Return:
            Boolean - True if there is a piece false otherwise
        """
        return self.board[y][x] is not Piece

    def get_board(self):
        """
        Purpose:
            Gets Gameboard object
        Return
            GameBoard Type - current state of the board
        """
        return self.board

    def move_pawn(self, pawn, new_x, new_y):
        """
        Purpose:
            Moves a pawn type to a new location on the board
        """
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
                    if (self.get_piece(x, y+1) is not Piece) or self.get_piece(x, y+2) is not Piece:
                        print("there is a piece in the way you cannot move")
                        return False

            # checking a single move forward from start
            if new_y == y + 1 and new_y == 2:
                if self.board[y + 1][x] is not Piece:
                    print("there is a piece in the way you cannot move")
                    return False

            # moving a pawn that is not on the start position
            if y != 1 and new_x == x:
                print("moving forward 1")

                # checking single move forward when not in the start position
                if self.board[y + 1][x] is not Piece:
                    print("there is a piece in the way you cannot move")
                    return False
                elif new_y != y + 1:
                    print("you can only move 1 spot forward if you are not on starting position")
                    return False

            # checking for proper pawn piece taking
            if (new_x == x + 1 or new_x == x - 1) and new_y == y + 1:
                print("taking piece")
                if self.board[new_y][new_x] is Piece:
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
                    if self.board[y - 1][x] is not Piece or self.board[y - 2][x] is not Piece:
                        print("there is a piece in the way you cannot move")
                        return False

            # checking single move forward from start
            if new_y == y - 1 and y == 6:
                if self.board[y - 1][x] is not Piece:
                    print("there is a piece in the way you cannot move")
                    return False

            # moving a pawn that is not on the start position
            if y != 6 and new_x == x:
                print("moving forward 1")

                # chcking single move forward
                if self.board[y - 1][x] is not Piece:
                    print("there is a piece in the way you cannot move")
                    return False
                elif new_y != y + 1 or new_y != y - 1:
                    print("you can only move 1 spot forward if you are not on starting position")
                    return False

            # checking for proper pawn piece taking
            if (new_x == x + 1 or new_x == x - 1) and new_y == y - 1:
                print("taking piece")

                # if the piece we are trying to take is None we cannot take
                if self.board[new_y][new_x] is Piece:
                    print("cannot take empty piece")
                    return False
                if self.board[new_y][new_x].get_team() == pawn.get_team():
                    print("Cannot take pawn on the same team")
                    return False

        pawn.set_x(new_x)
        pawn.set_y(new_y)
        self.board[new_y][new_x] = self.board[y][x]
        self.board[y][x] = Piece

    def move_rooke(self, rooke, new_x, new_y):
        """
        Purpose:
            To move the rooke to the desired new location
        PreConditions:
            new_x - int - new x location on the board
            new_y - int - new y position on the board
        PostConditions:
            chess board object changed so rooke is in new position
        return:
            True if succesful move, False otherwise
        """
        x = rooke.get_x()
        y = rooke.get_y()

        # if piece is moved off x or y invalid location
        if x == new_x and y == new_y:
            print("Invalid Location Must move piece")
            return False
        if y != new_y and x != new_x:
            print("Cannot move both x and y positions")

        if new_x != x and new_y == y:
            # checking if there is a piece in the way of the rooke preventing move --> x direction
            for j in range(1, abs(new_x - x) - 1):

                # checking positive x direction moves
                if new_x > x:

                    # if there is a piece in the way return False
                    if self.board[y][x + j] is not Piece:
                        print("Error Cannot move with piece in the way 1")
                        return False

                # checking negative x direction
                if new_x < x:

                    # if there is a piece in the way return false
                    if self.board[y][x - j] is not Piece:
                        print("Error Cannot move with piece in the way 2")
                        return False

        elif new_y != y and new_x == x:

            # checking if there is a piece in the way of the rooke preventing move --> y direction
            for j in range(1, abs(new_y - y) - 1):

                # checking positive y direction moves
                if new_y > y:

                    # if there is a piece in the way return False
                    if self.board[y + j][x] is not Piece:
                        print("Error Cannot move with piece in the way 3")
                        return False

                # checking negative y direction
                if new_y < y:

                    # if there is a piece in the way return false
                    if self.board[y][x - j] is not Piece:
                        print("Error Cannot move with piece in the way 4")
                        return False
        else:
            print("Unexpected Position Error")
            return False

        # print(self.board[new_y][new_x].get_team())
        # print(rooke.get_team())
        # TODO checking to see if location has piece / is empty
        # if self.board[new_y][new_x].get_team() == rooke.get_team():
        #     print("Cannot take piece on your own team")
        #     return False

        # move piece
        rooke.set_x(new_x)
        rooke.set_y(new_y)
        self.board[new_y][new_x] = self.board[y][x]
        self.board[y][x] = Piece


