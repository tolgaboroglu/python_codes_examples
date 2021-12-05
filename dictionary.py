# dictionary = A changeable,unordered collection of unique key: value pairs 
#              fast because they use hashing,allow us to access a value quickly 

capitals = {'USA': 'Washington Dc', 
            'Turkey': 'Ankara', 
            'Russia': 'Moscow'} 

#print(capitals) 
#print(capitals.keys()) -> usa,turkey,russia yı yazdırdı 
#print(capitals.values()) -> başkentler yazıldı 
#print (capitals.items()) -> ikisini ayrı ayrı yazdı 

#for key,value in capitals.items(): 
 #   print(key,value)  

#capitals.update({'Germany':'Berlin'}) -> yeni eklemek için 
#capitals.pop('Russia') -> silmek için  
#capitals.clear() -> tamamını silmek için