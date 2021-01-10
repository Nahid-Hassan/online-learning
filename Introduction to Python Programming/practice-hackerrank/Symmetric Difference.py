if __name__ == "__main__":
    m = int(input())
    a = set(map(int, input().strip().split()))
    n = int(input())
    b = set(map(int, input().strip().split()))

    a = a.symmetric_difference(b)
    res = list(a)
    res.sort()
    for r in res:
        print(r)
