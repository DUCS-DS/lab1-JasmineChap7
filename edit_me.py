def FindMax(inputArray):
    max_value = inputArray[0]  
    for i in range(1, len(inputArray)):  
        if inputArray[i] > max_value:  
            max_value = inputArray[i] 
    return max_value  #return the maximum
