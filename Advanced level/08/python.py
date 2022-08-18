any_list=[]

with open("file.txt",'r') as file:
    any_list=[i for i in file.readlines() if 'catch me' in i ]
    print('Result list: ',any_list, ' with lenth: ', len(any_list))
    
    
