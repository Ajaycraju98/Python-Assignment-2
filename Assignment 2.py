# Topic :List Exercise
# Q1. Create a list of 5 random numbers and print the list.
List_of_random_numbers = [1,5,10,35,50]
print("List of 5 random numbers:", List_of_random_numbers)

# Q2. Insert 3 new values to the list and print the updated list.
List_of_random_numbers .extend([60,100,101])
print("Updated list",List_of_random_numbers )

# Q3. Try to use a for loop to print each element in the list.
for i in List_of_random_numbers :
    print(i)


# Topic: Dictionary
# Exercise Q1.Create a dictionary with keys 'name', 'age', and 'address' and
# values 'John', 25, and 'New York' respectively.
New_dict= dict(name='John',age=25,address='New York')
print(New_dict)

# Q2. Add a new key-value pair to the dictionary created in Q1 with key 'phone' and value '1234567890'.
New_dict['phone']='1234567890'
print (New_dict)

# Topic: Set Exercise
# Q1.Create a set with values 1, 2, 3, 4, and 5.
new_set={1,2,3,4,5}
print("set with values",new_set)

# Q2. Add the value 6 to the set created in Q1.
new_set.add(6)
print("Add the value 6 to the set",new_set)

# Q3. Remove the value 3 from the set created in Q1.
new_set.remove(3)
print("Remove the value 3 from the set",new_set)


# Topic:Tuple Exercise
# Q1. Create a tuple with values 1, 2, 3, and 4
new_tuple=1,2,3,4
print(new_tuple)

# Q2. Print the length of the tuple created in Q1.
print(len(new_tuple))

