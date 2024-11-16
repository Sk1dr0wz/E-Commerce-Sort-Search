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
