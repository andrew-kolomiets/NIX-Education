
temp=1

any_list=[x for x in range(700,800)]

print(any_list)

for i in any_list:
    
    if(i==777 and (i in any_list)):
        print("Number 777 is find.")
        break
    elif(temp==100):
        print("Error!")
        break
     
    temp+=1

    