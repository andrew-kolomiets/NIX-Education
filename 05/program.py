


list_any=[x for x in range(100)]

def split_function(any_list, number):
    if(len(any_list)<number):
        print('Error, input list with size bigger than number')
    else: 
        k, m = divmod(len(any_list), number)
        l=[]
        for i in range(0,len(any_list),k):
            if(i+k<len(any_list)):
                l.append(any_list[i:i+k])
            else:
                l.append(any_list[i:len(any_list)])

        return l
    
print(split_function(list_any,10))

