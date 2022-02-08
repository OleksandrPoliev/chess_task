
limits =[1,2,3,4,5,6,7,8]
limits2=['a','b','c','d','e','f','g','h']

class Figure:
    vertical = ["1", "2", "3", "4", "5", "6", "7", "8"]
    horizontal = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    def __init__(self,data):
        self.data=data
    def list_available_moves(self):
        pass
    def validate_move(self,dest_field):
        pass

    def __str__(self):
        return self.data[1]
class pawl:
    def __init__(self,data):
        self.data=data

    def list_available_moves(self):

        limits = [1, 2, 3, 4, 5, 6, 7, 8]
        limits2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        self.x=self.data[0]
        self.y=int(self.data[1])


        return f"{self.x}{self.y+1}"

    def validate_move(self,dest_field):
        if self.list_available_moves()==dest_field:
            return "ok"
        return "ggvp"



class tower(Figure) :

    def list_available_moves(self):
        available_moves=[]
        vertical = ["1", "2", "3", "4", "5", "6", "7", "8"]
        horizontal = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        self.x=self.data[0]
        self.y=(self.data[1])
        for i in horizontal:
            if i != self.x:
                available_moves.append(i+self.y )
        for i in vertical:
            if i != self.y:
                available_moves.append(self.x + str(i))
        return available_moves

    def validate_move(self,dest_field):
        if dest_field in self.list_available_moves():
            return "ok"

        return "wrong move"



def get_position(figure,position):
    data = figure
    p=position
    if data == "tower":
        inf=tower(p)
        return (inf.list_available_moves())
#
b=tower('a2')
print(b.list_available_moves())
# print(b.validate_move('ar'))

