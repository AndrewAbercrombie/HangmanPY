import urllib.request
import urllib.parse
import random
import HangmanPics
import os




def handleCommands():

    tempCommand = input("Enter a command (Type 'HELP' for a list of commands): \t")
    tempCommand = tempCommand.lower()

    tempCommand = tempCommand.strip()

    if tempCommand == 'clear' or tempCommand == 'cls':
        os.system('cls')
        handleCommands()
    elif tempCommand == 'newgame':
        os.system('cls')
        main() 
    elif tempCommand == 'help':
        print('\n\n\tCommand List: \n\tnewgame: Start a new game\n\tclear: Clear the console\n\texit: Exit the game\n\n')
        handleCommands()
    elif tempCommand == 'exit':
        os._exit(0)
    else:
        print("\nUnknown command. Type HELP for a list of commands..\n\n")
        handleCommands()
        
   

def firstGame():
    
    print("Welcome to The Better Hangman - Developed By Andrew Abercrombie \n\n\n")



#This function is used to find the position that a char is in a string.
def charposition(string, char):
    pos = [] #list to store positions for each 'char' in 'string'
    for n in range(len(string)):
        if string[n] == char:
            pos.append(n)
    return pos


#this function is used to insert a character into a string
def insertChar(mystring, position, chartoinsert ):
    longi = len(mystring)
    mystring   =  mystring[:position] + chartoinsert + mystring[position:] 
    return mystring

#This function is used to remove characters from a string 
def remove_char(input_string, index):
    first_part = input_string[:index]
    second_part = input_string[index+1:]
    return first_part + second_part

#this function will simply check if the user has won the game
def checkForWin(string_to_check):
    temp = string_to_check
    if '-' in temp:
        return False
    else:
        return True


def main():
    #base variables
    lifeCount = 6
    word_to_show_user = ''
    X = 0
    Blank = True


    #URL to pull all the words from
    url = 'https://pastebin.com/raw/7KJNUqax'

    #Download the site as string
    f = urllib.request.urlopen(url)

    #Decode the site
    words = f.read().decode('utf-8')

    #split them into an array
    wordsSplit = words.split("\n")

    #generate a random number
    ranNumber = random.randint(0,999)

    #get a random word based on the random number
    randWord = wordsSplit[ranNumber]

    #remove spaces in the word
    randWord = randWord.replace(" ", "")

    #calculate the length of the word to get the "Show word" for the user
    length_of_word = len(randWord) - 1

    #create the "Show word"  
    while X < length_of_word:
        word_to_show_user = word_to_show_user + '-'
        X = X + 1

    #print the show word for the user
    print("Your word is: " + word_to_show_user + " Good Luck!")


    #start the actual game
    while lifeCount > 0:
        

        #make sure they dont enter a space and its only one character
        while Blank == True:
            #get a letter from the user
            letter_to_check = input("Guess a letter: ")
            if letter_to_check.strip() != '' and len(letter_to_check)== 1:
                Blank = False
        
        #reset this for the next time
        Blank = True
        
        #Ensure that the string is lowercase
        letter_to_check = letter_to_check.lower()

        #check if the letter is in the word
        if letter_to_check in randWord:

            #find the position that it is in the word
            position = charposition(randWord,letter_to_check)

            #convert this to string for parsing 
            position = str(position)

            #check if this letter appears mutiple times   
            if ',' in position:

                #remve all the not needed characters
                temp = position.replace("[",'')
                temp = temp.replace("]",'')
                temp = temp.replace(", ",',')

                #split it over the , so we can find all places its in the string
                tempSpl = temp.split(',')

                #loop though all the index's that the character appears
                for X in tempSpl:

                    #insert the character into the string and remove the asterisk for the user to see.
                    word_to_show_user = insertChar(word_to_show_user, int(X), letter_to_check)
                    word_to_show_user = remove_char(word_to_show_user, int(X) + 1)

                #print the result for the user
                print(word_to_show_user + '\n')
                
                #check if the user has won yet.
                if checkForWin(word_to_show_user) == True:

                    #the user won
                    print("You WIN, the word was: " + word_to_show_user)
                    commandToPass = input("Enter a command (Type 'HELP' for a list of commands): \t")
                    commands.handleCommands(commandToPass)
            else:
                #this means the letter appears once in the string

                #remove all not needed characters
                temp = position.replace("[",'')
                temp = temp.replace("]",'')

                #insert the character and remove the asterisk 
                word_to_show_user = insertChar(word_to_show_user, int(temp), letter_to_check)
                word_to_show_user = remove_char(word_to_show_user, int(temp) + 1)

                #print the result for the user
                print(word_to_show_user+ '\n')

                #Check if the user has won yet.
                if checkForWin(word_to_show_user) == True:
                    print("You WIN, the word was: " + word_to_show_user)
                    commandToPass = input("Enter a command (Type 'HELP' for a list of commands): \t")
                    commands.handleCommands(commandToPass)

        else:
            #this means that the user entered a letter thats not in the word


            #deduct a life
            lifeCount = lifeCount - 1
            
            #check if there out of lives.
            if lifeCount == 0:
                print('\t\t' + HangmanPics.pics[(6 - (lifeCount + 1))])
                print("You lose! The word was " + randWord + '\n\n' )
                
                handleCommands()
                
            #user still has lifes tell them how many.
            print('\t\t' + HangmanPics.pics[(6 - (lifeCount + 1))])
            print("You have: " + str(lifeCount) + " lives left! \n")

            
firstGame()
handleCommands()

            

