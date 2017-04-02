#!/usr/bin/env python  
# coding=utf-8

# 读入数据
n, m = map(int, raw_input().split(' '))
row_data_list = map(int, raw_input().split(' '))

# 数据预处理
clear_data_list = []
for row_temp_i in row_data_list:
    row_temp_list = row_temp_i.lower().split(' ')
    row_temp_set = set(row_temp_list)
    clear_data_list.append(row_temp_set)

# 数据做交集并输出
for m_i in xrange(n, n + m):
    final_find_set = ()
    final_find_i = -2
    for n_i in xrange(0, n):
        temp_find_set = clear_data_list[n_i] & clear_data_list[m_i]
        if len(temp_find_set) > len(final_find_set):
            final_find_set = temp_find_set
            final_find_i = n_i
    print row_data_list[final_find_i]

# 测试数据
# n, m = 6, 3
# row_data_list = ['An algorithm is an effective method that can be expressed within a finite amount of space and time',
# 'Starting from an initial state and initial input the instructions describe a computation',
# 'That when executed proceeds through a finite number of successive states',
# 'Eventually producing output and terminating at a final ending state',
# 'The transition from one state to the next is not necessarily deterministic',
# 'Some algorithms known as randomized algorithms incorporate random input',
# 'Next to the transition','Wormhole infinite time and space',
# 'The transition from one state to the next is not necessarily deterministic']