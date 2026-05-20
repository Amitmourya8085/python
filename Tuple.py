def tuple_operations():
    print("\n---- TUPLE OPERATIONS ----")
    
    tup = (10, 20, 30, 40, 20)
    print("Original:", tup)

    # Access
    print("First:", tup[0])

    # Slicing
    print("Slice:", tup[1:4])

    # Count
    print("Count of 20:", tup.count(20))

    # Index
    print("Index of 30:", tup.index(30))

    # Length
    print("Length:", len(tup))

    # Convert
    lst = list(tup)
    print("Tuple to list:", lst)

tuple_operations()