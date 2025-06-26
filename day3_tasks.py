# Day 3: Working with Lists, Split/Join, and Tuples

# 📥 Taking a sentence input from the user
sentence = input("Enter a sentence: ")

# 🔹 Splitting the sentence into a list of words
words_list = sentence.split()

# 📋 Printing the list of words
print("List of words:", words_list)

# 🔗 Joining the list back into a sentence with ' - ' separator
joined_sentence = ' - '.join(words_list)
print("Joined with '-':", joined_sentence)

# 👤 Storing first and last name in a tuple
name_tuple = ("Tayab", "Ali")

# 🖨️ Printing each part of the name using indexing
print("First Name:", name_tuple[0])
print("Last Name:", name_tuple[1])
