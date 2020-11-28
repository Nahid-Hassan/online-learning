def split_and_join(line):
    # write your code here
    temp = line.split(" ")
    return '-'.join(temp)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
