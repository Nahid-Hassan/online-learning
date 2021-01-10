if __name__ == "__main__":
    n = int(input())
    s = set(map(int, input().strip().split()))

    for _ in range(int(input())):
        instruct = input().split()
        if instruct[0] == 'pop':
            s.pop()
        elif instruct[0] == 'remove':
            s.remove(int(instruct[1]))
        elif instruct[0] == 'discard':
            s.discard(int(instruct[1]))

    print(sum(s))
