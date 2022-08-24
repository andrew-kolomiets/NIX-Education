
#----------------------------------------------------------------------------

import os 


def delete_files_func(path, file_extension):
    
    dir_list = os.listdir(path) 
    
    list_deliting=[x for x in dir_list if file_extension in x]
    
    for file in list_deliting:
        os.remove("12/test/"+str(file))
        
    return list_deliting

print("In directory delite files: \n",delete_files_func(path='12/test/', file_extension='.wew'))
    
    
#----------------------------------------------------------------------------







# directory = "test"
# parent_dir ="12/"

# path = os.path.join(parent_dir, directory)

# #-------------------------------------------
# dir_list = os.listdir(path) 

# for file in dir_list:
#     os.remove("12/test/"+str(file))
    
# for i in range(1,5):
#     os.remove("12/test/newfile"+str(i)+".rrt")
    
# os.rmdir(path) 

# os.mkdir(path)

# for i in range(1,5):
#     os.mknod("12/test/newfile"+str(i)+".txt")

# for i in range(1,5):
#     os.mknod("12/test/newfile"+str(i)+".rrt")
#-------------------------------------------

# def delete_files_func(path='/path/to/folder', file_extension='.txt'):

# dir_list = os.listdir(path) 

# print(dir_list)
    