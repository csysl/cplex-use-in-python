# -*- coding: utf-8 -*-
"""
    @project:cplexpy
    @file:lp_by_cplex.py
    @ide:PyCharm
    @time:2018-10-24 18:30
    @author:Sun
    @function:solve LP by cplex
"""

import cplex as cpx

"""
Maximize 
    x1  + 2*x2 + 3*x3
subject to
    –x1 +  x2 + x3 <= 20
    x1 – 3*x2 + x3 <= 30
with these bounds
    0 <= x1 <= 40
    0 <= x2 <= infinity
    0 <= x3 <= infinity
"""
#
c = cpx.Cplex()
# with cp.Cplex() as c:

# 添加变量和目标函数
name = ['x1', 'x2', 'x3']
up = [40, cp.infinity, cp.infinity]
obj = [1.0, 2.0, 3.0]


c.variables.add(names=name, ub=up, obj=obj)
"""
names: 列表，变量名
ub:    列表，上边界
lb:    列表，下边界，默认为0.0
obj:   列表，目标函数的系数
"""

# 设置求目标的最大值
c.objective.set_sense(c.objective.sense.maximize)

# 添加约束
cons = [[[0, 1, 2], [-1, 1, 1]],
        [[0, 1, 2], [1, -3, 1]]]
rhs = [20, 30]
c.linear_constraints.add(lin_expr=cons, rhs=rhs)
"""
lin_expr: 行(约束)表达式，列表（暂时不清楚是不是可以添加目标函数的行）
rhs:      行(约束)的右值，列表
lhs:      行(约束)的左值，列表
name:     行(约束)的名字，列表
"""

# 解决问题
c.solve()

# 输出解的状态
s = c.solution.get_status()
print('Solution status:', s, ':', c.solution.status[s])

# 输出目标函数最大值
v = c.solution.get_objective_value()
print('Solution value: ', v)

# 输出得到的解
vs = c.solution.get_values()
for i in range(3):
    print(vs[i], end=' ')
#
c.end()
