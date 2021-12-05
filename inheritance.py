class Animal: 

    alive = True 


    def eat(self): 
        print("This animal is eating") 
    
    def slumber(self): 
        print("This animal is sleeping") 
    

class Rabbit(Animal) :  
    
    def run(self):  
        print("The Rabbit is running")

class Fish(Animal): 
     
    def swim(self): 
        print("This fish is swiming")

class Hawk(Animal): 
    
    def fly(self): 
        print("This hawk is flying") 


rabbit = Rabbit() 
fish   = Fish() 
hawk   =  Hawk() 

rabbit.run() 
fish.swim() 
hawk.fly()