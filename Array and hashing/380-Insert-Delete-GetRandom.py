'''
Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.
'''
import random

class RandomizedSet:
    def __init__(self):
        # Dictionary to store value-to-index mapping for O(1) lookup
        self.val_to_index = {}  
        # List to store values for O(1) random access
        self.values = []  

    def insert(self, val: int) -> bool:
        # If the value already exists, return False
        if val in self.val_to_index:
            return False
        # Store the index of the new value
        self.val_to_index[val] = len(self.values)
        # Append the new value to the list
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        # If the value does not exist, return False
        if val not in self.val_to_index:
            return False
        
        # Get the index of the value to remove
        index_to_remove = self.val_to_index[val]
        # Get the last value in the list
        last_val = self.values[-1]
        
        # Move the last value to the position of the value to remove
        self.values[index_to_remove] = last_val
        # Update the dictionary with the new index of the last value
        self.val_to_index[last_val] = index_to_remove
        
        # Remove the last element from the list
        self.values.pop()
        # Remove the value from the dictionary
        del self.val_to_index[val]
        
        return True

    def getRandom(self) -> int:
        # Return a random element from the list
        return random.choice(self.values)

# Example usage:
# obj = RandomizedSet()
# print(obj.insert(1))  # True, as 1 is inserted
# print(obj.remove(2))  # False, as 2 is not present
# print(obj.insert(2))  # True, as 2 is inserted
# print(obj.getRandom())  # Randomly returns 1 or 2
# print(obj.remove(1))  # True, as 1 is removed
# print(obj.getRandom())  # Returns 2, as it's the only element left