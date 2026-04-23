def reverse_string(text):
    return "" if "" == text else reverse_string(text[1:]) + text[0]
