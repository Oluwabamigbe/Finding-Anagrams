def find_anagram(word, anagram):
    # [assignment] Add your code here
    x = []
    for i in word:
        y = i in anagram
        x.append(y)

    if (False in x):
        return False
    else:
        return True
        
print(find_anagram('elbow', 'hello'))

