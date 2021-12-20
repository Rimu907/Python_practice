# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 17:25:18 2020

@author: 90730
"""
import pickle

class trees:
    pass

class questions(trees):
    def __init__(self,text,ifyes,ifno):
        self.text=text
        self.ifyes=ifyes
        self.ifno=ifno
    def play(self):
        if ask(self.text):
            self.ifyes=self.ifyes.play()
        else:
            self.ifno=self.ifno.play()
        return self

class answer(questions):
    def __init__(self,name):
        self.name = name
    def play(self):
        if ask(f'Is it a {self.name}? '):
            print('great!')
            return self
        else:
            newanimal = input("What motorcycle were you thinking about? ")
            newquestion = input(f"What would be a question to differentiate "+\
                                f"between {self.name} and {newanimal}? ")
            if ask(f"The answer for {newanimal} would be? "):
                return questions(newquestion,answer(newanimal),self)
            else :
                return questions(newquestion,self,answer(newanimal))
def ask(q):
    while True:
        ans=input(q+'')
        if ans == 'yes':
            return True
        if ans == 'no' :
            return False
        else:
            print('please yes or no only')
try :
    # try to load the fuile, if it is not there we initialize the kb.
    file = open("animal.kb", "rb") # read binary
    kb = pickle.load(file)
    file.close()
except FileNotFoundError:
    kb = questions('is it motocycle? ',
                  questions('is it red? ',
                           answer('Ducati'),
                           answer('Honda')),
                  answer('kawsaki'))

while True:
    if ask('wanna play? '):
        kb=kb.play()
    else:
        break
    
file = open("animal.kb", "wb") # write binary
pickle.dump(kb,file)
file.close()              
        