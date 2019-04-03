# you get one skip

def one_edit(st_r, st_r2):
    i = 0
    j = 0

    skip = 1
    while i < len(st_r) and j < len(st_r2):
        if st_r[i] != st_r2[j] and skip > 0:
            if j + 1 < len(st_r2) and st_r[i] == st_r2[j + 1]:
                skip -= 1
                j += 1
            elif i + 1 < len(st_r) and st_r[i + 1] == st_r2[j]:
                skip -= 1
                i += 1
            elif i + 1 < len(st_r) and j + 1 < len(st_r2) and st_r[i + 1] == st_r2[j + 1]:
                skip -= 1
                i += 1
                j += 1
            elif i + 1 >= len(st_r) and j + 1 >= len(st_r2):
                skip -= 1
                i += 1
                j += 1

        elif st_r[i] != st_r2[j] and skip == 0:
            return False
        else:
            i += 1
            j += 1

    return True

if __name__=="__main__":
    print(one_edit("test1","test2"), "True")
    print(one_edit("test1","t1st1"), "True")
    print(one_edit("test1","test1"), "True")
    print(one_edit("1est1","test2"), "False")
    print(one_edit("aaabbccc","aabbccc"), "True")
    # issue with one above, where it iterates on the wrong side
    # this might get pretty interesting with replacements... not sure of an
    # easy way to test this

    # do I have to check if the next two characters match?
    print(one_edit("aabbccc","aabbccc"), "True")
    print(one_edit("aabbccc","aabbbcc"), "True")
    print(one_edit("aabbccc","aabbcc"), "True")

    print(one_edit("aaabbccc","aaabbbccc"), "True")
    print(one_edit("aaabbbccc","aabbccc"), "False")
    print(one_edit("aaabbbccc","aabbccc"), "False")
