def function_hello(tuples:tuple):
    
    if(tuples[1]=='ru'):
        return 'Привет,'+' '+tuples[0]+'!'
    elif(tuples[1]=='us'):
        return 'Hello,'+' '+tuples[0]+'!'
    elif(tuples[1]=='es'):
        return 'Hola,'+' '+tuples[0]+'!'
    else:
        return 'Hello,'+' '+tuples[0]+', but I do not know where are you from!'
        

users_list = [
    ('Александр', 'ru'),
    ('James', 'us'),
    ('Daniella', 'es'),
    ('Someone', 'unknown country'),
]



any_list=list(map(function_hello, users_list))

for i in any_list:
    print(i)