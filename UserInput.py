# Number of words
n = int(input("How many words do you want to enter? "))

words = []

# Get words from the user
for i in range(n):
    word = input(f"Enter word {i + 1}: ")
    words.append(word)

# Convert the list of words into a sentence
sentence = " ".join(words)

# Display the sentence
print("\nThe sentence is:")
print(sentence)