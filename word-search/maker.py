import random
from PIL import ImageFont, ImageDraw, Image
def make(row,column):
    return [['_' for _ in range(column)] for a in range(row)]
def add_horizontally(word,array,row,column,backwards=False):
    arr = list(array)
    row -= 1
    column -= 1
    word = word[::-1] if backwards else word
    somearr = list(word)
    for c in somearr:
        if(arr[row][column] != '_'):
            raise Exception("Oh the letter is already there")
        else:
            arr[row][column] = c
            column += 1
    return arr
def add_vertically(word,array,row,column,backwards=False):
    arr = list(array)
    row -= 1
    column -= 1
    word = word[::-1] if backwards else word
    somearr = list(word)
    for c in somearr:
        if(arr[row][column] != '_'):
            raise Exception("Oh the letter is already there")
        else:
            arr[row][column] = c
            row += 1
    return arr
def add_diagonally(word,array,row,column,backwards=False):
    arr = list(array)
    row -= 1
    column -= 1
    word = word[::-1] if backwards else word
    somearr = list(word)
    for c in somearr:
        if(arr[row][column] != '_'):
            raise Exception("Oh the letter is already there")
        else:
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
def check(condition,word):
    diagonal = condition[0][3]
    row_start = condition[0][0]
    column_start = condition[0][1]
    rows = condition[1]
    columns = condition[2]
    vertical = condition[3]
    if(diagonal):
        if(rows-row_start>len(word) & columns - column_start > len(word)):
            return True
        else:
            return False
    if(vertical):
        if(rows-row_start>len(word)):
            return True
        else:
            return False
    else:
        if(columns - column_start>len(word)):
            return True
        else:
            return False
def random_alpha():
    return 'abcdefghijklmnopqrstuvwxyz'[random.randint(0,25)]
def randomize(arr):
    return [[m if m!='_' else random_alpha() for m in a] for a in arr]
def generate(row,column,word_list,backwards=True,diagonal=True):
    if((max(len(w) for w in word_list) > row) | (max(len(w) for w in word_list) > column)):
        return ('wrong',)
    else:
        pass
    array = make(row,column)
    for word in word_list:
        i = True
        while(i):
            vertical = False
            conditions = random_condition(row,column,backwards=backwards,diagonals=diagonal)
            if(not conditions[3]):
                vertical = [True,False][random.randint(0,1)]
            if (check((conditions,row,column,vertical),word)):
                if(conditions[3]):
                    try:
                        array = add_diagonally(word,array,conditions[0],conditions[1],conditions[2])
                        i = False
                    except Exception:
                        pass
                elif(vertical):
                    try:
                        array = add_vertically(word,array,conditions[0],conditions[1],conditions[2])
                        i = False  
                    except Exception:
                        pass    
                else :
                    try:
                        array = add_horizontally(word,array,conditions[0],conditions[1],conditions[2])
                        i = False
                    except Exception:
                        pass
    return randomize(array)
#printf(generate(15,15,['rohit','priya','santosh','apple','pineapple']))
def draw_text(text, size, fill=None):
    loc = 'C:/Users/rohit/Downloads/OpenSans-Regular.ttf'
    #open(loc).read()
    font = ImageFont.truetype(
        'C:/Users/rohit\Downloads/OpenSans-Regular.ttf', size
    )
    size = font.getsize(text) # Returns the width and height of the given text, as a 2-tuple.
    im = Image.new('RGB', size, (0, 0, 0, 0)) # Create a blank image with the given size
    draw = ImageDraw.Draw(im)
    draw.text((0, 0), text, font=font, fill=fill) #Draw text
    return im
def text(arr):
    str = ''
    for row in arr:
        for word in row:
            str += word + ' '
        str += '\n'
    return str
open('test.txt','w').write(text(generate(15,15,['rohit','priya','santosh','apple','pineapple'])))
#img.save('out.jpeg')
print(text(generate(15,15,['rohit','priya','santosh','apple','pineapple'])))