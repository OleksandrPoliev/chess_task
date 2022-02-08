from abc import ABC, abstractmethod



class Figure(ABC):
    global vertical,horizontal
    vertical = ["1", "2", "3", "4", "5", "6", "7", "8"]
    horizontal = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    def __init__(self, data):
        self.data = data
        self.x = self.data[0]
        self.y = int((self.data[1]))
        self.available_moves = []

    @abstractmethod
    def list_available_moves(self):
        pass


    def validate_move(self, dest_field):
        if dest_field in self.list_available_moves():
            return "This move is available"
        return "You can't make this move"

    def __str__(self):
        return self.data


class pawl(Figure):
    def list_available_moves(self):
        if self.y == 2:
            self.available_moves.append(f'{self.x}{self.y + 1}')
            self.available_moves.append(f'{self.x}{self.y + 2}')
            return self.available_moves
        self.available_moves.append(f"{self.x}{self.y + 1}")
        return self.available_moves




class tower(Figure):

    def list_available_moves(self):

        self.x = self.data[0]
        self.y = (self.data[1])
        for i,j in zip(horizontal,vertical):
            if i != self.x:
                self.available_moves.append(i + self.y)
            if j != self.y:
                self.available_moves.append(self.x + str(j))
        return self.available_moves



def get_position(figure, position):
    data = figure
    p = position
    if data == "tower":
        inf = tower(p)
        return (inf.list_available_moves())


#

