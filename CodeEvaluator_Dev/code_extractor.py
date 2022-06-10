# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 10:02:09 2022

@author: MAQ
"""



coder_path = './'
out_file = coder_path + 'printsadded.py'
file = './code_to_test.py'




idx = 1
with open(file, 'r') as f:
    lines = f.readlines() 
    # lines.insert(0, "timeexporter = []\n")
    # lines.insert(0, "import time #REDACTLATERCODER\n")
    # exporter = []
    # for i in lines:
    #     counter = len(i) - len(i.lstrip())
    #     counter_pre = counter
    #     if ('def' or 'with' or 'if' or 'else' or 'for') in i:
    #         counter_pre = 0
    #         counter = 4
            
    #     appender_pre = " " * counter_pre 
    #     appender = " " * counter 
    #     if not i.strip(): 
    #         appender = ""
    #         appender_pre = ""
        
    #     exporter.append(appender_pre + "tic = time.time() #REDACTLATERCODER\n")
    #     exporter.append(i)
    #     exporter.append(appender +"toc = time.time() #REDACTLATERCODER\n")
    #     exporter.append(appender +"print(toc - tic) #REDACTLATERCODER\n")
    #     exporter.append(appender +"timeexporter.append(toc - tic) #REDACTLATERCODER\n")
    
    # with open(out_file, 'w') as ff:
    #     ff.writelines(exporter)
        
    
    with open(coder_path + 'docs.md', 'w') as of:
        print("| Line Number | Code | Time |", file = of)
        print("| --- | --- | --- |", file = of)
        for i in lines:
            i = i.rstrip()
            i = i.lstrip()
            print('| ' +str(idx) + " | " + i + " | ", file = of)
            idx = idx + 1
        