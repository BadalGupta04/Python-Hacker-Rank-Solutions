def minion_game(string):
    # your code goes here
    stuart = 0
    kevin = 0
    s = len(string)
    vow = 'AEIOU'
    
    
    for i in range (s):
        if string[i] in vow:
            kevin += s - i
        else:
            stuart += s - i
            
    if stuart > kevin:
        print("Stuart {}".format(stuart))
    elif kevin == stuart:
        print("Draw")        
    else:
        print("Kevin {}".format(kevin))
        

if __name__ == '__main__':
    s = input()
    minion_game(s)