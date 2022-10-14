def intersection(lists):
    common = lists[0]

    for one_list in lists:
        common = [value for value in one_list if value in common]

    return common
