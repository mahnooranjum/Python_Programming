| Line Number | Code | Time |
| --- | --- | --- |
| 1 | # -*- coding: utf-8 -*- | 
| 2 | """ | 
| 3 | Created on Fri Jun 10 10:02:09 2022 | 
| 4 |  | 
| 5 | @author: MAQ | 
| 6 | """ | 
| 7 |  | 
| 8 | import concurrent.futures | 
| 9 | import time | 
| 10 |  | 
| 11 | start = time.perf_counter() | 
| 12 |  | 
| 13 |  | 
| 14 | def do_something(seconds): | 
| 15 | print(f'Sleeping {seconds} second(s)...') | 
| 16 | time.sleep(seconds) | 
| 17 | return f'Done Sleeping...{seconds}' | 
| 18 |  | 
| 19 |  | 
| 20 | with concurrent.futures.ProcessPoolExecutor() as executor: | 
| 21 | secs = [5, 4, 3, 2, 1] | 
| 22 | results = executor.map(do_something, secs) | 
| 23 |  | 
| 24 | # for result in results: | 
| 25 | #     print(result) | 
| 26 |  | 
| 27 | finish = time.perf_counter() | 
| 28 |  | 
| 29 | print(f'Finished in {round(finish-start, 2)} second(s)') | 
