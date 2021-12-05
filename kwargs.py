# **kwargs = parameter that will pack all arguments into a dictionary 
#            useful so that a function can accept a varying amonut of keybord argument 

def hello(**kwargs) :  
    #print("hello"+ kwargs['first'] + ""+kwargs['last']) 
     print("Hello",end =" ") 
     for key,value in kwargs.items():  
        print(value,end=" ")


hello(title="Mr.",first="Tolga",middle = "Dude",last="Boroglu")  

