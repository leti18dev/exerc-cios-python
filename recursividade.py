def recursiva(n):
    if n <= 0:
        return 0
    elif n == 1:
        
        return 1
    else:
        return recursiva(n - 1) + recursiva(n - 2) 
        
        
        
  