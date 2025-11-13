# algorithms
all things algorithms

Not all algorithms are created equal — some are faster than others.
To measure efficiency, we use Big O Notation, which describes how the runtime grows as the input gets larger.

| Big O        | Name        | Example                                 | Meaning                                     |
| ------------ | ----------- | --------------------------------------- | ------------------------------------------- |
| **O(1)**     | Constant    | Accessing an element in a list by index | Same time no matter how large the input     |
| **O(n)**     | Linear      | Scanning a list of names                | Time grows with input size                  |
| **O(log n)** | Logarithmic | Binary search                           | Super-efficient — halves the work each time |
| **O(n²)**    | Quadratic   | Comparing all pairs of items            | Grows very quickly — bad for large data     |


## Search algorithms 

1. linear search - Check each item in order until you find what you’re looking for.

Time Complexity:
O(n) → the more items, the longer it takes.

2. binary search - Works only on sorted lists — cut the list in half repeatedly.

Time Complexity:
O(log n) → extremely fast for large datasets.