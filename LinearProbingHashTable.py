#ROLL NO.CH.AI.U4AID25028
# Function to insert a key using linear probing
def insert_key(hash_table, key):
    table_size = len(hash_table)

    # Calculate the initial hash index
    start_index = key % table_size

    # Check at most table_size positions
    for step in range(table_size):
        # Calculate the next index using linear probing
        index = (start_index + step) % table_size

        # Insert the key if the position is empty
        if hash_table[index] is None:
            hash_table[index] = key
            return True

    # No empty position was found
    return False


# Function to search for a key
def search_key(hash_table, key):
    table_size = len(hash_table)

    # Calculate the initial hash index
    start_index = key % table_size

    # Check at most table_size positions
    for step in range(table_size):
        # Calculate the next index
        index = (start_index + step) % table_size

        # An empty position means the key is absent
        if hash_table[index] is None:
            return -1

        # Return the index when the key is found
        if hash_table[index] == key:
            return index

    # The complete table was checked
    return -1


# Read the number of keys and table size
n, table_size = map(
    int,
    input(
        "Enter the number of keys and table size: "
    ).split()
)

# Validate the table size
if table_size <= 0:
    print("Hash table size must be greater than zero.")

else:
    # Read all the keys
    keys = list(
        map(
            int,
            input("Enter the keys: ").split()
        )
    )

    # Check whether exactly N keys were entered
    if len(keys) != n:
        print("Please enter exactly", n, "keys.")

    # The number of keys must not exceed table size
    elif n > table_size:
        print(
            "Number of keys cannot exceed table size."
        )

    else:
        # Create an empty hash table
        hash_table = [None] * table_size

        # Insert all the keys
        for key in keys:
            inserted = insert_key(hash_table, key)

            if not inserted:
                print(
                    "Hash table is full. "
                    "Cannot insert:",
                    key
                )
                break

        # Read the key to be searched
        search_value = int(
            input("Enter the key to search: ")
        )

        # Prepare values for display
        display_values = [
            "-" if value is None else value
            for value in hash_table
        ]

        # Display the final hash table
        print("\nHash Table:")
        print("Index:", *range(table_size))
        print("Value:", *display_values)

        # Search for the given key
        position = search_key(
            hash_table,
            search_value
        )

        # Display the search result
        if position != -1:
            print(
                "\nKey found at index",
                position
            )
        else:
            print("\nKey not found")