# -*- coding: utf-8 -*-
"""
    @project:cplexpy
    @file:C_objective.py
    @ide:PyCharm
    @time:2018-10-28 00:00
    @author:Sun
"""
import cplex as cpx

c=cpx.Cplex()

##Constants defining the sense of the objective function.
s=c.objective.sense.maximize #-1
#print(s)  #-1
#s=c.objective.sense[-1]
#print(s)  #maximize
s=c.objective.sense.minimize #1
#print(s)  #1
#s=c.objective.sense[1]
#print(s)  #minimize

obj=c.objective  #Contains methods for querying and modifying the objective function.

obj.set_sense(s) #Sets the sense of the objective function.
obj.get_sense()
obj.set_name('str') #Sets the name of the objective function.
obj.get_name()
##*args
obj.set_linear(*args) #Changes the coefficient of the linear part of the objective function.
obj.get_linear(*args)
#quadratic
obj.set_quadratic(*args)
obj.get_quadratic(*args)
obj.set_quadratic_coefficients(*args)
obj.get_quadratic_coefficients(*args)
obj.get_num_quadratic_variables()
obj.get_num_quadratic_nonzeros()

obj.set_offset(num) #Sets the constant offset of the objective function for a problem.
obj.get_offset()    #Gets the constant offset of the objective function for a problem.


