# 4️⃣ Count the Number of Words in a Sentence

def count_words(sentence):
    words = sentence.split()
    return len(words)

sentence = "This is a sample article summary."
print(f"Word Count: {count_words(sentence)}")
