def dict_operations():
    print("\n---- DICTIONARY OPERATIONS ----")
    
    d = {"name": "Amit", "age": 18, "city": "Boisar"}
    print("Original:", d)

    # Access
    print("Name:", d["name"])
    print("Age (get):", d.get("age"))

    # Add/Update
    d["email"] = "amit@gmail.com"
    d["age"] = 18
    print("After update:", d)

    # Remove
    d.pop("city")
    print("After pop:", d)

    # Keys, Values, Items
    print("Keys:", d.keys())
    print("Values:", d.values())
    print("Items:", d.items())

    # Loop
    for k, v in d.items():
        print(k, ":", v)

    # Copy
    new_d = d.copy()
    print("Copy:", new_d)

dict_operations()