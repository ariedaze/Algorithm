search_word = ""
start = 1
depth = 0

def solution(word):
    wd = {1: "A", 2: "E", 3: "I", 4: "O", 5: "U"}
    print("ABC"[:-1])
    def search(cnt, w):
        global search_word, start, depth
        print(depth)
        if word == search_word or cnt == 4 or start == 5:
            return

        for i in range(5):
            search_word += wd[w]
            search(i, w)
            search_word = search_word[:-1]

    # search(1, 1)
    return 0

# solution("AAAAE")
solution("AAAE")