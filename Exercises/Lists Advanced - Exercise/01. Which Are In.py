# 1.	Which Are In?
# Given two lists of strings print a new list of the strings that contains words from the first list which are
# substrings of any of the strings in the second list (only unique values)
# Input
# There will be 2 lines of input: the two lists separated by ", "
# Output
# Print the resulting list on the console
# Input                                                         Output
# arp, live, strong                                             ['arp', 'live', 'strong']
# lively, alive, harp, sharp, armstron


search_words = input().split(", ")
words = input().split(", ")
result = []
for search_word in search_words:
    for word in words:
        if search_word in word and search_word not in result:
            result.append(search_word)
print(result)
