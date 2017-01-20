#Palindrome Checker

import sys

while(1==1):
    print "Palindrome Checker"
    IN = raw_input("Enter the word you would like to check: ")

    word = IN.lower()

    middle_posn = len(word)/2
    first_half = word [ :middle_posn]
    second_half = word [ -middle_posn : ] #This removes the hassle of odd and even length words

    first_half.find(second_half[::-1])
    if word == "exit":
        sys.exit("The Palindrome Checker Program has ended")
    elif first_half.find(second_half[::-1]) == 0:
        print IN + " is a Palindrome\n"
    else:
        print IN + " is not a Palindrome\n"
