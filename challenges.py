def ints(list):
    first = list[0]
    count = 0
    for item in list:
        if item == first:
            count += 1

    if count == len(list):
        print("True")
    else:
        print("False")

ints([1,1,1,1,1,1,1])