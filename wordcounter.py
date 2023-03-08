import string

def count_words(filename):
    # Create an empty dictionary to store the word counts
    word_counts = {}
    
    # Open the file and read the contents
    with open(filename, "r") as file:
        text = file.read()
    
    # Convert all characters to lowercase and remove punctuation
    text = text.lower().translate(str.maketrans("", "", string.punctuation))
    
    # Split the text into words and count the occurrences of each word
    words = text.split()
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    
    return word_counts

# Ask the user for the filename
filename = input("Enter the filename: ")

# Count the words and print the result
word_counts = count_words(filename)
print("Word counts:")
for word, count in word_counts.items():
    print(f"{word}: {count}")
