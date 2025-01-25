# function to sort lists in ascending
def sort_algorithm(arr):
    n = len(arr)

    # loop to check through the whole list
    for i in range(n):

        # loop to sort the elements
        for j in range(0, n-i-1):

            # condition to switch position of elements
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return  arr
unsorted_list = [100, 95, 80, 10, 20, 40, 30, 50, 60, -35]

# calling the sort function
sorted_list = sort_algorithm(unsorted_list)
print("Sorted list is:", sorted_list)