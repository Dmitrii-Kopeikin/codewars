def permutations(word: str) -> list[str]:
    def get_permutation(permutation: str, chars: str):
        chars_len = len(chars)
        if chars_len == 1:
            permutations_set.add(permutation + chars[0])
        else:
            for i in range(0, chars_len):
                new_chars = chars.replace(chars[i], '', 1)
                get_permutation(permutation + chars[i], new_chars)

    permutations_set = set()
    get_permutation('', word)

    return list(permutations_set)


if __name__ == '__main__':
    pass
