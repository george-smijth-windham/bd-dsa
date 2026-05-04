def repeat_string(word, times):
    return "" if times <= 0 else word + repeat_string(word, times - 1)
