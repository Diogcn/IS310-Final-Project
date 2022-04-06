
# Step 1:
input_file = open("PrideandPrejudice.txt","r")
jane = input_file.read()
input_file.close()
  
# Step 2:
jane_cleaned = jane.split('\ufeffThe Project Gutenberg eBook of Pride and Prejudice, by Jane Austen\n\nThis eBook is for the use of anyone anywhere in the \
United States and\nmost other parts of the world at no cost and with almost no restrictions\nwhatsoever. You may copy it, give it away or re-use it under the \
terms\nof the Project Gutenberg License included with this eBook or online at\nwww.gutenberg.org. If you are not located in the United States, you\nwill have to \
check the laws of the country where you are located before\nusing this eBook.\n\nTitle: Pride and Prejudice\n\nAuthor: Jane Austen\n\nRelease Date: June, 1998 \
[eBook #1342]\n[Most recently updated: August 23, 2021]\n\nLanguage: English\n\nCharacter set encoding: UTF-8\n\n')
jane_cleaned = ''.join(jane_cleaned[1])

# Step 3:
jane_cleaned = jane_cleaned.replace("man","person").replace("wife","partner")
print(jane_cleaned)

# Step 4:
print('Enter a word to replace (Case Sensitive):')
word_r = input()
print('Enter a new word to replace with:')
word_n = input()
jane_cleaned = jane_cleaned.replace(word_r, word_n)
print('Text file has been altered. Check directory for altered file.')

with open("PrideandPrejudice_Alt.txt", "w") as output_file:
   output_file.write(jane_cleaned)
