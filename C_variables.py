# -*- coding: utf-8 -*-
"""
    @project:cplexpy
    @file:C_variables.py
    @ide:PyCharm
    @time:2018-10-27 23:10
    @author:Sun
"""
import cplex as cpx

cpx.infinity #无穷大变量

c=cpx.Cplex()

v=c.variables   #Methods for adding, querying, and modifying variables.

#the type of variables
t=v.type
t1=t.integer      #I
#print(t1)  #I
#t1=t['I']
#print(t1)  #integer
t2=t.binary       #B
t3=t.continuous   #C   default
t4=t.semi_integer #N
t5=t.semi_continuous #S

#get the num of one type variable
v.get_num() #Returns the number of variables in the problem.
v.get_num_integer() #Returns the number of integer variables in the problem.
v.get_num_binary() #Returns the number of binary variables in the problem.
v.get_num_semicontinuous() #Returns the number of semi-continuous variables in the problem.
v.get_num_semiinteger() #Returns the number of semi-integer variables in the problem.

#Adds variables and related data to the problem.
v.add(obj=None,lb=None,rb=None,types=None,names=None,columns=None)

##*args
#Deletes variables from the problem.
v.delete()
#Sets the lower bound for a variable or set of variables.
v.set_lower_bounds()
#Sets the upper bound for a variable or set of variables.
v.set_upper_bounds()
#Sets the name of a variable or set of variables.
v.set_names()
#Sets the type of a variable or set of variables.
v.set_types()
#Returns the lower bounds on variables from the problem.
v.get_lower_bounds()
#Returns the upper bounds on variables from the problem.
v.get_upper_bounds()
#Returns the names of variables from the problem.
v.get_names()
#Returns the types of variables from the problem.
v.get_types()
#Returns a set of columns of the linear constraint matrix.
v.get_cols()
#Returns a histogram of the columns of the linear constraint matrix.
v.get_histogram()

