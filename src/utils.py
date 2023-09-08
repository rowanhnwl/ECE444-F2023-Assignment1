# The utils class
class utils:

    # Reverse the digits of an integer
    def reversed(n):
        n_rev = 0

        while n != 0:
            digit = n % 10
            n_rev = n_rev * 10 + digit
            n = int(n/10)

        return n_rev

    # Return an integer in binary and octal bases
    def formatter(n):

        return [change_base(n, 2), change_base(n, 8)]

# Change an integer to a given base
def change_base(n, b):
    n_changed = 0
    n_copy = n
    digit = 1

    while n_copy != 0:
        n_changed += digit * (n_copy%b)

        n_copy = int(n_copy/b)
        digit *= 10

    return n_changed