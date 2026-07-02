my_set1 = {1, 2, 3, 4, 5}
my_set2 = {3, 4, 6, 7, 8}


print(my_set1 | my_set2)
# {1, 2, 3, 4, 5, 6, 7, 8}

print(my_set1 & my_set2)
# {3, 4}

print(my_set1 - my_set2)
# {1, 2, 5}

print(my_set1 ^ my_set2)
# {1, 2, 5, 6, 7, 8}

