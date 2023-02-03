# import pygame
from gameBoard import GameBoard
from gamePiece import *

# initailize the gameBoard
# pygame.init()
game = GameBoard()


bottom_label = "  0 1 2 3 4 5 6 7"

game.start_new_game()
game.move_pawn(game.get_piece(0, 1), 0, 3)
game.move_pawn(game.get_piece(1, 1), 0, 1)
game.move_rooke(game.get_piece(0, 0), 0, 2)
game.move_pawn(game.get_piece(0, 6), 0, 4)
game.move_rooke(game.get_piece(0, 7), 0, 5)
game.move_rooke(game.get_piece(0, 5), 4, 5)

game.move_rooke(game.get_piece(0, 2), 3, 2)





count = 0
for y in game.get_board():
    print(f"{count} ", end="")
    for x in y:
        if type(x) == Pawn:
            print("P", end="")
        elif type(x) == Rooke:
            print("R", end="")
        elif type(x) == Knight:
            print("K", end="")
        elif type(x) == Bishop:
            print("B", end="")
        elif type(x) == Queen:
            print("Q", end="")
        elif type(x) == King:
            print("X", end="")
        else:
            print(".", end="")
        print(" ", end="")
    print("")
    count += 1
print(bottom_label)
