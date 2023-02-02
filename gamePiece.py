class Piece(object):
    def __init__(self, team_n, original_x, original_y):
        self.team = team_n
        self.x = original_x
        self.y = original_y
        self.picture = None

    def get_team(self):
        return self.team

    def get_picture(self):
        return self.picture

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, new_x):
        self.x = new_x

    def set_y(self, new_y):
        self.y = new_y


class Pawn(Piece):
    def __init__(self, team_n, original_x, original_y):
        super().__init__(team_n, original_x, original_y)
        # if self.team == "white":
        #     self.picture = pygame.image.load("white_pawn.png")
        # else:
        #     self.picture = pygame.image.load("black_pawn.png")


class Bishop(Piece):
    def __init__(self, team_n, original_x, original_y):
        super().__init__(team_n, original_x, original_y)
        self.team = team_n


class Rooke(Piece):
    def __init__(self, team_n, original_x, original_y):
        super().__init__(team_n, original_x, original_y)
        self.team = team_n


class Queen(Piece):
    def __init__(self, team_n, original_x, original_y):
        super().__init__(team_n, original_x, original_y)
        self.team = team_n


class Knight(Piece):
    def __init__(self, team_n, original_x, original_y):
        super().__init__(team_n, original_x, original_y)
        self.team = team_n


class King(Piece):
    def __init__(self, team_n, original_x, original_y):
        super().__init__(team_n, original_x, original_y)


class Empty(Piece):
    def __init__(self, team_n, original_x, original_y):
        super().__init__(team_n, original_x, original_y)