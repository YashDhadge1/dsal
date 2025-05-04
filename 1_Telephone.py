SIZE = 10
table = [None] * SIZE

def hash_function(key):
    return key % SIZE

def insert_linear(name, tel_no):
    index = hash_function(tel_no)
    for i in range(SIZE):
        new_index = (index + i) % SIZE
        if table[new_index] is None:
            table[new_index] = [name, tel_no]
            print(f"Inserted at index {new_index} using Linear Probing")
            return
    print("Hash table is full. Cannot insert.")

def insert_quadratic(name, tel_no):
    index = hash_function(tel_no)
    for i in range(1, SIZE):
        new_index = (index + i * i) % SIZE
        if table[new_index] is None:
            table[new_index] = [name, tel_no]
            print(f"Inserted at index {new_index} using Quadratic Probing")
            return
    print("Hash table is full. Cannot insert.")

def insert_double_hashing(name, tel_no):
    index1 = hash_function(tel_no)
    index2 = 7 - (tel_no % 7)
    for i in range(SIZE):
        new_index = (index1 + i * index2) % SIZE
        if table[new_index] is None:
            table[new_index] = [name, tel_no]
            print(f"Inserted at index {new_index} using Double Hashing")
            return
    print("Hash table is full. Cannot insert.")

def display():
    print("\n--- Telephone Directory ---")
    for i in range(SIZE):
        if table[i] is not None:
            print(f"Index {i}: Name = {table[i][0]}, Phone = {table[i][1]}")
        else:
            print(f"Index {i}: Empty")

def search(name):
    for i in range(SIZE):
        if table[i] is not None and table[i][0].lower() == name.lower():
            print(f"\n'{name}' found at index {i} with phone number {table[i][1]}")
            return
    print(f"\n'{name}' not found in the directory.")

def main():
    while True:
        print("\n===== Telephone Directory =====")
        print("1. Insert using Linear Probing")
        print("2. Insert using Quadratic Probing")
        print("3. Insert using Double Hashing")
        print("4. Display Table")
        print("5. Search by Name")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice in [1, 2, 3]:
            name = input("Enter Name: ")
            tel_no = int(input("Enter Telephone Number: "))
            if choice == 1:
                insert_linear(name, tel_no)
            elif choice == 2:
                insert_quadratic(name, tel_no)
            elif choice == 3:
                insert_double_hashing(name, tel_no)
        elif choice == 4:
            display()
        elif choice == 5:
            search_name = input("Enter name to search: ")
            search(search_name)
        elif choice == 6:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
