# -*- coding: utf-8 -*-

"""
Created on Wed Sep 13 09:45:20 2017

@author: Maciej Soltysiak

You are given data to calculate viral potential, represented by a network of people ready to relay a message to more people.
We can assume this network contains no cyclic relation. 
For example, if person #1 has a relation with person #2 and if person #2 has a relation with person #3, 
then it is impossible for #3 to have a direct relation with #1.
 
When an individual broadcasts a message, it is counted as a single step, meaning that the time it takes
to broadcast the message is independant from
the amount of people in direct relation with the individual. 
We will consider that this event will always take 1 hour.


Input
Line 1: N the number of adjacency relations.
N next lines: an adjancency relation between two people, expressed as X (space) Y, meaning that X is adjacent to Y.
Output
The minimal amount of steps required to completely propagate the advertisement.
Contraints
0 < N< 150000
0 ≤ X,Y < 200000

Examples
Input
7
1 2
2 3
3 4
3 7
4 5
4 6
7 8

Output
2

Input
7
1 2
2 3
2 4
3 5
3 6
4 7
4 8

Output
2
"""

import sys
import math
from collections import defaultdict

# python 3 version
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

         
def remove_unused_keys(d):
    keys = d.keys()
    for k in list(keys):
        d[k] = d[k] - nodes_to_be_deleted 
        if not d[k]:
            del d[k]
                

n = int(input())  # the number of adjacency relations
nodes = defaultdict(set)
for i in range(n):
    # xi: the ID of a person which is adjacent to yi
    # yi: the ID of a person which is adjacent to xi
    xi, yi = [int(j) for j in input().split()]
    nodes[xi].add(yi)
    nodes[yi].add(xi)

min_popagation_path_len  = 0
nodes_to_be_deleted = set()

while(len(nodes)>0):
    
    for i in range(n+1):
        if len(nodes[i]) == 1:
            del nodes[i]
            nodes_to_be_deleted.add(i)
            #print("Deleting node: {}".format(i))
    if not nodes_to_be_deleted:
        break
    min_popagation_path_len += 1   
    remove_unused_keys(nodes)
    nodes_to_be_deleted.clear()


# The minimal amount of steps required to completely propagate the advertisement
print(min_popagation_path_len)
