# Two strings are considered close if you can attain one from the other using the following operations:

# Operation 1: Swap any two existing characters.
# For example, abcde -> aecdb
# Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
# For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
# You can use the operations on either string as many times as necessary.

# Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

def closeStrings(word1, word2):
    if len(word1) != len(word2) or set(word1) != set(word2):
        return False
    if word1 == word2:
        return True
    return sorted(Counter(word1).values()) == sorted(Counter(word2).values())

def Counter(word):
    count = {}
    for char in word:
        if char not in count:
            count[char] = 1
        else:
            count[char] += 1
    return count

if __name__ == "__main__":
    print(closeStrings("abc", "bca")) # True
    print(closeStrings("a", "aa")) # False
    print(closeStrings("cabbba", "abbccc")) # True
    print(closeStrings("cabbba", "aabbss")) # False
    print(closeStrings("uau", "ssx")) # False
    print(closeStrings("cabbba", "aabbss")) # False