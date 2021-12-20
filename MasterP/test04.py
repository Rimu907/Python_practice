#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 18:09:12 2020

@author: txa
"""

"test data"

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
