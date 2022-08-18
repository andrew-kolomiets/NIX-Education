def fun_gen(start,end):
    for i in range(start,end+1):
        yield(i)

for i in fun_gen(1,5):
    print(i)
