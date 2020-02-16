nums=[int(i) for i in input("Enter two prime numbers").split()]
num1=nums[0]
num2=nums[1]
N=num1*num2
phi=(num1-1)*(num2-1)
e=






def __gcd(a, b): 
  
    # Everything divides 0  
    if (a == 0 or b == 0): return 0
      
    # base case 
    if (a == b): return a 
      
    # a is greater 
    if (a > b):  
        return __gcd(a - b, b) 
              
    return __gcd(a, b - a) 


def coprime(a, b): 
      
    if ( __gcd(a, b) == 1): 
        print("Co-Prime") 
    else: 
        print("Not Co-Prime")      
  
# Driver code 
a = 5; b = 6
coprime(a, b)  
  
a = 8; b = 16
coprime(a, b) 