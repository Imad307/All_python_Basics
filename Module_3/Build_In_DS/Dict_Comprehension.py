'''
Dictionary comprehension is somewhat similar to lists comprehension. we will be adding new key, value pairs based on existing 
dictionary. However to iterate dictionary, we will use dict.items() operation which turns a dictions into lists of (key,value)tuples 
'''
#Example is as follows:
my_dict = {1: "Imad", 2:"Faizan", 3:"MKM"}
new_dict = {n**3 : new_dic + "!" for (n,new_dic) in my_dict.items()}
print(my_dict)
print(new_dict)