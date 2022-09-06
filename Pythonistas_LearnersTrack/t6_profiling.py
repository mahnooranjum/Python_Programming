def reverseStr(str1):
  return str1[::-1]

def fib(n):
    if n <= 2:
        return 1
    else: 
        return fib(n-1) + fib(n-2)
    

def toprofile():
    str1 = "helloworldadssafdsgdsfgsdgretgegesrgerg"
    reverseStr(str1)
    fib(30)
    return 0

def main():
    import cProfile
    import pstats

    with cProfile.Profile() as pr:
        toprofile()

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    # stats.print_stats()
    stats.dump_stats(filename="./profiler.prof")


if __name__ == '__main__':
    main()
