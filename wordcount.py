import sys

def snip_special_characters(word):

    word_new = ""
    for char in word:
        if char.isalpha() or char == "-":
            word_new += char
    return word_new



file_handler = open(str(sys.argv[1]))
word_counts = {}

for line in file_handler:
    line = line.rstrip()
    words = line.split(" ")

    for word in words:
        word = word.lower()
        word = snip_special_characters(word)
        word_counts[word] = word_counts.get(word,0) + 1
    
print word_counts        




