## Hashtables

### Implemntation
Typically, use an array of length N as underlying storage unit. Use a hashing function to determine which index to place the value. Good hashing functions will avoid collisions.

### Collision Handling
There are two ways to handle collisions:

  1. Separate Chaining
    - Each "bucket" holds a list (typically linked list) to hold all matching values.
    - Pro: No array resizing
    - Con: With bad hashing function, searching can be O(N) which defeats the purpose of using a hashtable.
  2. Open Addressing
    - Attempts to find next available bucket without value.
    - Pro: Super space efficient
    - Con: Potential resizing if hash table is too big for underlying array.

### Operations
  - Space:
    - Best: O(N)
    - Worst: O(N)
  - Search/Insert/Delete:
    - Best: O(1)
    - Worst: O(N)