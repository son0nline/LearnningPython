text = """Education is not the learning of facts
but the training of the mind to think

– Albert Einstein"""
prepositions = {"as", "but", "by", "down", "for", "in", "of", "on", "to", "with"}

# Add your code here.
wordsSet = set(text.split())

used_prepositions = prepositions & wordsSet
print(used_prepositions)
