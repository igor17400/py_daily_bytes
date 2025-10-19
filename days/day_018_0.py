def longest_substring(s: str) -> int:
    l_idx = 0
    len_ = len(s)
    unique_chars = set()
    longest_len = 0

    for r_idx in range(len_):
        while s[r_idx] in unique_chars:
            unique_chars.remove(s[l_idx])
            l_idx += 1

        unique_chars.add(s[r_idx])
        longest_len = max(longest_len, r_idx - l_idx + 1)

    return longest_len

s = "abcabcbb"
print("Longest substring: ", longest_substring(s))
print("-----")

s = "bbbbb"
print("Longest substring: ", longest_substring(s))
print("-----")

s = "pwwkew"
print("Longest substring: ", longest_substring(s))
print("-----")
