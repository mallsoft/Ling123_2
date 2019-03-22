
# opening the given file 'ttr_input'
file = open("ttr_input.txt",mode="r",encoding="utf-8")
# read the text and split on \s
text = file.read().split()

# types / unique words / set
word_set = len(set(text))
print(f"types: {word_set}")
# tokens / number of words in the text / list
word_list = len(text)
print(f"tokens: {word_list}")

# calculate the TTR 'type token ratio'
ratio = (word_set / word_list) * 100

# print the result
print(f"ratio = {ratio}")