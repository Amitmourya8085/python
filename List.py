def list_operations():
    print("---- LIST OPERATIONS ----")
    
    lst = [10, 20, 30, 40, 50]
    print("Original:", lst)

    # Access
    print("First element:", lst[0])
    print("Last element:", lst[-1])

    # Slicing
    print("Slice [1:4]:", lst[1:4])
    print("Reverse:", lst[::-1])

    # Add
    lst.append(60)
    print("After append:", lst)

    lst.insert(1, 15)
    print("After insert:", lst)

    lst.extend([70, 80])
    print("After extend:", lst)

    # Remove
    lst.remove(30)
    print("After remove:", lst)

    popped = lst.pop()
    print("Popped:", popped)

    # Update
    lst[0] = 100
    print("After update:", lst)

    # Search
    print("Index of 40:", lst.index(40))

    # Count
    print("Count of 20:", lst.count(20))

    # Sort
    lst.sort()
    print("Sorted:", lst)

    lst.reverse()
    print("Reversed:", lst)

    # Copy
    new_lst = lst.copy()
    print("Copy:", new_lst)

list_operations()