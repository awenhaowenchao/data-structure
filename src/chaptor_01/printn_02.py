
"""
RecursionError: maximum recursion depth exceeded while calling a Python object
maximum recursion depth should not more than 1000, because recurision use more space of memory
"""
def printn(n:int):
    print(n)
    if n==0:
        return
    else:
        printn(n - 1)

printn(1000)