if __name__ == "__main__":
    a = int(input())
    s1 = set(map(int, input().strip().split()))
    b = int(input())
    s2 = set(map(int, input().strip().split()))
    print(len(s1.union(s2)))
