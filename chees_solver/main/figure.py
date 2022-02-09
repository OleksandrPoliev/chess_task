from abc import ABC, abstractmethod


class Figure(ABC):
    def __init__(self, data):
        self.data = data
        self.x = data[0]
        self.y = data[1]
        self.vertical = ["1", "2", "3", "4", "5", "6", "7", "8"]
        self.horizontal = ["a", "b", "c", "d", "e", "f", "g", "h"]
        self.available_moves = []

    @abstractmethod
    def list_available_moves(self):
        pass

    def validate_move(self, dest_field):
        if dest_field in self.list_available_moves():
            return "This move is available"
        return "You can't make this move"

    def __str__(self):
        return self.x, self.y


class Pawn(Figure):
    def list_available_moves(self):
        if int(self.y) + 1 <= 8:
            if int(self.y) == 2:
                self.available_moves.append(f"{self.x}{int(self.y) + 1}")
                self.available_moves.append(f"{self.x}{int(self.y) + 2}")
                return self.available_moves
            self.available_moves.append(f"{self.x}{int(self.y) + 1}")
            return self.available_moves
        return "invalid data"


class Rook(Figure):
    def list_available_moves(self):
        for i, j in zip(self.horizontal, self.vertical):
            if i != self.x:
                self.available_moves.append(i + str(self.y))
            if j != self.y:
                self.available_moves.append(self.x + str(j))
        return self.available_moves


class King(Figure):
    def list_available_moves(self):
        for i, j in zip(self.horizontal, self.vertical):
            if self.horizontal.index(i) in [
                self.horizontal.index(self.x) - 1,
                self.horizontal.index(self.x),
                self.horizontal.index(self.x) + 1,
            ]:
                for k in range(1, 4):
                    if i + str(k) != str(self.x + self.y):
                        self.available_moves.append(i + str(k))
        return self.available_moves


class Bishop(Figure):
    def list_available_moves(self):
        x_cord = self.horizontal.index(self.x) + 1
        y_cord = self.vertical.index(self.y) + 1
        for i in range(1, 9):
            for z in range(1, 9):
                dx = abs(i - x_cord)
                dy = abs(z - y_cord)
                if (dx == dy) and (dx > 0):
                    self.available_moves.append(f"{self.horizontal[i - 1]}{z}")
        return self.available_moves


class Knight(Figure):
    def list_available_moves(self):
        x_cord = self.horizontal.index(self.x) + 1
        y_cord = self.vertical.index(self.y) + 1
        for colN in range(1, 9):
            for rowN in range(1, 9):
                if (colN == x_cord + 1 or colN == x_cord - 1) and\
                        (rowN == y_cord - 2 or rowN == y_cord + 2):
                    self.available_moves.append(f"{self.horizontal[colN - 1]}"
                                                f"{rowN}")
                elif (rowN == x_cord + 1 or rowN == x_cord - 1) and (
                        colN == y_cord - 2 or colN == y_cord + 2
                ):
                    self.available_moves.append(f"{self.horizontal[colN - 1]}"
                                                f"{rowN}")
        return self.available_moves


class Queen(Figure):
    def list_available_moves(self):
        x_cord = self.horizontal.index(self.x) + 1
        y_cord = self.vertical.index(self.y) + 1
        for i in range(1, 9):
            for z in range(1, 9):
                dx = abs(i - x_cord)
                dy = abs(z - y_cord)
                if (dx == dy) and (dx > 0):
                    self.available_moves.append(f"{self.horizontal[i - 1]}{z}")
        for i, j in zip(self.horizontal, self.vertical):
            if i != self.x:
                self.available_moves.append(i + str(self.y))
            if j != self.y:
                self.available_moves.append(self.x + str(j))
        self.available_moves = sorted(self.available_moves, key=lambda x: x)
        return self.available_moves


dict_figure = {
    "pawn": Pawn,
    "rook": Rook,
    "king": King,
    "bishop": Bishop,
    "knight": Knight,
    "queen": Queen,
}


def get_position(figure, position):
    data = figure
    figure_position = position
    horizontal = ["a", "b", "c", "d", "e", "f", "g", "h"]
    vertical = ["1", "2", "3", "4", "5", "6", "7", "8"]
    if figure_position[0] in horizontal and figure_position[1] in vertical:
        if data in dict_figure.keys():
            z = dict_figure[data](figure_position)
            return z.list_available_moves()
        return "invalid data"
    return "invalid data"


def validate_move_for(figure, position, second):
    data = figure
    figure_position = position
    figure_second_position = second
    horizontal = ["a", "b", "c", "d", "e", "f", "g", "h"]
    vertical = ["1", "2", "3", "4", "5", "6", "7", "8"]
    if figure_position[0] in horizontal and figure_position[1] in vertical:
        if data in dict_figure.keys():
            z = dict_figure[data](figure_position)
            return z.validate_move(figure_second_position)
        return "invalid data"
    return "invalid data"
