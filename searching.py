from operator import attrgetter
def linear_search(products, target, key=None, opt_target_max=None):
    """
    Perform linear search on a list of product objects to obtain a results list matching the target criteria based on the specified key.
    Optionally, it can search by matching a target range if a maximum target criteria is specified.

    :param products: List of Product objects to search.
    :param target: The target criteria to search for. Optionally acts as the minimum target if opt_target_max is specified.
    :param key: The attribute to search by (e.g., 'product_id', 'category', 'price').
    :param opt_target_max: Optional maximum target criteria to search for.
    """
    results = []

    # Traverse through all products
    for product in products:
        # If a product attribute matches the target / target range, add into results list
        if (opt_target_max and getattr(product, key) >= target and getattr(product, key) <= opt_target_max) or (getattr(product, key) == target):
            results.append(product)

    return results

def binary_search(products, target, key=None, opt_target_max=None):
    """
    Perform binary search on a sorted list of product objects to find products matching the target criteria.
    Optionally, it can search by a target range if a maximum target is specified.
    
    :param products: List of Product objects to search.
    :param target: The target criteria to search for. Optionally acts as the minimum target if opt_target_max is specified.
    :param key: The attribute to search by (e.g., 'product_id', 'category', 'price').
    :param opt_target_max: Optional maximum target criteria to search for.
    :return: List of products that match the search criteria.
    """
    # Sort the products by the specified key before performing the binary search
    sorted_products = sorted(products, key=lambda x: getattr(x, key))

    # If we're searching by a range, we need to perform binary search in that range
    if opt_target_max:
        results = []
        # Search for the lower bound (target) first
        low, high = 0, len(sorted_products) - 1
        while low <= high:
            mid = (low + high) // 2
            mid_val = getattr(sorted_products[mid], key)
            if mid_val < target:
                low = mid + 1
            elif mid_val > target:
                high = mid - 1
            else:
                # Found exact match, now check the range
                results.append(sorted_products[mid])
                break
        
        # Add all products within the target and opt_target_max range
        for product in sorted_products[low:]:
            if getattr(product, key) <= opt_target_max:
                results.append(product)
            else:
                break
        
        return results

    else:
        # For exact match searches (like Category), return all matches
        low, high = 0, len(sorted_products) - 1
        results = []

        while low <= high:
            mid = (low + high) // 2
            mid_val = getattr(sorted_products[mid], key)
            if mid_val < target:
                low = mid + 1
            elif mid_val > target:
                high = mid - 1
            else:
                # Exact match found, add this product to the results
                results.append(sorted_products[mid])

                # Collect additional matches to the left
                left = mid - 1
                while left >= 0 and getattr(sorted_products[left], key) == target:
                    results.append(sorted_products[left])
                    left -= 1

                # Collect additional matches to the right
                right = mid + 1
                while right < len(sorted_products) and getattr(sorted_products[right], key) == target:
                    results.append(sorted_products[right])
                    right += 1
                
                break  # We've collected all matching products

        return results


