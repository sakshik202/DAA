def remove_duplicates_custom(input_array):
    if len(input_array) == 0 or len(input_array) == 1:
        return input_array
    
    
    unique_value = 0
    
    
    for i in range(1, len(input_array)):
        if input_array[i] != input_array[unique_value]:
            unique_value += 1
            input_array[unique_value] = input_array[i]
    
   
    return input_array[:unique_value + 1]

if __name__ == "__main__":
    # Input 
    array_size = int(input("size of the array elements: "))
    
    
    input_arr = []
    print("Enter the elements to remove duplicates from sorted array:")
    input_string = input().split() 1
    for num in input_string:
        input_arr.append(int(num))
        
    original_arr = input_arr.copy()
    output_arr = remove_duplicates_custom(input_arr)
    
    
    print("Original Array :", original_arr)
    print("Output Array :", output_arr)
