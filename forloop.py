# basic Syntax 
# for item in iterable:
#    block of code

#range(stop),range(start,stop,step)
print("for range(5)")
for n in range(5):
    print(f"iteration{n}")

print(" for range(1,10,2)")

for n in range(1,10,2):
    print(f"iteration{n}")

fruits_list=["apple","banana","mango"]
num_tuple=(12,3,4)

print('for List :')
for fruits in fruits_list:
    print(fruits)
print('for tuple:')
for num in num_tuple:
    print(num)

user_profile={
    "name":"amit",
    "role":"student"
}
print('for dict: ')
for value in user_profile:
    print(value)
for key in user_profile:
    print(key)
for key,value in user_profile.items():
    print(f"{key}:{value}")

print('for enumerate: ')
lang=["c++","java","rust"]
for index,langs in enumerate(lang) :
    print(f"{index}.{langs}")

print('for zip')
lst1=["amit","deepak"]
lst2=[12,3,4]
for name,score in zip(lst1,lst2):
    print(f"{name}:{score}")

square=[x**2 for x in range(5)]
print(square)
