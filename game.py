# import pygame
from gameBoard import GameBoard
from gamePiece import *

# initailize the gameBoard
# pygame.init()
game = GameBoard()
#
# # chess game is 8 by 8
# dimensions = 8
#
# # individual square size
# square_size = 50
#
# screen = pygame.display.set_mode((dimensions * square_size, dimensions * square_size))
#
# pygame.display.set_caption("Mitchells ChessBoard")
#
# # Set the colors for the chessboard squares
# white = (255, 255, 255)
# black = (0, 0, 0)
#
# # store chess pieces on the board
# game_board_pieces = game.get_board()
#
# # get all current pieces on the board
# for pieces in game_board_pieces:
#     screen.blit(pieces.get_picture, ())
#
# # Draw the chessboard
# for row in range(dimensions):
#     for col in range(dimensions):
#         color = white if (row + col) % 2 == 0 else black
#         pygame.draw.rect(screen, color, (col * square_size, row * square_size, square_size, square_size))
#
# # Update the display
# pygame.display.flip()
#
# # Run the game loop
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
# # Quit Pygame
# pygame.quit()



bottom_label = "  0 1 2 3 4 5 6 7"

game.start_new_game()
game.move_pawn(game.get_piece(0, 1), 0, 3)
game.move_pawn(game.get_piece(1, 1), 0, 1)






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
