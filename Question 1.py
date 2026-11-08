import time


# ------------------------------------------------------------
# 1. Medicine Entity Class
# ------------------------------------------------------------

class Medicine:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def display(self):
        print("Product ID:", self.product_id)
        print("Product Name:", self.name)
        print("Price: RM", format(self.price, ".2f"))
        print("Stock Quantity:", self.stock)


# ------------------------------------------------------------
# 2. Hash Table Class
# ------------------------------------------------------------

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    # Hash function using division method
    def hash_function(self, key):
        return key % self.size

    # Insert medicine using linear probing
    def insert(self, medicine):
        index = self.hash_function(medicine.product_id)
        original_index = index
        collisions = 0

        while self.table[index] is not None:

            # Update if product ID already exists
            if self.table[index].product_id == medicine.product_id:
                self.table[index] = medicine
                print("Product updated successfully.")
                return True

            # Linear probing
            index = (index + 1) % self.size
            collisions += 1

            # Check whether the table is full
            if index == original_index:
                print("Hash table is full!")
                return False

        self.table[index] = medicine

        print("Product inserted successfully into slot", index)
        print("Collisions:", collisions)

        return True

    # Search medicine using linear probing
    def search(self, product_id):
        index = self.hash_function(product_id)
        original_index = index

        while self.table[index] is not None:

            if self.table[index].product_id == product_id:
                return self.table[index]

            index = (index + 1) % self.size

            if index == original_index:
                break

        return None

    # Display all hash table slots
    def display(self):
        print("\n===== HASH TABLE =====")

        for i in range(self.size):
            if self.table[i] is None:
                print("Index", i, ": Empty")
            else:
                medicine = self.table[i]
                print("Index", i, ":", medicine.product_id,
                      "-", medicine.name)


# ------------------------------------------------------------
# 3. Array Search Function
# ------------------------------------------------------------

def array_search(products, product_id):

    for medicine in products:
        if medicine.product_id == product_id:
            return medicine

    return None


# ------------------------------------------------------------
# 4. Search Performance Comparison
# ------------------------------------------------------------

def compare_search_performance(hash_table, products, product_id):

    repetitions = 10000

    # Hash table search
    start_time = time.perf_counter_ns()

    for i in range(repetitions):
        hash_table.search(product_id)

    hash_time = time.perf_counter_ns() - start_time

    # Array search
    start_time = time.perf_counter_ns()

    for i in range(repetitions):
        array_search(products, product_id)

    array_time = time.perf_counter_ns() - start_time

    print("\n===== SEARCH PERFORMANCE COMPARISON =====")
    print("Number of searches:", repetitions)

    print("\nHash Table:")
    print("Total time:", hash_time, "nanoseconds")
    print("Average time:",
          format(hash_time / repetitions, ".2f"), "nanoseconds")

    print("\nOne-Dimensional Array:")
    print("Total time:", array_time, "nanoseconds")
    print("Average time:",
          format(array_time / repetitions, ".2f"), "nanoseconds")


# ------------------------------------------------------------
# 5. Main Inventory System
# ------------------------------------------------------------

def main():

    hash_table = HashTable(11)

    # Predefined medicine records
    products = [
        Medicine(1042, "Paracetamol 500mg", 5.90, 120),
        Medicine(1053, "Vitamin C 1000mg", 12.50, 80),
        Medicine(1064, "Cough Syrup", 15.90, 50),
        Medicine(1075, "Antacid Tablets", 8.90, 100),
        Medicine(1086, "Ibuprofen 200mg", 7.50, 90),
        Medicine(1097, "Antiseptic Cream", 10.90, 40)
    ]

    # Insert predefined products into hash table
    for medicine in products:
        hash_table.insert(medicine)

    while True:

        print("\n===== PHARMACY INVENTORY SYSTEM =====")
        print("1. Insert Product")
        print("2. Search Product")
        print("3. Display Hash Table")
        print("4. Compare Search Performance")
        print("5. Exit")

        choice = input("Enter choice: ")

        # Insert product
        if choice == "1":

            try:
                product_id = int(input("Enter Product ID: "))
                name = input("Enter Product Name: ")
                price = float(input("Enter Product Price: "))
                stock = int(input("Enter Stock Quantity: "))

                if price < 0 or stock < 0:
                    print("Price and stock cannot be negative.")
                    continue

                medicine = Medicine(
                    product_id, name, price, stock
                )

                result = hash_table.insert(medicine)

                if result:
                    # Keep array records consistent
                    updated = False

                    for i in range(len(products)):
                        if products[i].product_id == product_id:
                            products[i] = medicine
                            updated = True
                            break

                    if not updated:
                        products.append(medicine)

            except ValueError:
                print("Invalid input. Please enter correct values.")

        # Search product
        elif choice == "2":

            try:
                product_id = int(input("Enter Product ID to search: "))

                result = hash_table.search(product_id)

                if result is not None:
                    print("\nProduct Found!")
                    result.display()
                else:
                    print("Product not found.")

            except ValueError:
                print("Please enter a valid numeric product ID.")

        # Display hash table
        elif choice == "3":
            hash_table.display()

        # Compare performance
        elif choice == "4":

            try:
                product_id = int(input("Enter Product ID to search: "))

                if hash_table.search(product_id) is None:
                    print("Product not found. Enter an existing ID.")
                else:
                    compare_search_performance(
                        hash_table, products, product_id
                    )

            except ValueError:
                print("Please enter a valid numeric product ID.")

        # Exit
        elif choice == "5":
            print("Exiting Inventory System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
