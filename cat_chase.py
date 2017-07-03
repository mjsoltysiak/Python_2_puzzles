# -*- coding: utf-8 -*-
"""
Created on Mon Jul 03 10:59:17 2017

@author: Maciej Soltysiak

Puzzle from: https://www.theguardian.com/science/2017/jul/03/can-you-solve-it-are-you-smarter-than-a-cat

A straight corridor has 7 doors along one side. Behind one of the doors sits a cat.
Your mission is to find the cat by opening the correct door. Each day you can open only one door. 
If the cat is there, you win. You are officially smarter than a cat. If the cat is not there, the door closes, 
and you must wait until the next day before you can open a door again.
If the cat was always to sit behind the same door, you would be able to find it in at most seven days, 
by opening each door in turn. But this mischievous moggy is restless. 
Every night it moves one door either to the left or to the right.
How many days do you now need to make sure you can catch the cat?
"""

import random as rand
import itertools

doors = [1,2,3,4,5]
left_edge = min(doors)
right_edge = max(doors)
n_experiments  = 50
wins = 0


def cat_moves(cat_position):
        cat_position += rand.choice([1,-1])
        if cat_position == left_edge-1:
            cat_position = left_edge+1
        if cat_position == right_edge+1:
            cat_position = right_edge-1
        return cat_position

def chase_cat(moves_list):
    cat_position = rand.choice(doors)       
    for move in moves_list:
        if cat_position == move:
            return 1
        cat_position = cat_moves(cat_position) 
    return 0
 
def test_single_solution(solution_moves,n_experiments2): 
    wins = 0
    for i in range(n_experiments2):
        wins += chase_cat(solution_moves)  
    if wins == n_experiments2:
        print(solution_moves)
        print("You have always caught a cat!")
        return True
    return False

def search_all_possible_solutions(doors):
    solutions = []
    final_solutions = []
    for moves in itertools.product(doors,repeat = (2*len(doors)-4)):
        wins = 0
        #print(moves)  
        for i in range(n_experiments):
            wins += chase_cat(moves)  
        if wins == n_experiments:
            solutions.append(moves)
            #print("You have always caught a cat!")
            
    for solution in solutions:
        if(test_single_solution(list(solution),1000)):
            final_solutions.append(solution)
    
    return final_solutions
        
        
        
print(search_all_possible_solutions(doors)) 

 
        
