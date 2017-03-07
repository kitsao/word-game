# Python Word Game
#
# Technical Interview Deliverable
# Created by: Kitsao Emmanuel
# Implemented by: Kitsao Emmanuel
#
from wordgame import *
import random
import string
import sys
import time
import random

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a Set of valid words. Words are strings of lowercase letters.

    Depending on the size of the word Set, this function may
    take a while to finish.
    """
    print "Loading word Set from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordSet: Set of strings
    wordSet = set(line.strip().lower() for line in inFile)
    print len(wordSet), "words loaded."
    print "---------------------------------------------------------\n"
    return wordSet
# (end of helper code)
# -----------------------------------
#
# Function #0: Introduction and tips
#
def intro():
    print "=========================================================\n"
    print "Hello and welcome to this simple two-player word game.\n"
    print "1. You or the computer may give the first letter."
    print "2. Take turns saying a letter."
    print "3. If a player says a word that ends a word, they lose."
    print "4. A letter that does not spell a word leads to a loss."
    print "=========================================================\n"


#
# Function #1: Test letter validity
#
def isValidLetter(letter):
    """
    Returns True if a letter is valid.

    letter: Entered letter
    """
    if letter.isalpha():
        return True
    return False
#
# Function #2: Check that only one letter is entered
#
def isOneLetter(letter):
    """
    Returns True if a single letter is entered.

    letter: Entered letter
    """
    if len(letter)==1:
        return True
    return False


#
# Function #3: Get the last characters of all strings in the loaded words
#

def getLastChars(wordSet):
    """
    Returns a Set of characters at the end of each string

    wordSet: Set of loaded words
    returns: unique array of characters
    """
    lttrs = []
    for word in wordSet:
        lttrs.append(word[-1:])
    return lttrs


#
# Function #4: Get the last characters of all strings in the loaded words
#
def getPreceedingChars(word, wordSet):
    """
    Return Set of the possible preceeding letter after a chosen letter

    wordSet: Set of loaded words
    returns: unique array of characters
    """
    # Declare variable for length of the current word.
    lttrs = []
    word_len = 0
    for ross in wordSet:
        if word:
            word_len=len(word)
        lttrs.append(ross[word_len:word_len + 1])
    return lttrs


#
# Function #5: Trim the Set of words using the given substring
#
def getTrimmedSet(word, wordSet):
    """
    Return Set words beginning with the given substring

    wordSet: Set of loaded words
    returns: unique array of characters
    """
    newWordSet=set()
    for i in wordSet:
        if i.startswith(word):
            newWordSet.add(i)
    return newWordSet


#
# Function #6: Check if letter ends a word
#
def getEndsWord(word, wordSet):
    """
    Checks if given letter ends a word.
    word: string (lowercase letters)
    letter: is the given letter
    """
    counter = 0
    if word == '':
        return 0
    for wrd in wordSet:
        if wrd.endswith(word) or word not in wrd:
            counter += counter
        return counter


#
# Function #7: Playing a letter
#
def playLetter(wordSet, ltr):
    """
    Allows the user to enter a letter:

    * The user must enter a letter to begin the game.
    * Invalid letters rejected and user prompted to enter valid word or "."
    * When a valid letter is entered, the other user must deal a letter.
    * If user enters a letter that ends a word, or a letter that leads to a
      non-existing word, the user loses the game.

      word: String of letters so far

    """
    # While there are possible words to be played:
    if ltr:
        print('\n')
        print('Current Letter(s): ' + ltr)
    # Prompt user for input
    letter = raw_input('Enter letter, or a "." quit: ')
    # If the input is a single period:
    if letter == '.':
        # Quit the game (break out of the loop)
        sys.exit(0)

    # Else proceed with the game:
    else:
        # Check if letter is valid:
        if not isValidLetter(letter) and not isOneLetter(letter):
            # Reject input with notification
            print('\n' + 'Invalid letter, please try again.')
        # Otherwise:
        else:
            # Update the word Set
            if ltr:
                letter = ltr+letter
            wordSet = getTrimmedSet(letter, wordSet)
    # Computer's turn to play
    if winOrLoss(letter, wordSet)==0:
        compPlayLetter(wordSet, letter)
    else:
        print "---------------------------------------------------------\n"
        print("Game Over. You Lost.")
        print "---------------------------------------------------------\n"
        sys.exit(0)
#
# Function #8: Playing a game
#

def playGame(wordSet):
    """
    Keep the game in play.

    When done playing the hand, repeat from step 1
    """
    choice = ''
    while True:
        choice = raw_input('Enter n to play, or e to end game: ')
        if choice == 'n':
            playLetter(wordSet)
        elif choice == 'e':
            break
        else:
            print "Invalid command."

#
#
# Function #9: Computer chooses a letter
#
#
def compChooseWord(wordSet, ltr):
    """
    Given the current string and Set of words, return the best letter
    ltr: Currently available letters
    wordSet: Set of valid words loaded

    returns: string
    """
    # New letter variable
    best_letter = ''
    # Get Set of last characters
    last_chars=set(getLastChars(wordSet))
    # Get all possible next characters
    next_chars=set(getPreceedingChars(ltr, wordSet))
    # Strip characters in last_chars from next_chars
    if len(next_chars)==1:
        best_letter=''.join(next_chars)
    else:
        best_letter=random.choice(tuple(next_chars))
    # return the best letter found.
    return best_letter

#
# Function #10: Computer plays a letter
#
def compPlayLetter(wordSet, ltr):
    """
    Allows the computer to play, computer chooses a letter.

    1) The computer chooses a letter.
    2) The letter may not end a word.
    3) The letter must lead to a valid word.
 
    letter: letter to be chosen
    wordSet: Set of valid words loaded
    """
    if ltr:
        print('\n')
        print('Current Letter(s): ' + ltr)
    letter = compChooseWord(wordSet, ltr)
    if isValidLetter(letter):
        print('Computer\'s Letter: ' + letter + '\n'),
    if ltr:
        letter = ltr+letter
    # Other player's turn to play
    if winOrLoss(letter, wordSet)==0:
        playLetter(wordSet, letter)
    else:
        print "---------------------------------------------------------\n"
        print("Hoooooooray! You won!")
        print "---------------------------------------------------------\n"
        sys.exit(0)
#
# Function #11: Playing the game
#
#
def playGame(wordSet):
    """
    Play the game
    wordSet: Set of loaded words
    """
    choice = ''
    while True:
        choice = raw_input('Enter n to start the game, or e to end game: ')
        if choice == 'e':
            break
        while True:
            player = raw_input('Enter u to have yourself play, c to have the computer play: ')
            if player != 'u' and player != 'c':
                print "Invalid command."
                continue
            if player == 'u':
                playLetter(wordSet, ltr=None)
            elif player == 'c':
                compPlayLetter(wordSet, ltr=None)
            break

#
# Function #12: Win/Loss function
#
def winOrLoss(str, wordSet):
    """
    Returns True if a letter is valid.

    str: Current letters
    wordSet: Set of loaded words
    """
    wordList=list(wordSet)
    available=[]
    counter=0
    count=0
    if str in wordList:
        counter=1
    for wrdlst in wordList:
        if wrdlst==str:
            available.append(wrdlst)
    if counter==0 and len(available)==0:
        return 0
    else:
        return 1
#
# Data structures for use during the game
#
if __name__ == '__main__':
    intro()
    wordSet = loadWords()
    playGame(wordSet)