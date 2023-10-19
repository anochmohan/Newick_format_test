#!/usr/bin/env python3

import sys
pattern = sys.argv[1]
#print(pattern)
def check(pattern: str) -> str:
    """Takes in parenthesis as input to check if they are paird or not
    
        Args:
            pattern: open or close parenthesis
    """

    # Counts the charecter in pattern
    counter=0

    # For loop to check each charecter in pattern;
    # if the counter ever hits -1 while in the loop - it breaks
    # at the end if the counter is 0, then it is paired, if not its not paired
    for i in pattern:
        if i == "(":
            counter+=1
        elif i == ")":
            counter-=1
        if counter == -1:
            break

    # checks the counter count
    if counter != 0:
        print("NOT PAIRED")
    else:
        print("PAIRED")


check(pattern)