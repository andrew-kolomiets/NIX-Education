# Напишите функцию, которая делает return
# строки приветствия людей из разных стран на разных языках
# , в зависимости от страны человека.
# Вызовите функцию используя map
# Требование: используйте map
# Для примера можете взять этот список юзеров:
# users_list = [
#     ('Александр', 'ru'),
#     ('James', 'us'),
#     ('Daniella', 'es'),
#     ('Someone', 'unknown country'),
# ]
# На выходе с использованием users_list, после использования map вы должны получить результат iterable с такими приветствиями:
# Привет, Александр!
# Hello, James!
# Hola, Daniella!
# Hello, Someone, but I do not know where are you from!

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