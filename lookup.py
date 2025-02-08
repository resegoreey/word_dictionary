#words and their meanings
word_dic = {"orphic": "mysterious and entrancing, beyond ordinary understanding",
            "indelible": "impossible to to erase or forget",
            "eunoia": "pure and well balanced mind, a good spirit, beautiful thinking",
            "collywobbles": "butterflies in stomach",
            "apricity": "the warmth of the sun in winter"}

#acessing the items
lookup = input("What's the word you want to lookup? ")
word = word_dic[lookup]
print(f"{lookup} : {word}")