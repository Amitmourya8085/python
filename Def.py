def unique_functions():
    print("\n---- UNIQUE FUNCTION USAGE ----")

    # Default argument
    def greet(name="Guest"):
        print("Hello", name)

    greet()
    greet("Amit")

    # *args
    def add_all(*nums):
        return sum(nums)

    print("Sum:", add_all(1, 2, 3, 4))

    # **kwargs
    def print_info(**data):
        for k, v in data.items():
            print(k, ":", v)

    print_info(name="Amit", age=18)

    # Lambda
    square = lambda x: x * x
    print("Square:", square(5))

    # Function inside function
    def outer():
        def inner():
            print("Inner function")
        inner()

    outer()

unique_functions()