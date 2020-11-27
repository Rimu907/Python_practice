# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:02:12 2020

@author: Caesar GUO-14311495
"""

class Expr:
    pass

class Var(Expr):
    def __init__(self,name):
        self.name = name
    def eval(self,env):
        return env[self.name]
    def __str__(self):
        return self.name
    
class Not(Expr):
    def __init__(self,lep,rep):
       self.l = lep
       self.r = rep
       self.fixity = 0
               
    def eval(self,env):
        return self.op(self.l.eval(env),self.r.eval(env))
        return not self.l.eval(env)    
    def __str__(self):
        if lep.fixity>self.fixity:        
            return "!" + str(self.l)
    
class Or(Expr):
    def __init__(self,l=None,r=None):
       self.l = l
       self.r = r
       self.fixity = 2
    def eval(self,env):
        return self.op(self.l.eval(env),self.r.eval(env))
        return self.l.eval(env) | self.r.eval(env)
    def __str__(self):
        return '('+str(self.l) + "|" + str(self.r)+')'
    
class And(Expr):
    def __init__(self,l=None,r=None):
       self.l = l
       self.r = r 
       self.fixity = 1
    def eval(self,env):
        return self.op(self.l.eval(env),self.r.eval(env))
        return self.l.eval(env) & self.r.eval(env)
    def __str__(self):
        return '('+str(self.l) + "&" + str(self.r)+')'

class Eq(Expr):
    def __init__(self,l=None,r=None):
       self.l = l
       self.r = r 
       self.fixity = 3
    def eval(self,env):
        return self.op(self.l.eval(env),self.r.eval(env))
        return self.l.eval(env) == self.r.eval(env)
    def __str__(self):
        return '('+str(self.l) + "==" + str(self.r)+')'


# =============================================================================
# class make_tt(BinOp): 
#      table=('x','y')
#      eval(table[0],table[1])
# =============================================================================
 

    
    
    
    
    
    
    
    
    
    
    
e1 = Or(Var("x"),Not(Var("x")))
e2 = Eq(Var("x"),Not(Not(Var("x"))))
e3 = Eq(Not(And(Var("x"),Var("y"))),Or(Not(Var("x")),Not(Var("y"))))
e4 = Eq(Not(And(Var("x"),Var("y"))),And(Not(Var("x")),Not(Var("y"))))
e5 = Eq(Eq(Eq(Var("p"),Var("q")),Var("r")),Eq(Var("p"),Eq(Var("q"),Var("r"))))

