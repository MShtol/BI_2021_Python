import matplotlib.pyplot as plt
import re
# 1 Parse all frp links from file
with open('references.txt') as f:
    lines = f.read()
pattern = re.compile(r'[;\s](ftp[^;\s]+)')
match = pattern.findall(lines)
with open('ftps', 'w') as ftps:
    ftps.write('\n'.join(match))
# 2 find all numbers
with open('2430AD.txt') as file:
    text = file.read()
pattern = re.compile(r'\b[\d]+\.*\d*\b')
all_numbers = pattern.findall(text)
# 2430 1969 2430 2430 57 57 1970 3.68 35 460 2430
# 3 find all words with A or a in it
pattern = re.compile(r'\b\S*[aA]\S*\b')  # A.D is provided without second dot
all_a_words = pattern.findall(text)
# len(all_a_words) == 983
# 4 Find all wxclamation sentences
pattern = re.compile(r'[A-Z][^\.!?]*!')
all_exclamations = pattern.findall(text)
# Yes! Literally! There was once a time! Centuries ago! Think, Cranwitz! If we succeed!
# 5 Plot distribution of number of uniqe words by word length
# A.D and J.B are proveded without second dot
pattern = re.compile(r'\b[\S]+\b')
all_words = pattern.findall(text.lower())
unique_words = set(all_words)
distr = {}
print(len(unique_words))
for i in unique_words:
    length = len(i)
    if length in distr:
        distr[length] += 1
    else:
        distr[length] = 1
plt.bar(distr.keys(), distr.values(), color='purple')
plt.xticks(list(distr.keys()))
plt.title('Unique word length distribution')
plt.xlabel('Word length')
plt.ylabel('Unique word number')
plt.show()
