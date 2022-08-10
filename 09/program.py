
list_1=[1, 2, 3, 4, 5]
list_2 = [1, 3, 4]

def filtration(x_list,y_list):
    for i in y_list:
        if (i in x_list):
            x_list.remove(i)
        else:
            continue
            
    return x_list

print(filtration(list_1,list_2))