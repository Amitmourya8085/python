fruits = {'apple', 'apple', 'bananna', 'mango'}
print(fruits) 
# Output: {'mango', 'bananna', 'apple'} (Duplicates removed)

skill = {'java', 'c++', 'python', 'ALP8085', 'mysql', 'docker'}
skill.add('c')
skill.update(['git']) # <-- Fixed: Wrapped 'git' in a list
skill.pop()
skill.discard('aws') # Safe! Does nothing since 'aws' isn't there
print(skill)
# Output: {'java', 'c++', 'python', 'ALP8085', 'mysql', 'docker', 'c', 'git'}

devs = {"Alice", "Bob", "Charlie"}
managers = {"Bob", "David"}

# Union: Everyone in the company
everyone = devs | managers # {'Alice', 'Bob', 'Charlie', 'David'}

# Intersection: People who are both devs and managers
tech_leads = devs & managers # {'Bob'}

# Difference: Devs who are NOT managers
pure_devs = devs - managers # {'Alice', 'Charlie'}

# Symmetric Difference: People with only ONE role
one_role = devs ^ managers # {'Alice', 'Charlie', 'David'}

# Create a set of squares for even numbers
evens_squared = {x**2 for x in range(10) if x % 2 == 0}
print(evens_squared) # {0, 16, 64, 4, 36}

a = {1, 2}
b = {1, 2, 3, 4}

print(a.issubset(b))    # True (All elements of a are in b)
print(b.issuperset(a))  # True (b contains all elements of a)
print(a.isdisjoint(b))  # False (They share elements)
