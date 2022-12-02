#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 21:32:15 2022

@author: roscopikotrain
"""

from functools import cmp_to_key


class Player:
    def __init__(self, name, score):
        self._name = name
        self._score = score
        
    def __repr__(self):
        rep = 'Player(' + self._name + ',' + str(self._score) + ')'
        return rep
        
    def comparator(a, b):
        """ The comparator"""
        if a._score < b._score: return -1
        elif a._score == b._score: return 0
        else: return 1


if __name__ == '__main__': 
    
########################## Testing ##########################################
    import unittest
  
    class Test_Player_class(unittest.TestCase):
        
        def test_repr(self):
            testPlayer = Player('Dave', 23)
            print(testPlayer)
            
        def test_comparator(self):
            playerA = Player('Dave', 23)
            playerB = Player('Sally', 37)
            print(playerA.comparator(playerB))
            
    unittest.main()
            