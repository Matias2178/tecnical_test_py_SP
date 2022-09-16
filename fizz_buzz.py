

def fizzbuzz():
    """
    Summary:
        Program that displays the numbres from 1 to 100 on the screen.
        substituting the multiples of 3 for the word "fizz"
        substituting the multiples of 5 for the word "buzz"
        substituting the multiples of 3 and 5 for the word "fizz buzz"
        
    Args:
        none
            
     Returns:
        none
    """
    for i in range(1,101,1):
        if (i%3 == 0) and (i%5 == 0):   #check if i is multiple of 3 and 5
            print("fizzbuzz")
        
        elif (i%3 ==0):                 #check if i is multiple of 3
            print("fizz")
        
        elif (i%5==0):                  #check if i is multiple of 5         
            print("buzz")
            
        else:                           #the munbes isn't a multiple of 3 or 5
            print(i)    

fizzbuzz()