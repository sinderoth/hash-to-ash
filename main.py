from article import Article


def test_phases():
    article = Article(7, 3112327, 3)
    path = []

    print("---------------- phase 1 -----------------")
    article.print_table()

    print("---------------- phase 2 -----------------")
    for i in range(26):
        char = chr(ord("a") + i)
        print(f"{char} is inserted with probe count {article.insert(char, i + 1)}")

    print(f"a is inserted with probe count {article.insert('a', 27)}")
    print(f"Table has a load factor of {article.get_load_factor()}\n")
    article.print_table()

    print("---------------- phase 3 -----------------")
    for i in range(26):
        char = chr(ord("a") + i)
        print(f'Trying to get "{char}", 1th occurance: {article.get(char, 1, path)}')
        print(f"Length of path for previous query: {len(path)}")
        print(path)
        path.clear()

    char = "a"
    print(f'Trying to get "{char}", 2th occurance: {article.get(char, 2, path)}')
    print(f"Length of path for previous query: {len(path)}")
    print(path)
    path.clear()

    print("---------------- phase 4 ------------------")
    for i in range(25, -1, -1):
        char = chr(ord("a") + i)
        print(f'Removing "{char}", 1st occurrence:', article.remove(char, 1))

        print(f'Trying to get "{char}", 1st occurrence:', article.get(char, 1, path))
        print("Length of path for previous query:", len(path))
        print(path)
        path.clear()

    print(f'Trying to get "a", 3rd occurrence:', article.get("a", 3, path))
    print(f'Removing "a", 1st occurrence:', article.remove("a", 1))
    print(f'Removing "a", 1st occurrence:', article.remove("a", 1))

    article.print_table()


def test_from_file():
    article = Article(7, 3112327, 3)
    path = []
    print("----------------")
    article.get_all_words_from_file("test3.txt")
    print("----------------")
    article.print_table()
    print("----------------")
    print(article.get_load_factor())


def main():
    # test_phases()
    test_from_file()

    # article.print_table()


if __name__ == "__main__":
    main()
