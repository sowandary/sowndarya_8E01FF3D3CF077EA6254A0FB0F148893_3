def linear_search_product(products, target_product):
    """
    Perform linear search to find target_product in the products list.
    
    Args:
    products (list): List of products.
    target_product (str): Target product name to search for.
    
    Returns:
    list: List of indices of all occurrences of the target product, or an empty list if not found.
    """
    indices = []
    for index, product in enumerate(products):
        if product == target_product:
            indices.append(index)
    return indices

# Example usage
products = ["apple", "banana", "orange", "apple", "grape", "apple"]
target_product = "apple"
result = linear_search_product(products, target_product)
print("Indices of", target_product, ":", result)


