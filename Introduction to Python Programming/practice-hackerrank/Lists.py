"""
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
"""
if __name__ == "__main__":
    result = list()

    for _ in range(int(input())):
        command, *args = input().split()

        if command == 'print':
            print(result)
        elif command == "reverse":
            result.reverse()
        elif command == "pop":
            result.pop()
        elif command == "sort":
            result.sort()
        elif command == 'append':
            result.append(int(list(args)[0]))
        elif command == 'insert':
            result.insert(int(list(args)[0]), int(list(args)[1]))
        else:
            result.remove(int(list(args)[0]))