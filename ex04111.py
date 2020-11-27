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
        self.fixity=0
    def eval(self,env):
        return env[self.name]
    def __str__(self):
        return self.name
    
class BinOp(Expr):
    bool_dic={}
    def __init__(self,l=None,r=None):
        self.l = l
        self.r = r
    def eval(self,env):
        return self.op(self.l.eval(env),self.r.eval(env))
    
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
        for i in aLst :
            for j in range(len(aLst)) :
                for k in onlyVar:
                    lAns = lAns + [aLst[j][k]]
                lAns = lAns + [self.eval(i)]
        return lAns    
    
    def make_bool(self,i) :
        sign="=!|&()"               
        onlyVar = set(str(self))-set(sign)
        #global Lst_All_Dic
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
        return
           
    def isTauto(self):
        if self.lAns == 'True':
            return True
        
#=============================================================================  
class Not(BinOp):
    def __init__(self,ex1=None,ex2=None):
        self.l=ex1
        self.r=ex2
        self.fixity=1    
    def eval(self,env):
        return not self.l.eval(env)   
    def __str__(self):       
            return "!" + str(self.l)
   
class Or(BinOp):
    def __init__(self,ex1,ex2):
        self.l=ex1
        self.r=ex2
        self.fixity=3        
    def eval(self,env):
        return self.l.eval(env) | self.r.eval(env)   
    def __str__(self):
        if (self.fixity)<(self.l.fixity) and (self.fixity)<(self.r.fixity):        
            return '('+str(self.l)+')' + '|' + '('+str(self.r)+')'
        elif (self.fixity)<(self.l.fixity):
            return '('+str(self.l)+')'+'|'+ str(self.r)
        elif (self.fixity)<(self.r.fixity):
            return str(self.l)+'|'+ '('+str(self.r)+')'
# =============================================================================
#         elif (self.fixity)==(self.l.fixity) and (self.fixity)==(self.r.fixity):
#             return str(self.l)+'|'+ str(self.r)
# =============================================================================
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
            return str(self.l)+ '&' + str(self.r)
     
        
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
