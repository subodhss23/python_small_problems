# Hamming distance is the number of characters that differ between two strings.

def hamming_distance(txt1, txt2):
    count = 0
    for i in range(len(txt)):
        if txt1[i] != txt2[i]:
            count += 1
    return count

print(hamming_distance("abcde", "bcdef"))
print(hamming_distance("abcde", "abcde"))
print(hamming_distance("strong", "strung"))