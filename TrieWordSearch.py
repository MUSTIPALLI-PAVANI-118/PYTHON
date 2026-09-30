#ROLL NO.:CH.AI.U4AID25028
# Class representing one node of the Trie
class TrieNode:
    __slots__ = ("children", "is_end")

    def __init__(self):
        # Dictionary for storing child nodes
        self.children = {}

        # Indicates the end of a complete word
        self.is_end = False


# Class representing the complete Trie
class Trie:
    def __init__(self):
        # Create the root node
        self.root = TrieNode()

    # Function to insert a word
    def insert(self, word):
        current = self.root

        # Process every character
        for character in word:
            next_node = current.children.get(character)

            # Create a new node when required
            if next_node is None:
                next_node = TrieNode()
                current.children[character] = next_node

            current = next_node

        # Mark the end of the complete word
        current.is_end = True

    # Function to find the node of a word or prefix
    def find_node(self, text):
        current = self.root

        # Follow the path of every character
        for character in text:
            current = current.children.get(character)

            # Return None if the path does not exist
            if current is None:
                return None

        return current

    # Function to search for a complete word
    def search(self, word):
        final_node = self.find_node(word)

        return (
            final_node is not None
            and final_node.is_end
        )

    # Function to check whether a prefix exists
    def starts_with(self, prefix):
        return self.find_node(prefix) is not None


# Create an empty Trie
trie = Trie()

# Read the number of words
n = int(input("Enter the number of words: "))

print("Enter", n, "words:")

# Read and insert N words
for index in range(1, n + 1):
    word = input(
        f"Enter word {index}: "
    ).strip()

    trie.insert(word)

# Read the word to be searched
search_word = input(
    "Enter the word to search: "
).strip()

# Read the prefix to be checked
prefix = input(
    "Enter the prefix to check: "
).strip()

print("\nSearch Results:")

# Display the word-search result
if trie.search(search_word):
    print("Word found")
else:
    print("Word not found")

# Display the prefix-search result
if trie.starts_with(prefix):
    print("Prefix found")
else:
    print("Prefix not found")