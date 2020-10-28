def neutralise(s1, s2):
    result = ''
    i = 0
    while (i <= len(s1) - 1):
        if s1[i] == '+' and s2[i] == '+':
            result += '+'
        elif s1[i] == '-' and s2[i] == '-':
            result += '-'
        elif s1[i] == '+' and s2[i] == '-' or s1[i] == '-' and s2[i] == '+':
            result += '0'
        i+=1
    return result

print(neutralise("--++--", "++--++"))
print(neutralise("-+-+-+", "-+-+-+"))
print(neutralise("-++-", "-+-+"))