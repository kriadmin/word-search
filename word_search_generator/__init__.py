import maker
generate = maker.generate
text = maker.text
def generator(row,column,word_list,backwards = True,diagonal = False):
    for i in range(len(word_list)):
        word_list[i] = word_list[i].lower()
    if((row < 5) |(column < 5)):
        raise Exception("Row and Column Length has to be greater than 5")
    elif(min(len(w) for w in word_list) < 4):
        raise Exception("The minimum length has to be less than 4")
    else:
        for w in word_list:
            if(not w.isalpha()):
                raise Exception("Words can contain only english alphabets")
    return text(generate(row,column,word_list,backwards,diagonal))
if __name__ == '__main__':
    print(generator(7,7,['Lord','Voldemo','likes','penpine','apple']))
