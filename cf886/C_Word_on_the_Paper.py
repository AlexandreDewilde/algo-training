for _ in range(int(input())):
    word = []

    for _ in range(8):
        for el in input():
            if el != ".":
                word.append(el)
    
    print("".join(word))