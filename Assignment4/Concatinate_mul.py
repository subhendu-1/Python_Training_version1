# 6️⃣ Concatenate Multiple Strings

def concatenate_strings(*args):
    return ' '.join(args)


sentence = concatenate_strings("Hello", "world,", "how", "are", "you?")
print(f"Concatenated Sentence: {sentence}")
