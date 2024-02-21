def merge_sorted_arrays(arr_list):
    merged_elements = []
    for arr in arr_list:
        merged_elements.extend(arr)
    merged_elements.sort()
    return merged_elements

if __name__ == "__main__":
    # Input 
    k = int(input("Number of Sorted Arrays: K = "))
    N = int(input("Enter the size of each array: N = "))
    
  
    sorted_arrays = []
    
    for i in range(k):
        print(f"Enter sorted array elements for array {i + 1}:")
        input_arr = list(map(int, input().split()))
        sorted_arrays.append(input_arr)
    
    merged_array = merge_sorted_arrays(sorted_arrays)
    
    # Merged array in sorted order
    print("Merged and Sorted array Elements:", *merged_array)


    
