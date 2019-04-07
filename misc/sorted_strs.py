
def sorted_strs(str_list, subs):

    notfound = True
    i = 0
    j = len(str_list) - 1
    level = 0

    while notfound:
        mid = (i + j) // 2

        if level > len(str_list[mid]):
            i = mid
        elif str_list[mid][level] > subs[0]:
            j = mid
        elif str_list[mid][level] < subs[0]:
            i = mid
        elif str_list[mid][level] == subs[0]:
            return (i, j, level, str_list[mid][level])
        
        if i == j and j == len(str_list) - 1:
            level += 1
            i = 0
            j = len(str_list) - 1
        elif i == j:
            i = j + 1
            
            # find bucket parameter
            # this means to find the last string that begins with the current char
            while 

            j = "i"
            # how do I set j???
            # need to do a binary search for end of b


def buicket_end(l, i, level):
    j = len(l)
    notfound = True

    while notfound:
        mid = (start + end) // 2

        if level > len(str_list[mid]):
            i = mid
        elif str_list[mid][level] > subs[0]:
            j = mid
        elif str_list[mid][level] < subs[0]:
            i = mid
        elif str_list[mid][level] == subs[0]:
            return (i, j, level, str_list[mid][level])



if __name__=="__main__":
    strings = ["a", "b", "c", "d"]

    print(sorted_strs(strings, "c"))

