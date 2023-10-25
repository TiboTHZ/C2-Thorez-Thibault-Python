num_words = 0

with open("7texte.txt", 'r') as f:
    for line in f:
        words = line.split()
        num_words += len(words)

result = open("myfile.txt", "x")
result.write(str(num_words))