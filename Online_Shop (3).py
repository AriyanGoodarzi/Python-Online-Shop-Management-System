class Product:
    def __init__(self, id, name, price, stock, description):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock
        self.description = description

    def __str__(self):
        return f"{self.id}.{self.name}|{self.price}|Stock:{self.stock}"

    @staticmethod
    def create_products():
        products = {
            1: Product(1, "h&m t-shirt",300000, 20, "casual cotton t-shirt"),
            2: Product(2, "jeans",750000, 10, "blue denim jeans"),
            3: Product(3, "vans hoodie",900000, 8, "warm hoodie"),
            4: Product(4, "levi jacket",1500000, 5,"denim jacket"),
            5: Product(5, "fila sneakers",1200000, 12, "sport shoes"),
            6: Product(6, "puma cap",150000, 20, "baseball cap"),
            7: Product(7, "uniqlo sweater",650000, 7, "wool sweater"),
            8: Product(8, "adidas shorts",400000, 10, "sport shorts"),
            9: Product(9, "nike socks",80000, 30, "cotton socks"),
            10: Product(10, "belt",180000, 18, "leather belt"),
            11: Product(11, "adidas t-shirt",450000, 10, "casual sports t-shirt"),
            12: Product(12, "nike hoodie",950000, 8, "warm hoodie"),
            13: Product(13, "levi jeans",780000, 12, "blue denim jeans"),
            14: Product(14, "puma sneakers",1200000, 15, "running shoes"),
            15: Product(15, "zara jacket",1500000, 7, "winter jacket"),
            16: Product(16, "h&m sweater",650000, 9, "wool sweater"),
            17: Product(17, "vans sneakers",1100000, 14, "skate shoes"),
            18: Product(18, "under armour shorts",320000, 10, "sports short"),
            19: Product(19, "ralph lauren polo",500000, 6, "cotton polo shirt"),
            20: Product(20, "converse shoes",900000, 8, "casual sneakers"),
            21: Product(21, "tommy hilfiger shirt",600000, 10, "casual cotton shirt"),
            22: Product(22, "gucci belt",2000000, 5, "leather belt"),
            23: Product(23, "lacoste polo",550000, 12, "cotton polo shirt"),
            24: Product(24, "north face jacket",1800000, 7, "winter jacket"),
            25: Product(25, "reebok sneakers",950000, 10, "training shoes"),
            26: Product(26, "diesel jeans",800000, 6, "blue denim jeans"),
            27: Product(27, "new balance shoes",850000, 12, "running shoes"),
            28: Product(28, "patagonia hoodie",1000000, 8, "warm hoodie"),
            29: Product(29, "uniqlo t-shirt",250000, 20, "cotton t-shirt"),
            30: Product(30, "fila cap",150000, 18, "baseball cap"),
        }
        return products

    @staticmethod
    def save_products_csv(products):
        with open("products.csv","w",encoding="utf-8") as f:
            f.write("id,name,price,stock,description\n")
            for product_id in products:
                p = products[product_id]
                f.write(f"{p.id},{p.name},{p.price},{p.stock},{p.description}\n")

    @staticmethod
    def load_products_csv():
        products = {}
        try:
            with open("products.csv","r",encoding="utf-8") as f:
                lines = f.readlines()
            for i in range(1,len(lines)):
                parts = lines[i].strip().split(",")
                id = int(parts[0])
                name = parts[1]
                price = int(parts[2])
                stock = int(parts[3])
                description = parts[4]
                products[id] = Product(id, name, price, stock, description)
        except FileNotFoundError:
            products = Product.create_products()
            Product.save_products_csv(products)
        return products

    @staticmethod
    def show_products(products):
        print("\n" + "=" * 70)
        print(" " * 25 + "product list")
        print("=" * 70)
        print("id | product name               | price (toman) | status")
        print("-" * 70)
        total_products = 0
        for product_id in products:
            p = products[product_id]
            total_products += 1
            id_str = str(p.id).ljust(2)
            name_str = p.name.ljust(26)
            price_str = str(p.price).ljust(13)
            status_str = f"In stock ({p.stock})" if p.stock > 0 else "not available"
            print(f"{id_str} | {name_str} | {price_str} | {status_str}")
        print("-" * 70)
        print(f"total products: {total_products}")
        print("=" * 70)

    @staticmethod
    def view_product_details(products):
        try:
            product_id = int(input("enter product id to view details (0 to quit): "))
            if product_id == 0:
                return
            if product_id in products:
                p = products[product_id]
                print("\n" + "=" * 50)
                print("product details")
                print("=" * 50)
                print(f"id: {p.id}")
                print(f"name: {p.name}")
                print(f"price: {p.price}")
                print(f"stock: {p.stock}")
                print(f"status: {'In stock' if p.stock>0 else 'not available'}")
                print(f"description: {p.description}")
                print("=" * 50)
            else:
                print("invalid product id")
        except ValueError:
            print("please enter a valid number.")

class Cart:
    def __init__(self):
        self.items = {}

    def add_to_cart(self, products):
        while True:
            try:
                product_id = int(input("enter product id to add to cart (0 to finish adding): "))
                if product_id == 0:
                    break
                if product_id not in products:
                    print("invalid product id")
                    continue
                product = products[product_id]
                if product.stock == 0:
                    print(f" {product.name} is not available.")
                    continue
                quantity = int(input(f"enter quantity for {product.name} (available: {product.stock}): "))
                if quantity <= 0:
                    print(" quantity must be greater than 0.")
                    continue
                if quantity > product.stock:
                    print(f" only {product.stock} items available.")
                    continue
                if product_id in self.items:
                    self.items[product_id] += quantity
                else:
                    self.items[product_id] = quantity
                print(f" added {quantity} x {product.name} to cart.")
            except ValueError:
                print(" please enter a valid number.")

    def remove_from_cart(self, products):
        try:
            product_id = int(input("enter product id to remove from cart (0 to quit): "))
            if product_id == 0:
                return
            if product_id not in self.items:
                print("product not in cart.")
                return
            del self.items[product_id]
            print(f" product removed from cart.")
        except ValueError:
            print("please enter a valid number.")

    def show_cart(self, products, shipping=None):
        print("\n" + "=" * 60)
        print(" " * 20 + "shopping cart")
        print("=" * 60)
        if not self.items:
            print("your cart is empty.")
        else:
            total = 0
            print("id | product name            | qty | unit price | total")
            print("-" * 60)
            for pid, qty in self.items.items():
                product = products[pid]
                line_total = qty * product.price
                total += line_total
                print(f"{str(pid).ljust(2)} | {product.name.ljust(24)} | {str(qty).ljust(3)} | {str(product.price).ljust(10)} | {line_total}")
            if shipping and shipping.selected_method:
                print(f"shipping ({shipping.selected_method['name']}) | Cost: {shipping.selected_method['cost']}")
                total += shipping.selected_method['cost']
            print("-" * 60)
            print(f"total amount: {total}")
        print("=" * 60)

    def checkout(self, products):
        if not self.items:
            print(" cart is empty cannot checkout.")
            return
        print("\nprocessing checkout")
        for pid, qty in self.items.items():
            product = products[pid]
            if qty > product.stock:
                print(f" not enough stock for {product.name}. available: {product.stock}")
                return
            product.stock -= qty
        Product.save_products_csv(products)
        print(" checkout successful\n")

class Invoice:
    invoice_counter = 1

    def __init__(self, cart_items, products, shipping_cost=0, shipping_name=""):
        self.invoice_id = Invoice.invoice_counter
        Invoice.invoice_counter += 1
        self.items = cart_items.copy()
        self.products = products
        self.shipping_cost = shipping_cost
        self.shipping_name = shipping_name
        self.total = self.calculate_total()
        self.paid = False

    def calculate_total(self):
        total = self.shipping_cost
        for pid, qty in self.items.items():
            product = self.products[pid]
            total += qty * product.price
        return total

    def update_shipping(self, shipping_cost, shipping_name):
        self.shipping_cost = shipping_cost
        self.shipping_name = shipping_name
        self.total = self.calculate_total()

    def show_invoice(self):
        print("\n" + "=" * 60)
        print(f"invoice #{self.invoice_id}")
        print("-" * 60)
        for pid, qty in self.items.items():
            product = self.products[pid]
            print(f"{product.name} | qty: {qty} | unit: {product.price} | total: {qty*product.price}")
        if self.shipping_cost > 0:
            print(f"shipping ({self.shipping_name}) | cost: {self.shipping_cost}")
        print("-" * 60)
        print(f"total amount: {self.total}")
        print(f"status: {'paid' if self.paid else 'unpaid'}")
        print("=" * 60)

    def save_invoice_to_file(self):
        filename = f"invoice_{self.invoice_id}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"invoice #{self.invoice_id}\n")
            f.write("-" * 50 + "\n")
            for pid, qty in self.items.items():
                product = self.products[pid]
                f.write(f"{product.name} | qty: {qty} | unit: {product.price} | total: {qty * product.price}\n")
            if self.shipping_cost > 0:
                f.write(f"shipping ({self.shipping_name}) | cost: {self.shipping_cost}\n")
            f.write("-" * 50 + "\n")
            f.write(f"total: {self.total}\n")
            f.write(f"status: {'paid' if self.paid else 'unpaid'}\n")
        print(f"invoice saved as {filename}")

    def pay_invoice(self):
        if self.paid:
            print("invoice already paid.")
        else:
            self.paid = True
            print("payment successful. invoice marked as paid.")

class Shipping:
    methods = {
        1: {"name": "standard delivery", "cost": 50000, "time": "3-5 days"},
        2: {"name": "express delivery", "cost": 100000, "time": "1-2 days"},
        3: {"name": "pick-up from store", "cost": 0, "time": "same day"}
    }

    def __init__(self):
        self.selected_method = None

    def show_methods(self):
        print("\n" + "=" * 50)
        print("shipping methods")
        print("=" * 50)
        for mid, info in Shipping.methods.items():
            print(f"{mid}. {info['name']} - cost: {info['cost']} | time: {info['time']}")
        print("=" * 50)

    def choose_method(self, last_invoice=None):
        try:
            method_id = int(input("select shipping method (0 to cancel): "))
            if method_id == 0:
                print("shipping selection cancelled.")
                return
            if method_id in Shipping.methods:
                self.selected_method = Shipping.methods[method_id]
                print(f"selected {self.selected_method['name']} - cost: {self.selected_method['cost']} | time: {self.selected_method['time']}")
                if last_invoice:
                    last_invoice.update_shipping(self.selected_method["cost"], self.selected_method["name"])
            else:
                print("invalid shipping method.")
        except ValueError:
            print("please enter a valid number.")

class Help:
    @staticmethod
    def show_help():
        print("\n" + "="*50)
        print("help & information")
        print("="*50)
        print("1. user guide: how to use the shopping system")
        print("2. contact us: ariyan@gmail.com | +98 912 051 0725")
        print("3. about us: We are a sample shopping app for learning purposes")
        print("="*50)

class UserProfile:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.purchase_count = 0

    def show_profile(self):
        print("\n" + "="*50)
        print(f"user profile: {self.username}")
        print(f"email: {self.email}")
        print(f"total purchases: {self.purchase_count}")
        print("="*50)

    def increment_purchases(self):
        self.purchase_count += 1

class UserSystem:
    users = {}

    @staticmethod
    def register():
        username = input("enter new username: ")
        if username in UserSystem.users:
            print(" username already exists.")
            return None
        password = input("enter password: ")
        email = input("enter email: ")
        UserSystem.users[username] = {"password": password, "email": email, "profile": UserProfile(username, email)}
        print("registration successful.")
        return username

    @staticmethod
    def login():
        username = input("enter username: ")
        password = input("enter password: ")
        if username in UserSystem.users and UserSystem.users[username]["password"] == password:
            print(f" welcome back {username}.")
            return username
        print("invalid username or password")
        return None

products = Product.load_products_csv()
cart = Cart()
last_invoice = None
shipping = Shipping()
current_user = None

while True:
    if not current_user:
        print("\n1. login")
        print("2. register")
        print("0. exit")
        choice = input("select an option: ")
        if choice == "1":
            current_user = UserSystem.login()
        elif choice == "2":
            current_user = UserSystem.register()
        elif choice == "0":
            print("goodbye")
            break
        else:
            print("invalid choice.")
        continue

    Product.show_products(products)
    print("1. add to cart")
    print("2. remove from cart")
    print("3. view cart")
    print("4. checkout")
    print("5. view product details")
    print("6. show last invoice")
    print("7. save invoice to file")
    print("8. pay invoice")
    print("9. shipping options")
    print("10. help & info")
    print("11. view profile")
    print("12. logout")
    print("0. exit")

    choice = input("select an option: ")
    if choice == "1":
        cart.add_to_cart(products)
    elif choice == "2":
        cart.remove_from_cart(products)
    elif choice == "3":
        cart.show_cart(products, shipping)
    elif choice == "4":
        if cart.items:
            shipping_cost = shipping.selected_method["cost"] if shipping.selected_method else 0
            shipping_name = shipping.selected_method["name"] if shipping.selected_method else "no shipping"
            last_invoice = Invoice(cart.items, products, shipping_cost, shipping_name)
            UserSystem.users[current_user]["profile"].increment_purchases()
        cart.checkout(products)
    elif choice == "5":
        Product.view_product_details(products)
    elif choice == "6":
        if last_invoice:
            last_invoice.show_invoice()
        else:
            print(" no invoice available.")
    elif choice == "7":
        if last_invoice:
            last_invoice.save_invoice_to_file()
        else:
            print(" no invoice available.")
    elif choice == "8":
        if last_invoice:
            last_invoice.pay_invoice()
        else:
            print(" no invoice available.")
    elif choice == "9":
        shipping.show_methods()
        shipping.choose_method(last_invoice)
    elif choice == "10":
        Help.show_help()
    elif choice == "11":
        UserSystem.users[current_user]["profile"].show_profile()
    elif choice == "12":
        current_user = None
        print("logged out successfully.")

