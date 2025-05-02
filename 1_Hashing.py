class TelephoneRecord:
    """A class to store telephone record data"""
    def __init__(self, name, tel_no):
        self.name = name
        self.tel_no = tel_no
        
    def __str__(self):
        return f"{self.name}: {self.tel_no}"


class Node:
    """Node class for linked list implementation in chaining"""
    def __init__(self, data=None):
        self.data = data  # Can be a TelephoneRecord or raw phone number
        self.next = None


class HashTable:
    """Generic hash table with multiple collision handling techniques"""
    
    def __init__(self, size=100, method="separate_chaining"):
        """Initialize hash table with specified size and collision handling method"""
        self.size = size
        self.method = method
        self.comparison_count = 0
        
        # Initialize appropriate data structure based on method
        if method == "separate_chaining":
            self.table = [[] for _ in range(size)]
        elif method in ["linear_probing", "quadratic_probing", "double_hashing"]:
            self.table = [None] * size
        else:
            raise ValueError("Invalid collision handling method")
    
    def hash_function(self, key):
        """Primary hash function"""
        if isinstance(key, str):
            # For string keys (like names)
            return sum(ord(c) for c in key) % self.size
        elif isinstance(key, int):
            # For integer keys (like phone numbers)
            return key % self.size
        else:
            # For TelephoneRecord objects or other types
            if hasattr(key, 'tel_no'):
                return key.tel_no % self.size
            else:
                return hash(key) % self.size
                
    def secondary_hash(self, key):
        """Secondary hash function for double hashing"""
        if isinstance(key, str):
            return 7 - (sum(ord(c) for c in key) % 7)
        elif isinstance(key, int):
            return 7 - (key % 7)
        else:
            if hasattr(key, 'tel_no'):
                return 7 - (key.tel_no % 7)
            else:
                return 7 - (hash(key) % 7)
    
    def insert(self, key, value=None):
        """Insert a key-value pair or just a key into the hash table"""
        # Create a record if both key and value are provided
        record = TelephoneRecord(key, value) if value is not None else key
        index = self.hash_function(record if value is None else key)
        
        # Use the appropriate collision handling method
        if self.method == "separate_chaining":
            self._insert_chaining(index, record)
            return True
        elif self.method == "linear_probing":
            return self._insert_linear_probing(index, record)
        elif self.method == "quadratic_probing":
            return self._insert_quadratic_probing(index, record)
        elif self.method == "double_hashing":
            return self._insert_double_hashing(index, record)
    
    def _insert_chaining(self, index, record):
        """Insert using separate chaining"""
        # Check if key already exists (for TelephoneRecord objects)
        if hasattr(record, 'name'):
            for i, item in enumerate(self.table[index]):
                if hasattr(item, 'name') and item.name == record.name:
                    self.table[index][i] = record  # Update existing record
                    return
        # If key doesn't exist or we're not checking, append to the chain
        self.table[index].append(record)
    
    def _insert_linear_probing(self, index, record):
        """Insert using linear probing"""
        original_index = index
        
        while self.table[index] is not None:
            # If key exists, update the value (for TelephoneRecord objects)
            if hasattr(record, 'name') and hasattr(self.table[index], 'name'):
                if self.table[index].name == record.name:
                    self.table[index] = record
                    return True
            
            # Linear probe to next position
            index = (index + 1) % self.size
            
            # If we've checked all positions, table is full
            if index == original_index:
                print("Hash table is full!")
                return False
                
        self.table[index] = record
        return True
    
    def _insert_quadratic_probing(self, index, record):
        """Insert using quadratic probing"""
        original_index = index
        j = 1
        
        while self.table[index] is not None:
            # If key exists, update the value (for TelephoneRecord objects)
            if hasattr(record, 'name') and hasattr(self.table[index], 'name'):
                if self.table[index].name == record.name:
                    self.table[index] = record
                    return True
            
            # Quadratic probe to next position
            index = (original_index + (j * j)) % self.size
            j += 1
            
            # Prevent infinite loop
            if j > self.size:
                print("Hash table is full or cannot find an empty slot!")
                return False
                
        self.table[index] = record
        return True
    
    def _insert_double_hashing(self, index, record):
        """Insert using double hashing"""
        original_index = index
        second_hash = self.secondary_hash(record if isinstance(record, (int, str)) else 
                                         record.name if hasattr(record, 'name') else record.tel_no)
        
        j = 0
        
        while self.table[index] is not None:
            # If key exists, update the value (for TelephoneRecord objects)
            if hasattr(record, 'name') and hasattr(self.table[index], 'name'):
                if self.table[index].name == record.name:
                    self.table[index] = record
                    return True
            
            # Use double hashing formula
            j += 1
            index = (original_index + j * second_hash) % self.size
            
            # Prevent infinite loop
            if j >= self.size:
                print("Hash table is full or cannot find an empty slot!")
                return False
                
        self.table[index] = record
        return True
    
    def search(self, key):
        """Search for a key in the hash table and return the record"""
        self.comparison_count = 0  # Reset comparison counter
        index = self.hash_function(key)
        
        if self.method == "separate_chaining":
            return self._search_chaining(index, key)
        elif self.method == "linear_probing":
            return self._search_linear_probing(index, key)
        elif self.method == "quadratic_probing":
            return self._search_quadratic_probing(index, key)
        elif self.method == "double_hashing":
            return self._search_double_hashing(index, key)
            
    def _search_chaining(self, index, key):
        """Search using separate chaining"""
        # Search through the chain at the hashed index
        for item in self.table[index]:
            self.comparison_count += 1
            
            # Check if we found our item
            if isinstance(key, str) and hasattr(item, 'name') and item.name == key:
                return item, self.comparison_count
            elif isinstance(key, int) and hasattr(item, 'tel_no') and item.tel_no == key:
                return item, self.comparison_count
            elif item == key:  # Direct comparison for other types
                return item, self.comparison_count
                
        return None, self.comparison_count
        
    def _search_linear_probing(self, index, key):
        """Search using linear probing"""
        original_index = index
        
        while self.table[index] is not None:
            self.comparison_count += 1
            
            # Check if we found our item
            if isinstance(key, str) and hasattr(self.table[index], 'name') and self.table[index].name == key:
                return self.table[index], self.comparison_count
            elif isinstance(key, int) and hasattr(self.table[index], 'tel_no') and self.table[index].tel_no == key:
                return self.table[index], self.comparison_count
            elif self.table[index] == key:  # Direct comparison
                return self.table[index], self.comparison_count
                
            # Linear probe to next position
            index = (index + 1) % self.size
            
            # If we've checked all positions, item not found
            if index == original_index:
                break
                
        return None, self.comparison_count
        
    def _search_quadratic_probing(self, index, key):
        """Search using quadratic probing"""
        original_index = index
        j = 0
        checked_positions = set()
        
        while True:
            # Calculate position using quadratic probing
            probe_index = (original_index + (j * j)) % self.size
            
            # If we've already checked this position or checked too many positions
            if probe_index in checked_positions or len(checked_positions) >= self.size:
                break
                
            checked_positions.add(probe_index)
            
            # If position is empty, item not found
            if self.table[probe_index] is None:
                j += 1
                continue
                
            self.comparison_count += 1
            
            # Check if we found our item
            if isinstance(key, str) and hasattr(self.table[probe_index], 'name') and self.table[probe_index].name == key:
                return self.table[probe_index], self.comparison_count
            elif isinstance(key, int) and hasattr(self.table[probe_index], 'tel_no') and self.table[probe_index].tel_no == key:
                return self.table[probe_index], self.comparison_count
            elif self.table[probe_index] == key:  # Direct comparison
                return self.table[probe_index], self.comparison_count
                
            j += 1
            
        return None, self.comparison_count
        
    def _search_double_hashing(self, index, key):
        """Search using double hashing"""
        original_index = index
        second_hash = self.secondary_hash(key)
        j = 0
        
        # Keep track of positions we've checked to avoid infinite loop
        checked_positions = set()
        
        while True:
            # Calculate position using double hashing
            probe_index = (original_index + j * second_hash) % self.size
            
            # If we've already checked this position or checked too many positions
            if probe_index in checked_positions or len(checked_positions) >= self.size:
                break
                
            checked_positions.add(probe_index)
            
            # If position is empty, item not found
            if self.table[probe_index] is None:
                j += 1
                continue
                
            self.comparison_count += 1
            
            # Check if we found our item
            if isinstance(key, str) and hasattr(self.table[probe_index], 'name') and self.table[probe_index].name == key:
                return self.table[probe_index], self.comparison_count
            elif isinstance(key, int) and hasattr(self.table[probe_index], 'tel_no') and self.table[probe_index].tel_no == key:
                return self.table[probe_index], self.comparison_count
            elif self.table[probe_index] == key:  # Direct comparison
                return self.table[probe_index], self.comparison_count
                
            j += 1
            
        return None, self.comparison_count
    
    def display(self):
        """Display all entries in the hash table"""
        print("\n" + "="*50)
        print(f"HASH TABLE ({self.method})")
        print("="*50)
        print("Index\tContent")
        print("-"*50)
        
        for i in range(self.size):
            if self.method == "separate_chaining":
                if not self.table[i]:  # Empty chain
                    print(f"{i}\t-")
                else:
                    print(f"{i}\t", end="")
                    for j, item in enumerate(self.table[i]):
                        if j > 0:
                            print(" -> ", end="")
                        print(f"{item}", end="")
                    print()
            else:  # For probing methods
                if self.table[i] is None:
                    print(f"{i}\t-")
                else:
                    print(f"{i}\t{self.table[i]}")
        print("="*50)
    
    def stats(self):
        """Display statistics about the hash table"""
        count = 0
        empty = 0
        
        if self.method == "separate_chaining":
            chains = []
            for i in range(self.size):
                chain_length = len(self.table[i])
                chains.append(chain_length)
                count += chain_length
                if chain_length == 0:
                    empty += 1
            
            print("\n" + "="*50)
            print(f"HASH TABLE STATISTICS ({self.method})")
            print("="*50)
            print(f"Total entries: {count}")
            print(f"Empty buckets: {empty} ({empty/self.size*100:.1f}%)")
            print(f"Average chain length: {sum(chains)/self.size:.2f}")
            print(f"Max chain length: {max(chains)}")
            print("="*50)
        else:
            for i in range(self.size):
                if self.table[i] is not None:
                    count += 1
                else:
                    empty += 1
            
            print("\n" + "="*50)
            print(f"HASH TABLE STATISTICS ({self.method})")
            print("="*50)
            print(f"Total entries: {count}")
            print(f"Empty slots: {empty} ({empty/self.size*100:.1f}%)")
            print(f"Load factor: {count/self.size:.2f}")
            print("="*50)


class TelephoneDirectory:
    """Unified telephone directory application"""
    
    def __init__(self, size=100):
        self.size = size
        self.hashtables = {
            "separate_chaining": HashTable(size, "separate_chaining"),
            "linear_probing": HashTable(size, "linear_probing"),
            "quadratic_probing": HashTable(size, "quadratic_probing"),
            "double_hashing": HashTable(size, "double_hashing")
        }
        self.current_method = None
    
    def set_method(self, method):
        """Set the current collision handling method"""
        if method in self.hashtables:
            self.current_method = method
            return True
        else:
            print(f"Invalid method: {method}")
            return False
    
    def insert(self, name, tel_no):
        """Insert a record into all hash tables"""
        success = True
        for method, hashtable in self.hashtables.items():
            if not hashtable.insert(name, tel_no):
                print(f"Failed to insert using {method}")
                success = False
        return success
    
    def search(self, key, compare_methods=False):
        """Search for a record in the hash tables"""
        if compare_methods:
            print("\n" + "="*60)
            print("COMPARISON OF COLLISION HANDLING METHODS")
            print("="*60)
            print("Method\t\t\tResult\tComparisons")
            print("-"*60)
            
            for method, hashtable in self.hashtables.items():
                result, comparisons = hashtable.search(key)
                status = "Found" if result else "Not found"
                print(f"{method:<20}\t{status}\t{comparisons}")
            
            print("="*60)
            return None
        elif self.current_method:
            result, comparisons = self.hashtables[self.current_method].search(key)
            if result:
                print(f"\nRecord found using {self.current_method}:")
                print(f"{result} (required {comparisons} comparisons)")
            else:
                print(f"\nRecord not found using {self.current_method} ({comparisons} comparisons made)")
            return result
        else:
            print("No method selected. Use set_method() first.")
            return None
    
    def display(self, method=None):
        """Display the hash table for the specified method"""
        if method:
            if method in self.hashtables:
                self.hashtables[method].display()
            else:
                print(f"Invalid method: {method}")
        elif self.current_method:
            self.hashtables[self.current_method].display()
        else:
            print("No method selected. Use set_method() or specify a method.")
    
    def stats(self, method=None):
        """Display statistics for the specified method"""
        if method:
            if method in self.hashtables:
                self.hashtables[method].stats()
            else:
                print(f"Invalid method: {method}")
        elif self.current_method:
            self.hashtables[self.current_method].stats()
        else:
            print("No method selected. Use set_method() or specify a method.")
    
    def compare_methods(self):
        """Compare all collision handling methods"""
        for method, hashtable in self.hashtables.items():
            hashtable.stats()


def run_demo():
    """Run a demonstration of the telephone directory"""
    print("="*60)
    print("TELEPHONE DIRECTORY DEMONSTRATION")
    print("="*60)
    
    # Create a telephone directory with size 10
    directory = TelephoneDirectory(10)
    
    # Sample data
    sample_data = [
        ("Alice", 1234567890),
        ("Bob", 9876543210),
        ("Charlie", 5551234567),
        ("David", 6667778888),
        ("Eve", 1112223333),
        ("Frank", 4445556666),
        ("Grace", 7778889999),
    ]
    
    # Insert sample data
    print("Inserting sample data...")
    for name, tel_no in sample_data:
        directory.insert(name, tel_no)
    
    # Display all methods
    for method in directory.hashtables.keys():
        directory.display(method)
    
    # Search and compare methods
    print("\nSearching for 'Charlie'...")
    directory.search("Charlie", compare_methods=True)
    
    print("\nSearching for 'Zoe' (not in directory)...")
    directory.search("Zoe", compare_methods=True)
    
    # Show statistics
    for method in directory.hashtables.keys():
        directory.stats(method)


def main():
    """Main interactive function"""
    print("="*60)
    print("TELEPHONE DIRECTORY APPLICATION")
    print("="*60)
    
    size = int(input("Enter the size of the hash table (default 100): ") or 100)
    directory = TelephoneDirectory(size)
    
    # Set default method
    directory.set_method("separate_chaining")
    
    while True:
        print("\n" + "="*40)
        print("MENU")
        print("="*40)
        print("1. Insert a telephone record")
        print("2. Search for a record")
        print("3. Display the hash table")
        print("4. Compare collision handling methods")
        print("5. Change collision handling method")
        print("6. Show statistics")
        print("7. Run demonstration")
        print("8. Exit")
        print("="*40)
        
        choice = input("Enter your choice (1-8): ")
        
        if choice == '1':
            name = input("Enter name: ")
            try:
                tel_no = int(input("Enter telephone number (digits only): "))
                directory.insert(name, tel_no)
                print(f"Record inserted: {name}: {tel_no}")
            except ValueError:
                print("Invalid telephone number. Please enter digits only.")
        
        elif choice == '2':
            search_type = input("Search by name or number? (n/num): ").lower()
            if search_type.startswith('n'):
                key = input("Enter name to search: ")
            else:
                try:
                    key = int(input("Enter number to search: "))
                except ValueError:
                    print("Invalid telephone number. Please enter digits only.")
                    continue
            
            compare = input("Compare all methods? (y/n): ").lower().startswith('y')
            directory.search(key, compare_methods=compare)
        
        elif choice == '3':
            directory.display()
        
        elif choice == '4':
            directory.compare_methods()
        
        elif choice == '5':
            print("\nAvailable methods:")
            for i, method in enumerate(directory.hashtables.keys(), 1):
                print(f"{i}. {method}")
            
            try:
                method_choice = int(input("Select method (1-4): "))
                methods = list(directory.hashtables.keys())
                directory.set_method(methods[method_choice-1])
                print(f"Method changed to {methods[method_choice-1]}")
            except (ValueError, IndexError):
                print("Invalid choice.")
        
        elif choice == '6':
            directory.stats()
        
        elif choice == '7':
            run_demo()
        
        elif choice == '8':
            print("Thank you for using the Telephone Directory!")
            break
        
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()