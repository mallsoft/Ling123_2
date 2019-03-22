from collections import Counter

noun = ["NOUN","PRON","PROPN"]
punctuation = ["PUNCT"]

# opening the given file 'pos_input.txt'
file = open("pos_input.txt",mode="r",encoding="utf-8")

# read the text and split into tuples
text = list(
        (elements.split("/")[0],elements.split("/")[1])
        for elements in file.read().split()
        )

# make a match list
# ie. if PUNCT and (then)NOUN add it, else pass. 
text_freq = list()
previous_tupl = None
for i,tupl in enumerate(text):
    if tupl[1] in noun and previous_tupl and previous_tupl[1] in punctuation:
            text_freq.append((previous_tupl,tupl))
    previous_tupl = tupl

# count the things!
text_freq = Counter(text_freq)

# print each on a separate line
for element,count in text_freq.items():
        print(element,count)
