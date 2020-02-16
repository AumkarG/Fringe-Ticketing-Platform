nums=[int(i) for i in input("Enter two prime numbers").split()]
num1=nums[0]
num2=nums[1]
N=num1*num2
phi=(num1-1)*(num2-1)
e=1
for i in range(2,phi):
    if coprime(i,phi) and comprime(i,N):
        e=i
        break
print(e)






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
        return True
    else: 
        return False      
  
