# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 16:46:11 2020

@author: Mani
"""

import random
maxn = 21
maxn1 = 20
activecases = random.randint(1, maxn1)
print("welcome to COVID 19 stay at home game")
print("this is a guessing game to detect number of active cases")
print("whats your name?")
myname=input()
print(myname + " guess the number of active cases")
guess=""
while guess != activecases:  
      guess = int(input("your try\n"))
      if guess > activecases:
          print("too high, try again\n")
          if guess > maxn:
                  print("extreme situation\n")
      if guess < activecases:
          print("too low, try again")
print("congrats " + myname)
print("you win")