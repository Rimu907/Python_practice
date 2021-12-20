# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:02:12 2020

@author: Caesar GUO-14311495
"""

class Expr:                                                        #creat abstract class
    pass

class Var(Expr):                                                   #Variables class,subclass of Expr        
    def __init__(self,name):                                       
        self.name = name                                           #Variables initialization,name as parameter
        self.fixity=0                                              #fixity:lowest value with the highest priority.This is for hiding outside brackets 
    def eval(self,env):
        return env[self.name]                                      #method eval, to evaluate  variables  
    def __str__(self):
        return self.name                                           #return Variables as string 
    
class BinOp(Expr):                                                 #abstract class for organizing other classes and sharing codes
    bool_dic={}                                                    #Creat a bool dictionary
    def __init__(self,l=None,r=None):                              #left and right expressions, operations'classes will share this.
        self.l = l
        self.r = r

    def eval(self,env):
        return self.op(self.l.eval(env),self.r.eval(env))          #method eval, to evaluate left subtree and right subtree 
    
    def make_bool(self,i) :
        sign="=!|&()"               
        onlyVar = set(str(self))-set(sign)
        if i == len(onlyVar) :   
            for j in lVar :
                if str(BinOp().bool_dic[j])=='False':
                    print(str(BinOp().bool_dic[j] )+ "    |    ",end="")
                else:
                    print(str(BinOp().bool_dic[j] )+ "     |    ",end="")
            print(self.eval(BinOp().bool_dic))
            return
        BinOp().bool_dic[lVar[i]] = True
        self.make_bool(i+1)
        BinOp().bool_dic[lVar[i]] = False
        self.make_bool(i+1)
        
    def make_bool1(self,i) :
        global result
        sign="=!|&()"               
        onlyVar = set(str(self))-set(sign)
        if i == len(onlyVar) :   
            result +=[self.eval(BinOp().bool_dic)]
            return
        BinOp().bool_dic[list(onlyVar)[i]] = True
        self.make_bool1(i+1)
        BinOp().bool_dic[list(onlyVar)[i]] = False
        self.make_bool1(i+1) 
               
    def make_tt(self):
        global aLst,lAns,lVar
        aLst,lAns,lVar = [],[],[]
        sign="=!|&()"        
        onlyVar = set(str(self))-set(sign)     
        for i in onlyVar:
            lVar += i 
        for i in onlyVar:
            print(i +"        |    ",end="")
        print(str(self)) 
        self.make_bool(0) 
        return (''.join(aLst))
                                 
    
    def isTauto(self):
        global result
        result = []
        self.make_bool1(0)
        for i in result:
            if i==False:
                return False            
        return True
           
#===============================================================#
  
class Not(BinOp):
    def __init__(self,l,r):

        self.fixity=1    
    def eval(self,env):
        return not self.l.eval(env)   
    def __str__(self):
        if self.fixity<self.l.fixity:
            return "!" + "("+str(self.l)+")"
        else:
            return "!" + str(self.l)
        
class Or(BinOp):
    def __init__(self,ex1,ex2):
        self.l=ex1
        self.r=ex2
        self.fixity=3        
    def eval(self,env):
        return self.l.eval(env) | self.r.eval(env)   
    def __str__(self):
        if self.fixity < self.l.fixity and self.fixity < self.r.fixity:        
            return '('+str(self.l)+')' + '|' + '('+str(self.r)+')'
        elif self.fixity < self.l.fixity:
            return '('+str(self.l)+')'+'|'+ str(self.r)
        elif self.fixity < self.r.fixity:
            return str(self.l)+'|'+ '('+str(self.r)+')'
        else:
            return str(self.l)+'|'+ str(self.r)
        
class And(BinOp):
    def __init__(self,ex1,ex2):
        self.l=ex1
        self.r=ex2
        self.fixity=2    
    def eval(self,env):
        return self.l.eval(env) & self.r.eval(env)    
    def __str__(self):
        if self.fixity < self.r.fixity:
            return  str(self.l) + "&" + "("+str(self.r) +")"
        elif self.fixity < self.l.fixity:
            return  "("+str(self.l)+")" + "&" + str(self.r)  
        elif self.fixity < self.l.fixity and self.fixity < self.r.fixity:        
            return '('+str(self.l)+')' + '&' + '('+str(self.r)+')'        
        else:
            return str(self.l) + "&" + str(self.r) 
            
class Eq(BinOp):
    def __init__(self,ex1,ex2):
        self.l=ex1
        self.r=ex2
        self.fixity=4  
    def eval(self,env):
        return self.l.eval(env) == self.r.eval(env)
    def __str__(self):    
        return str(self.l) + "==" + str(self.r)

e1 = Or(Var("x"),Not(Var("x")))
e2 = Eq(Var("x"),Not(Not(Var("x"))))
e3 = Eq(Not(And(Var("x"),Var("y"))),Or(Not(Var("x")),Not(Var("y"))))
e4 = Eq(Not(And(Var("x"),Var("y"))),And(Not(Var("x")),Not(Var("y"))))
e5 = Eq(Eq(Eq(Var("p"),Var("q")),Var("r")),Eq(Var("p"),Eq(Var("q"),Var("r"))))

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
