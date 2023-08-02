#Ask for plain text sentence 
org_sentence = input("Please enter the original sentence")

#Create dictionary for casear cipher translations
caser_cipher = {
    'A': 'F', 'B': 'G', 'C': 'H', 'D': 'I', 'E': 'J', 'F': 'K', 'G': 'L', 'H': 'M',
    'I': 'N', 'J': 'O', 'K': 'P', 'L': 'Q', 'M': 'R', 'N': 'S', 'O': 'T', 'P': 'U',
    'Q': 'V', 'R': 'W', 'S': 'X', 'T': 'Y', 'U': 'Z', 'V': 'A', 'W': 'B', 'X': 'C',
    'Y': 'D', 'Z': 'E',
    'a': 'f', 'b': 'g', 'c': 'h', 'd': 'i', 'e': 'j', 'f': 'k', 'g': 'l', 'h': 'm',
    'i': 'n', 'j': 'o', 'k': 'p', 'l': 'q', 'm': 'r', 'n': 's', 'o': 't', 'p': 'u',
    'q': 'v', 'r': 'w', 's': 'x', 't': 'y', 'u': 'z', 'v': 'a', 'w': 'b', 'x': 'c',
    'y': 'd', 'z': 'e'
}

#Create a new list to store all translated variables 
translated_list = []
#Iterate through each character in the original sentence by using a loop 
for char in org_sentence:
    if char in caser_cipher:
        translated_list.append(caser_cipher[char])
    else: 
        translated_sentence.append(char)
    
# Join the characters in the list to form the translated sentence
translated_sentence = "".join(translated_list)

# Print the translated sentence
print("Translated Sentence:", translated_sentence)