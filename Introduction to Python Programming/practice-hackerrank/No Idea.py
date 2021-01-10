if __name__ == "__main__":
    input()
    elements = list(map(int, input().strip().split()))
    a = set(map(int, input().strip().split()))
    b = set(map(int, input().strip().split()))

    results = 0

    for element in elements:
        if element in a:
            results += 1
        if element in b:
            results -= 1
    
    print(results)
