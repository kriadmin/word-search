import random

def make(row,column):
    return [['_' for _ in range(column)] for a in range(row)]
def add_horizontally(word,arr,row,column,backwards=False):
    word = word[::-1] if backwards else word
    somearr = list(word)
    for c in somearr:
        arr[row][column] = c
        column += 1
    return arr
def add_vertically(word,arr,row,column,backwards=False):
    word = word[::-1] if backwards else word
    somearr = list(word)
    for c in somearr:
        arr[row][column] = c
        row += 1
    return arr
def add_diagonally(word,arr,row,column,backwards=False):
    word = word[::-1] if backwards else word
    somearr = list(word)
    for c in somearr:
        arr[row][column] = c
        row += 1
        column += 1
    return arr
def printf(arr):
    for row in arr:
        for letter in row:
            print(letter,end=' ')
        print('\n')
def random_condition(rows,columns,backwards=True,diagonals=True):
    row = random.randint(0,rows)
    column = random.randint(0,columns)
    backward = backwards if not backwards else [True,False][random.randint(0,1)]
    diagonal = diagonals if not diagonals else [True,False][random.randint(0,1)]
    return (row,column,backward,diagonal)
def generate(row,column,word_list,backwards=True,diagonal=True):
    pass
print(random_condition(10,10,diagonals=False))
