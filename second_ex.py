def bigger_is_greater(w):
    word = list(w)
    i = len(word) - 1

    while i > 0 and word[i - 1] >= word[i]:
        i -= 1

    if i <= 0:
        return "no answer"

    j = len(word) - 1
    while word[j] <= word[i - 1]:
        j -= 1

    word[i - 1], word[j] = word[j], word[i - 1]

    word[i:] = reversed(word[i:])

    return "".join(word)


def main():
    T = int(input().strip())
    for _ in range(T):
        w = input().strip()
        result = bigger_is_greater(w)
        print(result)


if __name__ == "__main__":
    main()
