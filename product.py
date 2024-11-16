class Product:
    def __init__(self, product_id, product_name, price, number_of_reviews, rating, category):
        self.product_id = product_id
        self.product_name = product_name
        self.price = float(price)
        self.number_of_reviews = int(number_of_reviews)
        self.rating = float(rating)
        self.category = category

    def __repr__(self):
        return (f"{self.product_id}: {self.product_name} - ${self.price:.2f}, "
                f"Rating: {self.rating}, Reviews: {self.number_of_reviews}, Category: {self.category}")
