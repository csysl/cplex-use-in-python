# -*- coding: utf-8 -*-
"""
    @project:cplexpy
    @file:C_linear_constraints.py
    @ide:PyCharm
    @time:2018-10-28 10:53
    @author:Sun
"""
import cplex as cpx

c=cpx.Cplex()

lc=c.linear_constraints   #Methods for adding, modifying, and querying linear constraints.

#Adds linear constraints to the problem.
lc.add(lin_expr=None,senses='',rhs=None,range_values=None,names=None)


