'''
This problem was asked by Amazon.

Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
'''

def k_distinct(k, s):
    count = 0
    start = 0
    end = 0
    best_start = 0
    best_end = 0
    seen = set()
    for i in range(len(s)):
        c = s[i]
        if c not in seen:
            count += 1
        if count == 1:
            start = i
        if count > k:
            end = i
        if (end - start >= best_end - best_start):
            best_start = start
            best_end = end
            seen = set()
            count = 0
    return s[best_start:best_end + 1]

print(k_distinct(2, "abcba"))