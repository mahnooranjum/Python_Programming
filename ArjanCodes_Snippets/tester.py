# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 04:41:23 2023

@author: MAQ
"""


keypairs = [[('t1', 't2'), ('t1_t2_1', 't2_t1_1')], 
            [('t1', 't2'), ('t1_t2_2', 't2_t1_2')], 
            [('t1', 't2'), ('t1_t2_3', 't2_t1_3')], 
            [('t1', 't3'), ('t1_t3_1', 't3_t1_1')], 
            [('t1', 't3'), ('t1_t3_2', 't3_t1_2')], 
            [('t2', 't3'), ('t2_t3_1', 't3_t2_1')], 
            [('t3', 't2'), ('t2_t3_2', 't3_t2_2')], ]

keypairs_sorted = []
for i in keypairs: 
    
    if i[0][0] < i[0][1]:
        keypairs_sorted.append(i)
    else:
        i_0 = (i[0][1],i[0][0])
        i_1 = (i[1][1],i[1][0])
        keypairs_sorted.append([i_0, i_1])
        
keypairs = keypairs_sorted


def split_composites_pairs(keypairs):

    p_traversed = []
    comp_list = []
    
    for tup in keypairs:
        a, b = tup
        check = 0
        inner_list = []
        inner_list.append(b)
        for tup2 in keypairs:
            c, d = tup2
            if (((a[0] == c[0]) and (a[1] == c[1])) and ((b[0] != d[0]) or (b[1] != d[1]))):

                check += 1
                already_bool = False
                for tup3 in comp_list:
                    e = tup3[0]

                    if a == e:
                        already_bool = True
                if already_bool ==  False:

                    inner_list.append(d)

        if check == 0:
            p_traversed.append(tup)
        elif len(inner_list) > 1:
            comp_list.append([a, inner_list])
    
    return p_traversed, comp_list


