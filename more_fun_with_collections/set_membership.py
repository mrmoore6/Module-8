def in_set(set,number):
    if number in set:
        bool = True
    else:
        bool = False
    return bool



if __name__ == '__main__':
    set = {1,2,3,4,4,}
    anwser = in_set(set, 5)
    print(anwser)



