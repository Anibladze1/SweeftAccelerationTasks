def count_words(words):
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count


def main():
    n = int(input().strip())
    words = [input().strip() for _ in range(n)]

    word_count = count_words(words)

    print(len(word_count))
    print(" ".join(str(word_count[word]) for word in word_count))


if __name__ == "__main__":
    main()
