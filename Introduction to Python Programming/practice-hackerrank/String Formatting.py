def print_formatted(number):
    # your code goes here
    bit_length = len(bin(number)[2:]) + 1

    for i in range(1, number + 1):
        print("{:>{}}{:>{}}{:>{}}{:>{}}".format(
            i, bit_length-1, oct(i)[2:], bit_length, hex(i)[2:].upper(), bit_length, bin(i)[2:], bit_length))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
