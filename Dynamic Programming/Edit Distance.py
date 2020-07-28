# A Naive recursive Python program to fin minimum number
# operations to convert str1 to str2


def editDistance(str1, str2, n, m, operation=0):

    # If first string is empty, the only option is to
    # insert all characters of second string into first
    if n == 0:
        return m

    # If second string is empty, the only option is to
    # remove all characters of first string
    if m == 0:
        return n

    # If last characters of two strings are same, nothing
    # much to do. Ignore last characters and get count for
    # remaining strings.
    if str1[n-1] == str2[m-1]:
        return editDistance(str1, str2, n-1, m-1)

    x = str1

    if operation == 1:
        x = x[:n] + str2[m-1] + x[n:]
    elif operation == 2:
        x = x[:n-1] + x[n:]
    elif operation == 3:
        x = x[:n] + str2[m-1] + x[n+1:]

    print(x)

    # If last characters are not same, consider all three
    # operations on last character of first string, recursively
    # compute minimum cost for all three operations and take
    # minimum of three values.
    return 1 + min(editDistance(str1, str2, n, m-1, 1),    # Insert
                   editDistance(str1, str2, n-1, m, 2),    # Remove
                   editDistance(str1, str2, n-1, m-1, 3)    # Replace  )


# Driver program to test the above function
str1="sunday"
str2="saturday"
print(editDistance(str1, str2, len(str1), len(str2)))
