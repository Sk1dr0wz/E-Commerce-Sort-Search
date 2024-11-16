from data_handler import read_products, write_products
from sorting import quick_sort

def display_products(products):
    """Display a list of products in a readable format."""
    for product in products:
        print(f"{product.product_id}: {product.product_name} - ${product.price:.2f}, "
              f"Rating: {product.rating}, Reviews: {product.number_of_reviews}, Category: {product.category}")

def sorting_menu(products):
    """Handle the sorting menu."""
    while True:
        print("\nSorting Menu:")
        print("1. Quick Sort")
        print("2. Merge Sort (not yet implemented)")
        print("3. Heap Sort (not yet implemented)")
        print("4. Back to Main Menu")
        choice = input("Select the sorting algorithm: ")

        if choice == "1":
            while True:
                print("\nQuick Sort Criteria:")
                print("1. Sort by Price (Ascending)")
                print("2. Sort by Rating (Descending)")
                print("3. Sort by Number of Reviews (Descending)")
                print("4. Back to Sorting Menu")
                criteria = input("Select sorting criteria: ")

                if criteria == "1":
                    products = quick_sort(products, key='price', reverse=False)
                    print("\nProducts sorted by Price (Ascending):")
                    display_products(products)
                elif criteria == "2":
                    products = quick_sort(products, key='rating', reverse=True)
                    print("\nProducts sorted by Rating (Descending):")
                    display_products(products)
                elif criteria == "3":
                    products = quick_sort(products, key='number_of_reviews', reverse=True)
                    print("\nProducts sorted by Number of Reviews (Descending):")
                    display_products(products)
                elif criteria == "4":
                    break
                else:
                    print("Invalid choice. Please try again.")
        elif choice in ["2", "3"]:
            print("Selected algorithm is not yet implemented.")
        elif choice == "4":
            return products
        else:
            print("Invalid choice. Please try again.")

def searching_menu(products):
    """Handle the searching menu."""
    while True:
        print("\nSearching Menu:")
        print("1. Linear Search (not yet implemented)")
        print("2. Binary Search (not yet implemented)")
        print("3. Back to Main Menu")
        choice = input("Select the searching algorithm: ")

        if choice in ["1", "2"]:
            print("Selected searching algorithm is not yet implemented.")
        elif choice == "3":
            return
        else:
            print("Invalid choice. Please try again.")

def main():
    filename = "productdata.csv"
    products = read_products(filename)

    if not products:
        print("No products to display. Starting with an empty product list.")

    while True:
        print("\nMain Menu:")
        print("1. Display Products")
        print("2. Sorting Algorithms")
        print("3. Searching Algorithms")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            display_products(products)
        elif choice == "2":
            products = sorting_menu(products)
        elif choice == "3":
            searching_menu(products)
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
