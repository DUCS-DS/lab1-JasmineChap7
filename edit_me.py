def find_max(inputArray):
    max_value = inputArray[0]  
    for i in range(1, len(inputArray)):  
        if inputArray[i] > max_value:  
            max_value = inputArray[i] 
    return max_value  #return the maximum

test_list = [2112*i % 2024 for i in range(10000)]

print(find_max(test_list))