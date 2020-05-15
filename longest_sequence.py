
def preprocess_word(given_word: str) -> str:
    return "".join(map(lambda x: "[^" + x + "]*" + x, given_word))

def is_subsequence(main_word: str, given_word: str) -> bool:
    import re
    pattern_word = preprocess_word(given_word)
    pattern = re.compile(pattern_word)
    finding = pattern.findall(main_word)
    return len(finding) != 0

S = "abppplee"
D = ["able", "ale", "apple", "bale", "kangaroo", "apppp"]
longest_subsequence = ""

for word in D:
    if is_subsequence(S, word):
        print(word)
        if len(word) > len(longest_subsequence):
            longest_subsequence = word

print("Longest:", longest_subsequence)