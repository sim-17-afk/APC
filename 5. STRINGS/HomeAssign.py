from collections import Counter

text = input("Enter a paragraph of text:\n")

# 1) Count total number of words
words = text.split()
total_words = len(words)
print("Total number of words:", total_words)

# 2) Count frequency of each word
word_freq = Counter(word.lower() for word in words)
print("Frequency of each word:")
for word, freq in word_freq.items():
    print(f"{word}: {freq}")

# 3) Top 3 most frequent words
top_3 = word_freq.most_common(3)
print("Top 3 most frequent words:")
for word, freq in top_3:
    print(f"{word}: {freq}")

# 4) Count number of vowels in the entire text
vowels = "aeiouAEIOU"
vowel_count = sum(1 for char in text if char in vowels)
print("Number of vowels in the text:", vowel_count)