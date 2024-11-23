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
    