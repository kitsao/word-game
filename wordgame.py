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
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print len(wordList), "words loaded."
    print "---------------------------------------------------------\n"
    return wordList


def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq


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

def getLastChars(wordList):
    """
    Returns a list of characters at the end of each string

    wordList: List of loaded words
    returns: unique array of characters
    """
    lttrs = []
    for word in wordList:
        lttrs.append(word[-1:])
    return lttrs


#
# Function #4: Get the last characters of all strings in the loaded words
#
def getPreceedingChars(word, wordList):
    """
    Return list of the possible preceeding letter after a chosen letter

    wordList: List of loaded words
    returns: unique array of characters
    """
    # Declare variable for length of the current word.
    lttrs = []
    word_len = 0
    for ross in wordList:
        if word:
            word_len=len(word)
        lttrs.append(ross[word_len:word_len + 1])
    return lttrs


#
# Function #5: Trim the list of words using the given substring
#
def getTrimmedList(word, wordList):
    """
    Return list words beginning with the given substring

    wordList: List of loaded words
    returns: unique array of characters
    """
    newWordList=[]
    for i in wordList:
        if i.startswith(word):
            newWordList.append(i)
    return newWordList


#
# Function #6: Check if letter ends a word
#
def getEndsWord(word, wordList):
    """
    Checks if given letter ends a word.
    word: string (lowercase letters)
    letter: is the given letter
    """
    counter = 0
    if word == '':
        return 0
    for wrd in wordList:
        if wrd.endswith(word) or word not in wrd:
            counter += counter
        return counter


#
# Function #7: Playing a letter
#
def playLetter(wordList, ltr):
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
            # Update the word list
            if ltr:
                letter = ltr+letter
            wordList = getTrimmedList(letter, wordList)
    # Computer's turn to play
    if winOrLoss(letter, wordList)==0:
        compPlayLetter(wordList, letter)
    else:
        print "---------------------------------------------------------\n"
        print("Game Over. You Lost.")
        print "---------------------------------------------------------\n"
        sys.exit(0)
#
# Function #8: Playing a game
#

def playGame(wordList):
    """
    Keep the game in play.

    When done playing the hand, repeat from step 1
    """
    choice = ''
    while True:
        choice = raw_input('Enter n to play, or e to end game: ')
        if choice == 'n':
            playLetter(wordList)
        elif choice == 'e':
            break
        else:
            print "Invalid command."

#
#
# Function #9: Computer chooses a letter
#
#
def compChooseWord(wordList, ltr):
    """
    Given the current string and list of words, return the best letter
    ltr: Currently available letters
    wordList: List of valid words loaded

    returns: string
    """
    # New letter variable
    best_letter = ''
    # Get list of last characters
    last_chars=list(set(getLastChars(wordList)))
    # Get all possible next characters
    next_chars=list(set(getPreceedingChars(ltr, wordList)))
    # Strip characters in last_chars from next_chars
    if len(next_chars)==1:
        best_letter=''.join(next_chars)
    else:
        best_letter=random.choice(next_chars)
    # return the best letter found.
    return best_letter

#
# Function #10: Computer plays a letter
#
def compPlayLetter(wordList, ltr):
    """
    Allows the computer to play, computer chooses a letter.

    1) The computer chooses a letter.
    2) The letter may not end a word.
    3) The letter must lead to a valid word.
 
    letter: letter to be chosen
    wordList: list of valid words loaded
    """
    if ltr:
        print('\n')
        print('Current Letter(s): ' + ltr)
    letter = compChooseWord(wordList, ltr)
    if isValidLetter(letter):
        print('Computer\'s Letter: ' + letter + '\n'),
    if ltr:
        letter = ltr+letter
    # Other player's turn to play
    if winOrLoss(letter, wordList)==0:
        playLetter(wordList, letter)
    else:
        print "---------------------------------------------------------\n"
        print("Hoooooooray! You won!")
        print "---------------------------------------------------------\n"
        sys.exit(0)
#
# Function #11: Playing the game
#
#
def playGame(wordList):
    """
    Play the game
    wordList: list of loaded words
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
                playLetter(wordList, ltr=None)
            elif player == 'c':
                compPlayLetter(wordList, ltr=None)
            break

#
# Function #12: Win/Loss function
#
def winOrLoss(str, wordList):
    """
    Returns True if a letter is valid.

    str: Current letters
    wordList: List of loaded words
    """
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
    wordList = loadWords()
    playGame(wordList)