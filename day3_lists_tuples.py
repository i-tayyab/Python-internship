#TASK 1

sentence = input("Enter a sentence: ")

#Splitting the sentence into a list of words
words_list = sentence.split()

#Printing the list of words
print("List of words:", words_list)

#Joining the list back into a sentence with ' - ' separator
joined_sen = ' - '.join(words_list)
print("Joined with '-':", joined_sen)


TASK 2
# Storing first and last name in a tuple
tuple = ("Tayab", "Bahir")

# Printing each part of the name using indexing
print("First Name:", tuple[0])
print("Last Name:", tuple[1])
