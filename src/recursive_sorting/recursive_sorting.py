# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

    if len(arr) > 1:
        # Split into left and right arrays (lists)
        midway_point = len(arr) // 2 # This divides and returns an int, it will never return a float. 
        left_array = arr[ : midway_point ]
        right_array = arr[ midway_point : ]

        left = merge_sort(left_array)
        right = merge_sort(right_array)

        arr = merge(left, right)


    return arr
