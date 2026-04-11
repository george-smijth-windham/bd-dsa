def count_names(list_of_lists, target_name):
    count = 0
    for name_list in list_of_lists:
        for name in name_list:
            count = count if name != target_name else count + 1
    return count
