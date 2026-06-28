def string_operations():
    print("\n---- STRING OPERATIONS ----")
    
    s = "Hello Python World"
    print("Original:", s)

    # Access
    print("First char:", s[0])

    # Slicing
    print("Slice [0:5]:", s[0:5])

    # Length
    print("Length:", len(s))

    # Case
    print("Upper:", s.upper())
    print("Lower:", s.lower())

    # Find
    print("Find 'Python':", s.find("Python"))

    # Replace
    print("Replace:", s.replace("Python", "Java"))

    # Split
    print("Split:", s.split())

    # Join
    print("Join:", "-".join(["Amit", "Mourya"]))

    # Check
    print("Is alpha:", s.isalpha())
    print("Starts with Hello:", s.startswith("Hello"))

string_operations()