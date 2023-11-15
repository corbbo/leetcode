# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        list_of_vowels = set(['a', 'e', 'i', 'o', 'u'])
        count = max_count = 0
        for i in range(len(s)):
            if i >= k:
                if s[i-k] in list_of_vowels:
                    count -= 1
            if s[i] in list_of_vowels:
                count += 1
            max_count = max(max_count, count)
        return max_count
    
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
    print(solution.maxVowels("tryhard", 8)) # 0
    print(solution.maxVowels("tryhard", 9)) # 0
    print(solution.maxVowels("tryhard", 10)) # 0