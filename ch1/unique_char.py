def unique_char(st_r):
    check = set()

    for char in st_r:
        print(char)
        if char in check:
            return False
        else:
            check.add(char)
    return True

if __name__=="__main__":
    print(unique_char("abcdefghijklmnopqrstuvwxyz"))
    print(unique_char("abcdefghijklmnopqrstuvwxyza"))
    print("hi")
