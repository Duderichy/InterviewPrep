def str_cmp(string):

    array = []
    prev = None
    count = None

    for char in string:
        if prev == None and count == None:
            prev = char
            count = 1
        elif char == prev:
            count += 1
        else:
            array.append((prev, count))
            print(char, count)
            prev = char
            count = 1
    array.append((char, count))
    return array


if __name__=="__main__":
    print(str_cmp("aaabbbbbbbbcccaaaaaaaaa"))
    print("aaabbbbbbbbcccaaaaaaaaa")
