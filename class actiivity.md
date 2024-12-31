number=int(input("enter the number "))
start=int(input("enter the starting number"))
end=int(input("enter the ending number"))
if end>start:
    print ("the asecending order")
    for i in range(start,end+1):
      print(f" {number} * {i} = {number*i}")
      
else :
    print ("the descing order " )
    for i in range (start,end-1,-1):
        print(f"{number} * {i} = {number*i}")
    
