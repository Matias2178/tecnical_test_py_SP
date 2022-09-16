def fibonacci(number: int()):
    """
    Summary:
        Program that solves for any number in the fibonacci series
        fibonacci series:  0,1,1,2,3,5,8,13,21..
        f(0) = 0
        f(1) = 1
        f(n) = f(n-1) + f(n-2) 

    Args:
        number (int): number to calculate fibonacci series

    Returns:
        (int): fibonacci number of n
    """
    prev_value = 0
    act_value = 1
    aux = 0
    
    if type(number)!= int:  #check the input type of the variable entred
        print("wrong variable type")
        return

    if number < 0:          #check if numbes is negative 
        print("wrong number input!! is a negative number \n changing to positive")
        number = abs(number)
  
    
    if number == 0:         #check if value is 0
        return 0
    
    for i in range(1,number,1): #calculate fibonacci number
        aux = prev_value + act_value
        prev_value = act_value
        act_value = aux
        
    return act_value

def control(n, result):
    if fibonacci(n) == result:
        print("Fibonacci series of ",n, "is: ", result)
    else:
        print("something is wrong!!")

