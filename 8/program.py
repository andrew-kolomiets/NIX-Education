
any_list=[44,52,523,62,2,7,23,5,8,3,8,74,234,8734,32,743,4234,654,2542,3434,5,643,64,643,23477,234777,3423452,34523,2,354,23,7,3442,2345,625346,22,5,746,2,52,4,35,346]

temp=1

for i in any_list:
    
    if(i==777):
        print("Number 777 is find.")
        break
        
    temp+=1
    
    if(temp==100 or temp==len(any_list)):
        print("Error!")
        break

    