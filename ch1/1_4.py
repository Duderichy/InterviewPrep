def pal_perm(st_r):
    check = {}

    for char in st_r:
        if char in check:
            check[char] += 1
        else:
            check[char] = 1

    odd = False

    for k, v in check.items():
        if v % 2 == 1 and not odd:
            odd = True
        elif v % 2 == 0:
            pass
        elif v % 2 == 1 and odd:
            return False
    return True


if __name__=="__main__":
    print(pal_perm("cat tac"))
    print(pal_perm("cat taca"))
    print(pal_perm("acat taca"))
