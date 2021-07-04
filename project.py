#generate hashing using md5
import hashlib    
def hashing_string(string1):
    result=hashlib.md5(string1.encode())
    print(result)
    
s=input("Enter any string : ")
hashing_string(s)
   
#create hashing 3 different algorithms
def hashing_string1(string2):
    result1=hashlib.md5(string2.encode())
    print(result1)
    result2=hashlib.sha224(string2.encode())
    print(result2)
    result3=hashlib.sha1(string2.encode())
    print(result3)
    
s1=input("Enter any string : ")
hashing_string1(s1)

  
#salting and iteration in hashing
def hashing_string2(string3):
    salt="a123b"
    for i in range(6):
        result=hashlib.md5((salt+string3).encode())
    print(result)    
    
s2=input("Enter any string : ")
hashing_string2(s2)

