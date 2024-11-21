def quick_sort(products, key, reverse=False):
    """
    Perform Quick Sort on a list of product objects based on the specified key.

    :param products: List of Product objects to sort.
    :param key: The attribute to sort by (e.g., 'price', 'rating', 'number_of_reviews').
    :param reverse: True for descending order, False for ascending order.
    :return: A sorted list of Product objects.
    """
    if len(products) <= 1:
        return products

    # Choose a pivot value
    pivot = products[len(products) // 2]
    pivot_value = getattr(pivot, key)

    # Partition the list based on the pivot
    if reverse:
        # Descending order
        left = [p for p in products if getattr(p, key) > pivot_value]
        middle = [p for p in products if getattr(p, key) == pivot_value]
        right = [p for p in products if getattr(p, key) < pivot_value]
    else:
        # Ascending order
        left = [p for p in products if getattr(p, key) < pivot_value]
        middle = [p for p in products if getattr(p, key) == pivot_value]
        right = [p for p in products if getattr(p, key) > pivot_value]

    # Recursively sort the partitions and combine them
    return quick_sort(left, key, reverse) + middle + quick_sort(right, key, reverse)


def merge_sort(products, left, right, key, reverse=False): 
    """
    Perform Merge Sort on a list of product objects partitioned by left object to right object based on the specified key.

    :param products: List of Product objects to sort.
    :param left: The left-most object of the current list partition.
    :param right: The right-most object of the current list partition.
    :param key: The attribute to sort by (e.g., 'price', 'rating', 'number_of_reviews').
    :param reverse: True for descending order, False for ascending order.
    :return: A sorted list of Product objects.
    """
    def merge(products, left, middle, right, key, reverse=False):
        """
        Submethod: Sorts two halves of a list partition and merges into one partition.
        
        :param middle: The middle object of the current list partition.
        (Refer to parent method for other param definitions.)
        """
        length_array_left = middle - left + 1
        length_array_right = right - middle

        # Create temporary arrays
        array_left = [0] * length_array_left
        array_right = [0] * length_array_right

        # Copy data to temp arrays
        for i in range(length_array_left):
            array_left[i] = products[left + i]
        for j in range(length_array_right):
            array_right[j] = products[middle + 1 + j]

        index_array_left = 0  # Initial index of left subarray
        index_array_right = 0  # Initial index of right subarray
        index_array_merged = left  # Initial index of merged subarray

        # Sort the two halves, then merge the temp arrays back into products[left..right]
        while index_array_left < length_array_left and index_array_right < length_array_right:

            # reverse XOR (left key <= right key)
            if reverse ^ (getattr(array_left[index_array_left], key) <= getattr(array_right[index_array_right], key)):
                products[index_array_merged] = array_left[index_array_left]
                index_array_left += 1
            else: 
                products[index_array_merged] = array_right[index_array_right]
                index_array_right += 1
                
            index_array_merged += 1

        # Copy the remaining elements in the left array (if there are any)
        while index_array_left < length_array_left:
            products[index_array_merged] = array_left[index_array_left]
            index_array_left += 1
            index_array_merged += 1

        # Copy the remaining elements in the right array (if there are any)
        while index_array_right < length_array_right:
            products[index_array_merged] = array_right[index_array_right]    
            index_array_right += 1
            index_array_merged += 1


    if left < right:
        middle = (left + right) // 2

        # Divide / partition the list into halves
        # Recursively sort and merge the list partitions
        merge_sort(products, left, middle, key, reverse)  
        merge_sort(products, middle + 1, right, key, reverse)
        merge(products, left, middle, right, key, reverse)

    return products
