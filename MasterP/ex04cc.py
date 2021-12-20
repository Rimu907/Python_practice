# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 12:19:20 2020

@author: Chao Cui
"""

# superclass for all boolean expressions
class Expr :
    Dic = {}
    def make_tt(self):
        global Lst_All_Dic,Answer,Lst_Var
        Lst_Var = []
        Answer = []
        Lst_All_Dic = []
        Var_Expr = set(str(self))-set("()!&|=") # Filter the matches of expressions to obtain the names of expression variables       
        for i in Var_Expr :
            Lst_Var += i 
        for i in Var_Expr :
            print(i+"     | ",end="")
        print(str(self))
        self.Bool_Recursive(0)
        for i in Lst_All_Dic :
            for j in range(len(Lst_All_Dic)) :
                for k in Var_Expr :
                    Answer = Answer + [Lst_All_Dic[j][k]]
                Answer = Answer + [self.eval(i)]
        return Answer
    
    def Bool_Recursive(self,i) :
        Var_Expr = set(str(self))-set("()!&|=")
        global Lst_All_Dic
        if i == len(Var_Expr) :
            Lst_All_Dic = Lst_All_Dic + [Expr().Dic.copy()]  
            return 
        Expr().Dic[Lst_Var[i]] = True
        self.Bool_Recursive(i+1)
        Expr().Dic[Lst_Var[i]] = False
        self.Bool_Recursive(i+1)
        
    def isTauto(self) :
        # if self.eval(self.env) == True :
        #     return True
        # else :
        #     return False
        pass
        
class BinOp(Expr) : # abstract class
    def __init__(self,left,right) :
        self.left = left
        self.right = right
        
    def __str__(self) :
        return str(self.op(self.left,self.right))
        
# op(boolean,boolean) : boolean
    def eval(self,env) :
        return self.op(self.left.eval(env),self.right.eval(env))
    
    def add_brackets(self) :
        if (str(type(self.left)) == "<class '__main__.Var'>") and (str(type(self.right)) == "<class '__main__.Var'>") :
            return True
        else :
            return False
    

# represents logical variables
class Var(Expr):
    def __init__(self,value) :
        self.value = value

    def __str__(self) : 
        return self.value   
    
    def eval(self,env) :
        return env[self.value]
           
# represents logical negation
class Not(Var) :
    def op (self,x) :
        return (not x)
    
    def __str__(self) :
        return f"!{self.value}"
    
    def eval(self,env) :
        return self.op(self.value.eval(env))
      
# represents logical and
class And(BinOp) :
    def op(self,x,y) :
        return (x and y)
        
    def __str__(self) :
        if self.add_brackets() :
            return f"({self.left}&{self.right})"
        else :
            return f"{self.left}&{self.right}"

# represents logical or
class Or(BinOp) :
    def op(self,x,y) :
        return (x or y)
    
    def __str__(self) : 
        if self.add_brackets() :
            return f"({self.left}|{self.right})"
        else :
            return f"{self.left}|{self.right}"
      
# represents logical equivalence
class Eq(BinOp) :
    def op(self,x,y) :
        return (x == y)
        
    def __str__(self) : 
        if self.add_brackets() :
            return f"({self.left}=={self.right})"
        else :
            return f"{self.left}=={self.right}"

e1 = Or(Var("x"),Not(Var("x")))
e2 = Eq(Var("x"),Not(Not(Var("x"))))
e3 = Eq(Not(And(Var("x"),Var("y"))),Or(Not(Var("x")),Not(Var("y"))))
e4 = Eq(Not(And(Var("x"),Var("y"))),And(Not(Var("x")),Not(Var("y"))))
e5 = Eq(Eq(Eq(Var("p"),Var("q")),Var("r")),Eq(Var("p"),Eq(Var("q"),Var("r"))))
print("\n")
###############################################################################
print(e1)
print(e2)
print(e3)
print(e4)
print(e5)
print("\n")
###############################################################################
print(And(Not(Var("p")),Var("q")))
print(Not(And(Var("p"),Var("q"))))
print(Or(And(Var("p"),Var("q")),Var("r")))
print(And(Var("p"),Or(Var("q"),Var("r"))))
print(Eq(Or(Var("p"),Var("q")),Var("r")))
print(Or(Var("p"),Eq(Var("q"),Var("r"))))
print("\n")
###############################################################################
print (e2.eval({"x" : True}))
print (e3.eval({"x" : True, "y" : True}))
print (e4.eval({"x" : False, "y" : True}))
print("\n")
###############################################################################
print(e1.make_tt())
print(e2.make_tt())
print(e3.make_tt())
print(e4.make_tt())
print(e5.make_tt())
###############################################################################
print (And(Var("x"),And(Var("y"),Var("z"))))
print (And(And(Var("x"),Var("y")),Var("z")))
print("\n")
###############################################################################
# print (e1.isTauto())
# print (e2.isTauto())
# print (e3.isTauto())
# print (e4.isTauto())
# print (e5.isTauto())
"""
x|!x
x==!!x
!(x&y)==!x|!y
!(x&y)==!x&!y
p==q==r==p==q==r

!p&q
!(p&q)
p&q|r
p&(q|r)
p|q==r
p|(q==r)

True
True
False
x       | x|!x
True    | True
False   | True

x       | x==!!x
True    | True
False   | True

y       | x     | !(x&y)==!x|!y
True    | True  | True
False   | True  | True
True    | False | True
False   | False | True

y       | x     | !(x&y)==!x&!y
True    | True  | True
False   | True  | False
True    | False | False
False   | False | True

p       | q     | r     | p==q==r==p==q==r
True    | True  | True  | True
False   | True  | True  | True
True    | False | True  | True
False   | False | True  | True
True    | True  | False | True
False   | True  | False | True
True    | False | False | True
False   | False | False | True

x&y&z
x&y&z
True
True
True
False
True
"""