my_tuple = ("Junior", "Middle", "Senior", [1, 2, 3])

my_tuple[-1].append(4)

print(my_tuple)
# ('Junior', 'Middle', 'Senior', [1, 2, 3, 4])

my_tuple1 = ("Junior", "Middle", "Senior")

junior, middle, senior = my_tuple1

print(junior)
print(middle)
print(senior)

# Junior
# Middle
# Senior


# remove duplicates using a set
{'python', 'c++', 'javascript'}


languages = ["python", "javascript", "c++", "c++"]
print(languages)
unique_languages = set(languages)
print(unique_languages)

# ['python', 'javascript', 'c++', 'c++']
# {'python', 'c++', 'javascript'}


#ADD & remove
languages1 = {"python", "JS", "C++"}
languages1.remove("JS")
languages1.add("java")
print(languages1)

# {'C++', 'python', 'java'}