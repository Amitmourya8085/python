def lambda_examples():
    print("---- LAMBDA FUNCTIONS ----")

    # 1. Basic
    square = lambda x: x * x
    print("Square:", square(5))

    # 2. Multiple arguments
    add = lambda a, b: a + b
    print("Add:", add(3, 4))

    # 3. Inside function call
    print("Multiply:", (lambda x, y: x * y)(2, 3))

    # 4. With list (map)
    nums = [1, 2, 3, 4]
    squares = list(map(lambda x: x*x, nums))
    print("Squares:", squares)

    # 5. With filter
    even = list(filter(lambda x: x % 2 == 0, nums))
    print("Even numbers:", even)

    # 6. With sorting
    data = [("Amit", 19), ("Pankaj", 19)]
    data.sort(key=lambda x: x[1])
    print("Sorted by age:", data)

    # 7. Conditional lambda
    check = lambda x: "Even" if x % 2 == 0 else "Odd"
    print("Check:", check(7))

lambda_examples()