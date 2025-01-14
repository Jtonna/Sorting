# TO-DO: complete the helpe function below to merge 2 sorted arrays

arr = [62, 35, 43, 37, 82, 96, 22, 63, 49, 2, 1, 4, 7, 8, 12, 15]

# The arrays myst be sorted
def merge( arrA, arrB ):
    num_elements = len( arrA ) + len( arrB )
    merged_arr = [0] * num_elements
    # TO-DO

    # Keeps track of the array index
    a_index = 0
    b_index = 0

    for i in range(num_elements):
    # for each index in merged array `elements` ...

        # Find the smallest first-item between arrayA and arrayB
        # Add that to `elements` at the given index
        # Increment the a_index/b_index counter
        if a_index >= len(arrA):
            # 1. A is empty, B is not
            merged_arr[i] = arrB[b_index]
            b_index += 1

        elif b_index >= len(arrB):
            # 2. B is empty, A is not
            merged_arr[i] = arrA[a_index]
            a_index += 1

        elif arrA[a_index] < arrB[b_index]:
            # 3. A has the smaller element
            merged_arr[i] = arrA[a_index]
            a_index += 1

        else: # arrA[a_index] > arrB[b_index]:
            # 4. B has the smaller element
            merged_arr[i] = arrB[b_index]
            b_index += 1

        pass
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

    if len(arr) > 1:
        # Split into left and right arrays (lists)
        midway_point = len(arr) // 2 # This divides and returns an int, it will never return a float. 
        left_array = arr[ : midway_point ]
        right_array = arr[ midway_point : ]

        # Sort each of the split arrays
        sorted_left = merge_sort(left_array)
        sorted_right = merge_sort(right_array)

        # Merge the sorted arrays into one
        arr = merge(sorted_left, sorted_right)


    return arr
    
merge_sort(arr)
