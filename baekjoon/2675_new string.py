for tc in range(int(input())):
    r, s = map(str, input().split(" "))
    new_R = int(r)
    new_S = list(str(s))
    p = ""
    for i in new_S:
        p += new_R*i
    print(p)