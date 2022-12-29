words = ['aha', 'area', 'bulbs', 'chic', 'dad', 'wow', 'tact', 'pulp', 'pump', 'mom']
for word in words:
    if len(word) == 3:
        if word[0] == word[2]:
            print(word)