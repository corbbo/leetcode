# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        list_of_substrings = []
        list_of_vowels = ['a', 'e', 'i', 'o', 'u']
        list_of_counts = []
        for i in range(len(s)-k+1):
            list_of_substrings.append(s[i:i+k])
        for substring in list_of_substrings:
            count = 0
            for char in substring: 
                if char in list_of_vowels: count += 1
                list_of_counts.append(count)
        return max(list_of_counts)
    
if __name__ == '__main__':
    solution = Solution()
    print(solution.maxVowels("abciiidef", 3)) # 3
    print(solution.maxVowels("aeiou", 2)) # 2
    print(solution.maxVowels("leetcode", 3)) # 2
    print(solution.maxVowels("rhythms", 4)) # 0
    print(solution.maxVowels("tryhard", 4)) # 1
    print(solution.maxVowels("tryhard", 5)) # 1
    print(solution.maxVowels("tryhard", 6)) # 1
    print(solution.maxVowels("tryhard", 7)) # 1
    print(solution.maxVowels("tryhard", 8)) # 1
    print(solution.maxVowels("tryhard", 9)) # 1
    print(solution.maxVowels("tryhard", 10)) # 1