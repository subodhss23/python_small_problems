''' Create two functions: is_prefix(word, prefix-) and is_suffix(word, -suffix).
    1. is_prefix should return True if it begins with the prefix argument.
    2. is_suffix should return True if it ends with suffix argument.

    Otherwise return False.'''


def is_prefix(word, prefix):
    removed_str = prefix.strip('-')
    if word.startswith(removed_str):
        return True
    return False


def is_suffix(word, suffix):
    removed_str_one = suffix.strip('-')
    if word.endswith(removed_str_one):
        return True
    return False


print(is_prefix("automation", "auto-"))
print(is_suffix("arachnophobia", "-phobia"))
print(is_prefix("retrospect", "sub-"))
print(is_suffix("vocation", "-logy"))