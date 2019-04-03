def perm(st_r, st_r2):
    check = {}
    check2 = {}

    for char in st_r:
        if char in check:
            check[char] += 1
        else:
            check[char] = 1

    for char2 in st_r2:
        if char2 in check2:
            check2[char2] += 1
        else:
            check2[char2] = 1

    return check == check2


if __name__=="__main__":
    print(perm("aabc","aabc"))
    print(perm("aabc","abc"))
