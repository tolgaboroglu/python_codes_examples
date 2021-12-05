#nested functions calls = function calls inside other function calls 
#                         innermost function calls are resolved first 
#                          returned value is used as argument for the next outher function 

#num = input("enter a whole positive number:") 
#num = float(num) 
#num = abs(num)  
#num = round(num)  
#print(num)  

print(round(abs(float(input("Enter a whole positive number:")))))