# In Python, there are several ways to concatenate strings. Here are some common methods with examples:

# 1: Using the + operator:

str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)  # Output: Hello World


# 2: Using the str.join() method:

str_list = ["Hello", "World"]
result = " ".join(str_list)
print(result)  # Output: Hello World

# 3: Using formatted strings (f-strings):

str1 = "Hello"
str2 = "World"
result = f"{str1} {str2}"
print(result)  # Output: Hello World

# 4: Using the str.format() method:

str1 = "Hello"
str2 = "World"
result = "{} {}".format(str1, str2)
print(result)  # Output: Hello World

# 5: Using the += operator:

str1 = "Hello"
str1 += " World"
print(str1)  # Output: Hello World

# 6: Using the * operator for repetition:

str1 = "Hello "
result = str1 * 3
print(result)  # Output: Hello Hello Hello