from gamePiece import *
from GameBoardSystem import GameBoard
import tkinter as tk


class ChessGUI:
    def __init__(self, chess_game):
        # current team that will be moving, white will move first
        self.__current_team_to_move = "white"
        # full chess game object state
        self.__chess_game = chess_game
        # this is thr grid size (chess boards are 8x8)
        self.__number_of_squares_on_board = 8
        # this is the size of each tile on the chess board
        self.__individual_square_size = 70
        # this is used to load the chess pieces
        self.__chess_pieces_png = {}
        # this stores where the user clicks to find which piece will be moved
        self.__selection_of_first_click = None
        # store previous moves
        self.__stored_chess_board_state = []

        # tkinter root for chess game
        self._chess_game_root = tk.Tk()
        self._chess_game_canvas = tk.Canvas(self._chess_game_root, width=self.__number_of_squares_on_board * self.__individual_square_size + 200,
                                            height=self.__number_of_squares_on_board * self.__individual_square_size)
        self._chess_game_canvas.pack(side=tk.LEFT)

        # frame for buttons
        self._chess_right_block_frame = tk.Frame(self._chess_game_root)
        self._chess_right_block_frame.pack(side=tk.RIGHT)

        # current turn indicator
        self._current_teams_turn = tk.Label(self._chess_right_block_frame, text=f"Current turn: {self.__current_team_to_move}")
        self._current_teams_turn.pack()

        # reset chess board button
        self._new_game_button = tk.Button(self._chess_right_block_frame, text="New Game", command=self.start_new_game)
        self._new_game_button.pack()

        # TODO undo move button
        # self.undo_move_button = tk.Button(self.right_frame, text="Undo Move", command=self.undo_move)
        # self.undo_move_button.pack()

        # initialize the game board
        self.initialize_board()

        # Add the chess pieces to the board and update the canvas
        self.update_board()

        # Add event listener to the canvas that listens for clicks
        self._chess_game_canvas.bind("<Button-1>", self.piece_to_move_selection)

        # Start the tkinter event loop
        self._chess_game_root.mainloop()

    def initialize_board(self):
        # Load image files for each chess piece and store them in the piece_images dictionary
        for color in ["white", "black"]:
            for piece_type in ["king", "queen", "rook", "bishop", "knight", "pawn"]:
                file_name = f"chess_pieces/{color}_{piece_type}.png"
                self.__chess_pieces_png[(color, piece_type)] = tk.PhotoImage(file=file_name)

        # Loop through the rows and columns of the grid, creating squares with the appropriate color
        for row in range(self.__number_of_squares_on_board):
            for col in range(self.__number_of_squares_on_board):
                if (row + col) % 2 == 0:
                    color = "#c2a07e"
                else:
                    color = "#a36b36"
                self._chess_game_canvas.create_rectangle(col * self.__individual_square_size, row * self.__individual_square_size,
                                                         (col + 1) * self.__individual_square_size,
                                                         (row + 1) * self.__individual_square_size, fill=color)

    def update_board(self):

        # Loop through the rows and columns of the grid, adding chess pieces to the appropriate squares
        for row in range(self.__number_of_squares_on_board):
            for col in range(self.__number_of_squares_on_board):
                piece = self.__chess_game.get_piece(row, col)
                if type(piece) is not EmptySpace:
                    color = piece.get_team()
                    piece_type = piece.piece_type
                    image = self.__chess_pieces_png[(color, piece_type)]
                    if (row, col) in self.__chess_pieces_png:
                        # Delete the previous image for this piece
                        self._chess_game_canvas.delete(self.__chess_pieces_png[row, col])
                    # Add the new piece image at the correct location
                    self.__chess_pieces_png[(row, col)] = self._chess_game_canvas.create_image((col + 0.5) *
                                                                                        self.__individual_square_size,
                                                                                        (row + 0.5) * self.__individual_square_size,
                                                                                        image=image)
                else:
                    if (row, col) in self.__chess_pieces_png:
                        # Delete the image for the empty space
                        self._chess_game_canvas.delete(self.__chess_pieces_png[(row, col)])
                        del self.__chess_pieces_png[(row, col)]

    def piece_to_move_selection(self, event):
        col = event.x // self.__individual_square_size
        row = event.y // self.__individual_square_size
        self.update_board()

        # Check if the selected piece is valid
        piece = self.__chess_game.get_piece(row, col)
        if type(piece) is EmptySpace or piece.get_team() != self.__current_team_to_move:
            return

        # Remove the old piece's image from the canvas
        for item in self._chess_game_canvas.find_enclosed(col * self.__individual_square_size,
                                              row * self.__individual_square_size,
                                              (col + 1) * self.__individual_square_size,
                                              (row + 1) * self.__individual_square_size):
            self._chess_game_canvas.delete(item)

        # Update the first selection and bind the canvas to the second click event
        self.__selection_of_first_click = piece
        self._chess_game_canvas.bind("<Button-1>", self.handle_second_selection)

    # def move_piece(self, row, col):
    #     # Get the piece that was clicked
    #     # loop until they select a valid piece on their team
    #     self.update_board()
    #     # piece selected
    #     first_piece_selected_by_player = self.__chess_game.get_piece(row, col)
    #     self.__selection_of_first_click = first_piece_selected_by_player
    #     if first_piece_selected_by_player.get_team() != self.__current_team_to_move:
    #         print("invalid Character to move")
    #         self._chess_game_canvas.bind("<Button-1>", self.piece_to_move_selection)
    #
    #     # get the second location, if invalid repeat entire step
    #     self._chess_game_canvas.bind("<Button-1>", self.handle_second_selection)

    def handle_second_selection(self, event):
        col = event.x // self.__individual_square_size
        row = event.y // self.__individual_square_size
        valid_move = False
        self.update_board()

        # Determine if the move is valid
        if type(self.__selection_of_first_click) == Pawn:
            valid_move = self.__chess_game.move_pawn(self.__selection_of_first_click, row, col)
        elif type(self.__selection_of_first_click) == Rooke:
            valid_move = self.__chess_game.move_rook(self.__selection_of_first_click, row, col)
        elif type(self.__selection_of_first_click) == Bishop:
            valid_move = self.__chess_game.move_bishop(self.__selection_of_first_click, row, col)
        elif type(self.__selection_of_first_click) == King:
            valid_move = self.__chess_game.move_king(self.__selection_of_first_click, row, col)
        elif type(self.__selection_of_first_click) == Queen:
            valid_move = self.__chess_game.move_queen(self.__selection_of_first_click, row, col)
        elif type(self.__selection_of_first_click) == Knight:
            valid_move = self.__chess_game.move_knight(self.__selection_of_first_click, row, col)

        if valid_move:
            # Switch the current team to move
            if self.__current_team_to_move == "white":
                self.__current_team_to_move = "black"
            else:
                self.__current_team_to_move = "white"

            # Update the board and bind the canvas to the first click event again
            self.update_board()
            self._chess_game_canvas.bind("<Button-1>", self.piece_to_move_selection)

            # Update the turn label
            self._current_teams_turn.configure(text=f"Current turn: {self.__current_team_to_move}")

            # add the game_state to the previous_game_states
            self.__stored_chess_board_state.append(self.__chess_game)

        else:
            # The move was invalid, so bind the canvas to the second click event again
            self._chess_game_canvas.bind("<Button-1>", self.piece_to_move_selection)

    def start_new_game(self):
        self.__chess_game = GameBoard()
        self.__current_team_to_move = "white"
        self.update_board()

    # def undo_move(self):
    #     # Check if there are any previous board states to undo
    #     if len(self.__stored_chess_board_state) == 0:
    #         return
    #
    #     # Restore the previous board state and switch the current team to move
    #     previous_state = self.__stored_chess_board_state.pop()
    #     self.board.set_board(previous_state)
    #     self.__current_team_to_move = "white" if self.__current_team_to_move == "black" else "white"
    #
    #     # Update the GUI to reflect the restored board state
    #     self.update_board()
    #     self.turn_label.configure(text=f"Current turn: {self.__current_team_to_move}")




board = GameBoard()
gui = ChessGUI(board)
