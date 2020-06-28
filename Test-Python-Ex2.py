# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 09:14:53 2020

@author: Morgann
"""

##In a lottery game, there is a container which contains 50 balls numbered from 1 to 50. 
#The lottery game consists in picking 10 balls out of the container, and ordering them in ascending order. 
#Write a Python function which generates the output of a lottery game (it should return a list). 
#Also describe which unit tests you could implement to test the output of your function.
import random as rd

def lottery_game():
    Container = range(1,51)  ##on crée le container de 50 boules
    Output = []
    for i in range(10):
        Output += [rd.choice(Container)]    ## On choisit 10 boules au hasard dans le container
        Container.remove(Output[i])         ## qu'on enleve enseuite pour ne pas qu'elle apparaisse 2 fois
    return sorted(Output)

## To test this function, we could run it many times in order to check the number of occurence, to check if it's totally random or not.