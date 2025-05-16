input = input()

def is_palindrome(string):
    if len(string) <= 1:
        return True
    first_string = string[0]
    last_string = string[-1]
    if first_string == last_string:
        return is_palindrome(string[1:len(string) - 1])
    else:
        return False

# def is_palindrome(string):
#     for i in range(0, len(string) // 2):
#         if string[i] != string[len(string) - 1 - i]:
#             return False
#     return True

print(is_palindrome(input))