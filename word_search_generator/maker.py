import random
from copy import deepcopy
def make(row,column):
    return [['_' for _ in range(column)] for a in range(row)] # Generates a empty array of specified width(column) and height(row)
def add_horizontally(word,array,row,column,backwards=False):
    arr = deepcopy(array) #Copy the array because we may make unwanted mutations
    word = word[::-1] if backwards else word #If backwards is true reverse the word
    somearr = list(word)
    for c in somearr:
        if((arr[row][column] != '_') & (arr[row][column] != c)): #If there already exists a character and it is not same as c then
            raise Exception("Oh the letter is already there") #Throw a error
        else:
            arr[row][column] = c #Else add the letter to the correct row and column
            column += 1 #Increase column by 1
    return arr
def add_vertically(word,array,row,column,backwards=False): #Same as add horizontally except it increases row by 1
    arr = deepcopy(array)
    word = word[::-1] if backwards else word
    somearr = list(word)
    for c in somearr:
        if((arr[row][column] != '_') &  (arr[row][column] != c)):
            raise Exception("Oh the letter is already there")
        else:
            arr[row][column] = c
            row += 1
    return arr
def add_diagonally(word,array,row,column,backwards=False): #Same as add_vertically except increase both row and cloumn by 1
    arr = deepcopy(array)
    word = word[::-1] if backwards else word
    somearr = list(word)
    for c in somearr:
        if((arr[row][column] != '_') & (arr[row][column] != c)):
            raise Exception("Oh the letter is already there")
        else:
            arr[row][column] = c
            row += 1
            column += 1
    return arr
def horizontal_add(word,arr,row,column):
    return add_horizontally(word,arr,row,column,False)
def horizontal_add_backwards(word,arr,row,column):
    return add_horizontally(word,arr,row,column,True)
def vertical_add(word,arr,row,column):
    return add_vertically(word,arr,row,column,False)
def vertical_add_backwards(word,arr,row,column):
    return add_vertically(word,arr,row,column,True)
def diagonal_add(word,arr,row,column):
    return add_diagonally(word,arr,row,column,False)
def diagonal_add_backwards(word,arr,row,column):
    return add_diagonally(word,arr,row,column,True)
def horizontal_check(arr,row,column,word):
    for letter in list(word):
        
        try:
            if((arr[row][column] == '_') or (arr[row][column] == letter)):
                pass
            else:
                return False
        except:
            return False
        column += 1
    return True
def horizontal_check_backwards(arr,row,column,word):
    word = word[::-1]
    for letter in list(word):
        
        try:
            if((arr[row][column] == '_') or (arr[row][column] == letter)):
                pass
            else:
                return False
        except:
            return False
        column += 1
    return True
def vertical_check(arr,row,column,word):
    for letter in list(word):
        
        try:
            if((arr[row][column] == '_') or (arr[row][column] == letter)):
                pass
            else:
                return False
        except:
            return False
        row += 1
    return True
def vertical_check_backwards(arr,row,column,word):
    word = word[::-1]
    for letter in list(word):
        
        try:
            if((arr[row][column] == '_') or (arr[row][column] == letter)):
                pass
            else:
                return False
        except:
            return False
        row += 1
    return True
def diagonal_check(arr,row,column,word):
    for letter in list(word):
        
        try:
            if((arr[row][column] == '_') or (arr[row][column] == letter)):
                pass
            else:
                return False
        except:
            return False
        column += 1
        row += 1
    return True
def diagonal_check_backwards(arr,row,column,word):
    word = word[::-1]
    for letter in list(word):
        try:
            if((arr[row][column] == '_') or (arr[row][column] == letter)):
                pass
            else:
                return False
        except:
            return False
        column += 1
        row += 1
    return True
def random_condition(arr,word):
    indexes = []
    row = len(arr)
    column = len(arr[0])
    for i in range(row):
        for j in range(column):
            indexes.append([i,j])
    random.shuffle(indexes)
    for index in indexes:
        tests = [horizontal_check,vertical_check,horizontal_check_backwards,vertical_check_backwards,diagonal_check,diagonal_check_backwards]
        random.shuffle(tests)
        for test in tests:
            if(test(arr,index[0],index[1],word)):
                return (test.__name__,index[0],index[1])
    raise Exception('Word cannot be fitted')
def check(condition,word): # Check ifthe provided condition is fitting i.e. there should be no out of index problem
    diagonal = condition[0][3]
    row_start = condition[0][0]
    column_start = condition[0][1]
    rows = condition[1]
    columns = condition[2]
    vertical = condition[3]
    if(diagonal):
        if(((rows-row_start) >= len(word)) & ((columns - column_start) >= len(word))):
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
def random_alpha(): # Returns a random alphabet
    return 'abcdefghijklmnopqrstuvwxyz'[random.randint(0,25)]
def randomize(arr): # After the grid is made fill the remaining places with randome characters
    return [[m if m!='_' else random_alpha() for m in a] for a in arr]
def generate(row,column,word_list,backwards=True,diagonal=True): # Uses all the above methods to make array
    if((max(len(w) for w in word_list) > row) | (max(len(w) for w in word_list) > column)): #If the word is larger than row or column length than return 'wrong'.
        raise Exception("Word Length can't be more than the number of rows or cloumns")
    else:
        pass
    array = make(row,column)
    for word in word_list:
        condition = random_condition(array,word)
        array = deepcopy(globals()[condition[0].replace('check','add')](word,array,condition[1],condition[2]))
    return (array) # Fill with random characters
def text(arr): # Convert given array to text  
    string = ''
    for row in arr:
        for word in row:
            string += str(word) + ' '
        string += '\n'
    return string
#open('test.txt','w').write(text(generate(15,15,['Lord','Voldemort','likes','penpineapple','applepen']))) # To test it!
#print(text(make(30,10)))

