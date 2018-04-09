def factcal(n): # Create the factorial of a positive integer    
    fact = 1
    while n>0:
          fact *= n
          n=n-1
          if(n<=1):
            break
    else: # Display the message if n is not a positive integer.        
          print('Input a correct number....') 
          return
    return fact

def factdata(n): # return the numbers of factorial x
    result = []
    while n>0:
       result.append(n)
       n = n - 1
       if(n==0):
        break
    else: # Display the message if n is not a positive integer.        
       print('Input a correct number....') 
       return
    return result
