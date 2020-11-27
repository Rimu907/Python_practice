# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:02:12 2020

@author: Caesar GUO-14311495
"""

class Expr:                                                                    #abstract class
    pass

class Var(Expr):                                                               #Variables class,subclass of Expr        
    def __init__(self,name):                                       
        self.name = name                                                       #Variables initialization,name as parameter
        self.fixity=0                                                          #fixity:lowest value with the highest priority.This is for hiding outside brackets 
    def eval(self,env):
        return env[self.name]                                                  #method eval, to evaluate a variable  
    def __str__(self):
        return self.name                                                       #return Variables as string 
    
class BinOp(Expr):                                                             #abstract class for organizing other classes and sharing codes
    bool_dic={}                                                                #Creat a bool dictionary
    def __init__(self,l=None,r=None):                                          #left and right expressions, operations'classes will share this.
        self.l = l                                                             #r=None because Not operation does not need the second parameter
        self.r = r

    def make_bool(self,i) :                                                    #Generate bool values
        sign="=!|&()"               
        onlyVar = set(str(self))-set(sign)                                     #set minus, only variables in in this list
        if i == len(onlyVar) :                                     
            for j in lVar :                                                    #j are the Variables
                if str(BinOp().bool_dic[j])=='False':                          #if False, One space less printing in output, make output orderliness
                    print(str(BinOp().bool_dic[j] )+ "    |    ",end="")
                else:
                    print(str(BinOp().bool_dic[j] )+ "     |    ",end="")      #print the bool Values based on the number of Variables in onlyVar
            print(self.eval(BinOp().bool_dic))
            return
        BinOp().bool_dic[lVar[i]] = True                                       #Recursion to generate bool values, True, i+1, False, i+1, True
        self.make_bool(i+1)
        BinOp().bool_dic[lVar[i]] = False
        self.make_bool(i+1)
        
    def make_bool1(self,i) :                                                   #make_bool1 is same with make_bool, but without print the list
        global result                                                          #make_bool1 is built for Function isTauto()
        sign="=!|&()"               
        onlyVar = set(str(self))-set(sign)
        if i == len(onlyVar) :   
            result +=[self.eval(BinOp().bool_dic)]                             #Store the result bool values in list
            return
        BinOp().bool_dic[list(onlyVar)[i]] = True
        self.make_bool1(i+1)
        BinOp().bool_dic[list(onlyVar)[i]] = False
        self.make_bool1(i+1) 
               
    def make_tt(self):                                                         #make truthtable fuction
        global aLst,lVar
        aLst,lVar = [],[]
        sign="=!|&()"        
        onlyVar = set(str(self))-set(sign)                                     #set minus, only variables in in this list
        for i in onlyVar:
            lVar += i                                                          #lVar stores variables        
            print(i +"        |    ",end="")                                   #print the Variables as list headings
        print(str(self)) 
        self.make_bool(0)                                                      #start from 0, in make_bool i = the number of variables 
        return (''.join(aLst))                                                 #join is to hide list symbol[]
                                     
    def isTauto(self):                                                         
        global result
        result = []
        self.make_bool1(0)                                                     #call make_bool1, to get the result bool values in List result[]
        for i in result: 
            if i==False:
                return False                                                   #if any False in the result bool list, the expression is not tauto
        return True
           
#===============================================================#
  
class Not(BinOp):                                                              #Not operation, fixty = 1, priority higher than And
    def __init__(self,ex1=None,ex2=None):
        self.l=ex1
        self.r=ex2
        self.fixity=1    
    def eval(self,env):
        return not self.l.eval(env)                                            # ! expression
    def __str__(self):
        if self.fixity<self.l.fixity:                                          #if expression's priority lower than Not, add brackets to the expression
            return "!" + "("+str(self.l)+")"
        else:
            return "!" + str(self.l)                                           #expression display 
        
class Or(BinOp):
    def __init__(self,ex1,ex2):                                                #Or operation                     
        self.l=ex1
        self.r=ex2
        self.fixity=3                                                          #fixty = 3, priority higher than equal
    def eval(self,env):
        return self.l.eval(env) | self.r.eval(env)   
    def __str__(self):
        if self.fixity < self.l.fixity and self.fixity < self.r.fixity:        #if expressions' priority lower than Or, add brackets to the expressions
            return '('+str(self.l)+')' + '|' + '('+str(self.r)+')'
        elif self.fixity < self.l.fixity:
            return '('+str(self.l)+')'+'|'+ str(self.r)
        elif self.fixity < self.r.fixity:
            return str(self.l)+'|'+ '('+str(self.r)+')'
        else:
            return str(self.l)+'|'+ str(self.r)                                #expression display
        
class And(BinOp):                                                              #And operation, fixty = 2, priority higher than Or, lower than Not
    def __init__(self,ex1,ex2):
        self.l=ex1
        self.r=ex2
        self.fixity=2    
    def eval(self,env):
        return self.l.eval(env) & self.r.eval(env)    
    def __str__(self):                                                         #Same, if expressions' priority lower than and, add brackets to the expressions                          
        if self.fixity < self.r.fixity:
            return  str(self.l) + "&" + "("+str(self.r) +")"
        elif self.fixity < self.l.fixity:
            return  "("+str(self.l)+")" + "&" + str(self.r)  
        elif self.fixity < self.l.fixity and self.fixity < self.r.fixity:        
            return '('+str(self.l)+')' + '&' + '('+str(self.r)+')'        
        else:
            return str(self.l) + "&" + str(self.r)                             #expression display
            
class Eq(BinOp):                                                               #Equal operation, lowest priority
    def __init__(self,ex1,ex2):
        self.l=ex1
        self.r=ex2
        self.fixity=4  
    def eval(self,env):
        return self.l.eval(env) == self.r.eval(env)
    def __str__(self):    
        return str(self.l) + "==" + str(self.r)                                #expression display

e1 = Or(Var("x"),Not(Var("x")))
e2 = Eq(Var("x"),Not(Not(Var("x"))))
e3 = Eq(Not(And(Var("x"),Var("y"))),Or(Not(Var("x")),Not(Var("y"))))
e4 = Eq(Not(And(Var("x"),Var("y"))),And(Not(Var("x")),Not(Var("y"))))
e5 = Eq(Eq(Eq(Var("p"),Var("q")),Var("r")),Eq(Var("p"),Eq(Var("q"),Var("r"))))
e6 = (Not(Not(Var("x"),Var("y")),Var("z")))
print(e1)
print(e2)
print(e3)
print(e4)
print(e5)

print(And(Not(Var("p")),Var("q")))
print(Not(And(Var("p"),Var("q"))))
print(Or(And(Var("p"),Var("q")),Var("r")))
print(And(Var("p"),Or(Var("q"),Var("r"))))
print(Eq(Or(Var("p"),Var("q")),Var("r")))
print(Or(Var("p"),Eq(Var("q"),Var("r"))))

print (e2.eval({"x" : True}))
print (e3.eval({"x" : True, "y" : True}))
print (e4.eval({"x" : False, "y" : True}))

print(e1.make_tt())
print(e2.make_tt())
print(e3.make_tt())
print(e4.make_tt())
print(e5.make_tt())

print (And(Var("x"),And(Var("y"),Var("z"))))
print (And(And(Var("x"),Var("y")),Var("z")))

print (e1.isTauto())
print (e2.isTauto())
print (e3.isTauto())
print (e4.isTauto())
print (e5.isTauto())
