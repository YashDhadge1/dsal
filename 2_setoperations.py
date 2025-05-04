class MySet: 
    def __init__(self):
        self.elements = []
    
    def add(self, newElement):
        if not self.contains(newElement):
            self.elements.append(newElement)
            
    def remove(self, element): 
        new_list = []
        for e in self.elements:
            if e != element:
                new_list.append(element) 
        self.elements = new_list
        
    def contains(self, element):
        for e in self.elements:
            if e == element:
                return True
        return False
    
    def iterator(self):
        for e in self.elements:
            yield e
    
    def size(self):
        count = 0
        for _ in self.elements:
            count += 1
        return count    
    
    def intersection(self, other_set):
        result = MySet()
        for e in self.elements:
            if other_set.contains(e):
                result.add(e)
        return result
    
    def union(self, other_set):
        result = MySet()
        for e in self.elements:
            result.add(e)
        for e in other_set.elements:
            result.add(e)
        return result
    
    def difference(self, other_set):
        result = MySet()
        for e in self.contains:
            if not other_set.contains(e):
                result.add(e)
        return result
    
    def isSubset(self, other_set):
        for e in self.contains:
            if not other_set.contains(e):
                return False
        return True
    
    def display(self):
        print(self.elements)
        
def menu():
    A = MySet()
    B = MySet()
    
    while True:
        print("\n--- MENU ---")
        print("1. Add to Set A")
        print("2. Add to Set B")
        print("3. Remove from Set A")
        print("4. Remove from Set B")
        print("5. Show Set A")
        print("6. Show Set B")
        print("7. Size of Set A")
        print("8. A ∩ B (Intersection)")
        print("9. A ∪ B (Union)")
        print("10. A - B (Difference)")
        print("11. A ⊆ B (Subset Check)")
        print("12. Exit")
        
        ch = input("Enter choice: ")
        if ch == "1":
            count = int(input("How many elements do you want to add to Set A? "))
            for i in range(count):
                x = int(input(f"Enter element {i+1}: "))
                A.add(x)

        elif ch == "2":
            count = int(input("How many elements do you want to add to Set B? "))
            for i in range(count):
                x = int(input(f"Enter element {i+1}: "))
                B.add(x)
        elif ch == "3":
            x = int(input("Enter value to remove from Set A: "))
            A.remove(x)
        elif ch == "4":
            x = int(input("Enter value to remove from Set B: "))
            B.remove(x)
        elif ch == "5":
            print("Set A:", end=" ")
            A.display()
        elif ch == "6":
            print("Set B:", end=" ")
            B.display()
        elif ch == "7":
            print("Size of Set A:", A.size())
        elif ch == "8":
            print("A ∩ B:", end=" ")
            A.intersection(B).display()
        elif ch == "9":
            print("A ∪ B:", end=" ")
            A.union(B).display()
        elif ch == "10":
            print("A - B:", end=" ")
            A.difference(B).display()
        elif ch == "11":
            print("A is subset of B:", A.is_subset(B))
        elif ch == "12":
            print("Exiting.")
            break
        else:
            print("Invalid choice. Try again.")

menu()
