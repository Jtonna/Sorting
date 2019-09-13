# TO-DO: complete the helpe function below to merge 2 sorted arrays

# The arrays myst be sorted
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO

    # Keeps track of the array index
    a_index = 0
    b_index = 0

    # for each index in merged array `elements` ...
        # Find the smalles first-item between arrayA and arrayB
        # Add that to `elements` at the given index
        # Increment the a_index/b_index counter

    
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
