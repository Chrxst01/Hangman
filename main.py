import random, sys, threading, time

corguess = ""
remain = 12
wguessed = ""


def guess(toguess):

    global corguess
    global remain
    global wguessed
     
    while remain > 0:

        length = len(toguess)


        for i in range(3):
            print('')
        print(f'Length of word >> {length}')
        print(f'Guesses remaining >> {remain}')
        print(f'Correct Letters Guessed >> {corguess}')
        print(f'Wrong Letters Guessed >> {wguessed}')

        for i in range(3):
            print('')


        isguess = input('Enter guess >> ')
        for i in range(3):
            print('')
        if isguess in wguessed:
            print('You have already guessed this letter')
        elif isguess in corguess:
            print('You have already guessed this letter')

        elif len(isguess) > 1:
            if isguess.lower() == toguess:
                print('You Won!')
                sys.exit()
            else:
                print(f'Word {isguess} isnt the word!')
                remain = remain -2
                for i in range(3):
                    print('')


        elif len(isguess) ==1:

            if isguess.lower() in toguess:
                corguess = corguess + f"{isguess}, "
                print('You guessed a letter!')
                for i in range(3):
                    print('')
            else:
                wguessed = wguessed + f"{isguess}, "
                print(f'{isguess} Not in the word!')
                remain = remain -1
                for i in range(3):
                    print('')
    for i in range(3):
        print('')
    guess(toguess)



words = "cross,bait,elfin,building,grip,blade,box,hallowed,rate,whisper,rotten,walk,seemly,rambunctious,fog,wiry,kittens,kick,thaw,husky,medical,maddening,roof,friend,education,discreet,bashful,watch,beautiful,plate,confuse,coherent,maniacal,ball,lace,zealous,chickens,arithmetic,peck,callous,bloody,thankful,class,red,lamp,caption,trucks,tip,ashamed,sidewalk,yoke,contain,promise,pine,cough,deer,abnormal,clumsy,useful,distance,murder,spiritual,profit,print,sort,nondescript,curtain,versed,worried,feigned,unarmed,adamant,excited,enter,swim,rampant,soup,fallacious,fair,carpenter,relieved,cellar,channel,live,phone,wealth,glass,wasteful,curly,wish,decorous,chalk,thrill,note,tall,hover,books,mess up,gorgeous,terrible,nervous,listen,picayune,knowledgeable,rifle,canvas,list,business,guard,subsequent,subtract,defiant,ladybug,kind,treat,tame,connection,summer,unequaled,decay"
print('Press enter to play')
input()

print('Rules')
print('============')
print('A random word will be generated')
print('You will have 12 guesses')
print("""
If you guess a letter, it will take up one guess, 
unless it is in the word. if you guess a wird,
it takes up two guesses unless it is in the word
""")

print('Press enter to begin')
input()


print('Getting random word...')
words = words.split(',')
toguess = random.choice(words)
print(toguess)
print('I am thinking of a word... ')
length = len(toguess)
print(f'it is {length} Letters long... ')
print('Good luck!')
guess(toguess)
