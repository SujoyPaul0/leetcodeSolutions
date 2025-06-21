class TrieNode:
    def __init__(self):
        """
        Initializes a Trie node with an array of 26 children (for each lowercase English letter)
        and a boolean flag 'end' to indicate if the node marks the end of a word.
        """
        self.children = [None] * 26  # Array to hold references to child nodes (for 'a' to 'z')
        self.end = False  # Marks if this node represents the end of a word


class Trie:
    def __init__(self):
        """
        Initialize the Trie data structure with a root TrieNode.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the Trie character by character.
        """
        curr = self.root
        for c in word:
            i = ord(c) - ord("a")  # Convert character to index (0-25)
            if curr.children[i] is None:
                curr.children[i] = TrieNode()  # Create a new node if it doesn't exist
            curr = curr.children[i]  # Move to the next node
        curr.end = True  # Mark the last node as the end of a valid word

    def search(self, word: str) -> bool:
        """
        Searches for a word in the Trie and returns True if it exists, False otherwise.
        """
        curr = self.root
        for c in word:
            i = ord(c) - ord("a")  # Convert character to index
            if curr.children[i] is None:
                return False  # If node does not exist, the word is not present
            curr = curr.children[i]
        return curr.end  # Return True if it's marked as the end of a word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns True if any word in the Trie starts with the given prefix, False otherwise.
        """
        curr = self.root
        for c in prefix:
            i = ord(c) - ord("a")  # Convert character to index
            if curr.children[i] is None:
                return False  # If a node is missing, no word starts with this prefix
            curr = curr.children[i]
        return True  # If traversal is successful, a word with this prefix exists
    
# Implement Trie