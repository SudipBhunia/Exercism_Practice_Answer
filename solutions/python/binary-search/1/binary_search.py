def find(search_list, value):
    if value not in search_list:
        raise ValueError("value not in array")
    lf, rt= 0, len(search_list) - 1
    while lf <= rt:
        mid = (lf + rt) // 2
        if search_list[mid] == value:
            return mid
        elif search_list[mid] > value:
            rt = mid - 1
        else:
            lf = mid + 1