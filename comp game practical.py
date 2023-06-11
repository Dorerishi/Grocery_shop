# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 22:28:27 2020

@author: hrushikesh
"""
thespace='''



































'''
#hangman
hangmanfinal='''       
       __________________
       |               __|__
       |              | X X |
       |              |_____|
       |                 |
       |               __|__
       |                _|_
_______|______         |   |'''

hang='''       
       __________________
       |                 |
       |
       |
       |
       |
       |
_______|______'''
hang_head='''       
       __________________
       |               __|__
       |              |     |
       |              |_____|
       |
       |
       |
_______|______'''
hang_head_body='''       
       __________________
       |               __|__
       |              |     |
       |              |_____|
       |                 |
       |                 |
       |                 |
_______|______'''
print('         HANGMAN       ')
import random
comp_words=["stack", "overflow", "rocks"]
spacing=' __ '
vowels=['a','e','i','o','u',' ']
consonents=['q', 'w', 'r', 't', 'y', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
wrongs=0
while True:
    type_of_game=input('write (pvp) for player vs player and (pvc) for player vs computer(type exit to exit):')
    if type_of_game=='pvp':
        w=input("write word:")
    elif type_of_game=='pvc':
        w=random.choice(comp_words)
    elif type_of_game=="exit":
        print('thank you for playing')
        break
    else:
        print('error try again')
        continue
    word=w.lower()
    word_l=[]
    word_g=''
    wrongs=0
    vowels=['a','e','i','o','u',' ']
    consonents=['q', 'w', 'r', 't', 'y', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
    if word.isalpha():
        for i in word:
            word_l.append(i)
        #print('word_l')
        for letter in word_l:
            for v in vowels:
                if v==letter:
                    word_g+=letter
            for c in consonents:
                if c==letter:
                    word_g+=spacing
        print(thespace,word_g)
        while wrongs<4:
            inp=input("write one letter:")
            inp_letter=inp.lower()
            for x in word_l:
                if x==inp_letter:
                    #print(word_g.count(inp_letter))
                    if word_g.count(inp_letter)==1:
                        continue
                    elif word_g.count(inp_letter)==0:
                        consonents.remove(inp_letter)
                        vowels.append(inp_letter)
                        #print(consonents,vowels)
                        word_g=''
                        for letter in word_l:
                            for v in vowels:
                                if v==letter:
                                    word_g+=letter
                            for c in consonents:
                                if c==letter:
                                    word_g+=spacing
            print(word_g)
            if word.count(inp_letter)==0:
                wrongs=wrongs+1
            print('Number of wrongs:',wrongs)
            if wrongs==1:
                print(hang)
            if wrongs==2:
                print(hang_head)
            if wrongs==3:
                print(hang_head_body)
            if wrongs==4:
                print(hangmanfinal)
                print('YOU LOSE word:',word)
            
            if word_g==word:
                print('YOU WIN')
                break
            
    
            
            












