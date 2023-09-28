# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 19:26:23 2021

@author: ASUS
"""

print("There are 21 matchsticks.You are allowed to pick between 1-4 sticks at a time.Last to pick a matchstick loses")
print()

def matches():
    s = (5 - n)
    print("Bot chose: ",s)

for i in range(1,5):
    n = int(input("Enter a number from 1 to 4: "))
    matches()
    i=i+1

print("You Picked the last match stick, You lose.")