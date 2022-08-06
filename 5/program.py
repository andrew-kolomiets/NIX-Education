
list_any=[x for x in range(10)]

def split_function(any_list, number):
    if(len(any_list)<number):
        print('Error, input list with size bigger than number')
    else: 
        k, m = divmod(len(any_list), number)
        return (any_list[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(number))

print(split_function(list_any,2))

# поки не працює треба подумати як реалізувати