def find_missing(list1,list2):
    

    if list1 == list2:

        return 0

    elif list1 != list2:

        j = set(list1)

        k = set(list2)

        missing = j^k

        return list(missing)[0]
        print(find_missing([1,2],[1,2,3]))