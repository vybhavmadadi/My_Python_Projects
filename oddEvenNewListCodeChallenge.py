# From two lists, make a new list with odd nums frmo first list and even from the second.


def oddEven(list1, list2):

    result_list = []

    for n in list1:
        if n % 2 != 0:
            result_list.append(n)

    for n in list2:
        if n % 2 == 0:
            result_list.append(n)

    return result_list


list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

print(oddEven(list1, list2))
