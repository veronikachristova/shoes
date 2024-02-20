class Shoe:
    def __init__(self, id, gender, type, color, price, brand, size):
        self.id = id
        self.gender = gender
        self.type = type
        self.color = color
        self.price = price
        self.brand = brand
        self.size = size

    def __str__(self):
        return f"Shoe:{self.id},{self.brand}, {self.type}, ({self.gender}), Color: {self.color}, Size: {self.size}, Price: {self.price}eur"


class ShoeModel:
    def __init__(self):
        self.shoes = []

    def add(self, shoe):
        self.shoes.append(shoe)

    def delete(self, id):
        shoes_to_delete = []
        for shoe in self.shoes:
            if shoe.id == id:
                shoes_to_delete.append(shoe)
        for shoe in shoes_to_delete:
            self.shoes.remove(shoe)
        return self.shoes

    def get_all_shoes(self):
        return self.shoes

    def get_shoe_by_size(self, size):
        shoes_by_size = []
        for shoe in self.shoes:
            if shoe.size == size:
                shoes_by_size.append(shoe)
        return shoes_by_size

    def get_grand_total(self):
        prices = []
        for shoe in self.shoes:
            prices.append(shoe.price)
        return sum(prices)


class ShoeView:
    def display_shoes(self, shoes):
        print("Shoe Inventory:")
        for shoe in shoes:
            print(shoe)

    def display_total_price(self, total_price):
        print(f"Total Price of Shoes: {total_price}eur")


class ShoeController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_shoe(self, id, gender, type, color, price, brand, size):
        shoe = Shoe(id, gender, type, color, price, brand, size)
        if shoe not in self.model.shoes:
            self.model.add(shoe)

    def delete_shoe_by_id(self, id):
        return self.model.delete(id)

    def view_all_shoes(self):
        shoes = self.model.get_all_shoes()
        self.view.display_shoes(shoes)

    def view_shoes_by_size(self, size):
        shoes = self.model.get_shoe_by_size(size)
        self.view.display_shoes(shoes)

    def view_total_price(self):
        total_price = self.model.get_grand_total()
        self.view.display_total_price(total_price)


if __name__ == "__main__":
    shoe_model = ShoeModel()
    shoe_view = ShoeView()
    shoe_controller = ShoeController(shoe_model, shoe_view)


    shoe_controller.add_shoe(1, "Men", "Sneakers", "Black", 10, "Nike", 10)
    shoe_controller.add_shoe(2, "Women", "Sandals", "Brown", 30, "Adidas", 7)
    shoe_controller.add_shoe(3, "Women", "Boots", "Red", 80, "Timberland", 9)
    shoe_controller.add_shoe(4, "Men", "Heels", "Pink", 30, "Gucci", 10)
    shoe_controller.add_shoe(5, "Women", "Wedges", "Brown", 30, "Mustang", 11)
    shoe_controller.add_shoe(6, "Women", "Boots", "Orange", 40, "Asos", 5)
    shoe_controller.add_shoe(7, "Men", "Sneakers", "Black", 50, "New Balance", 10)
    shoe_controller.add_shoe(8, "Women", "Sneakers", "White", 30, "Bershka", 8)
    shoe_controller.add_shoe(9, "Women", "Boots", "Green", 40, "Zara", 6)
    shoe_controller.add_shoe(10, "Women", "Boots", "Purple", 50, "Massimo Dutti", 9)

    shoe_controller.view_all_shoes()

    shoe_id_to_delete = 2

    shoe_controller.view_all_shoes()
    shoe_controller.view_total_price()
