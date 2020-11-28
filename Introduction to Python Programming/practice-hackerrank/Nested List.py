if __name__ == "__main__":

    name_grade = list()

    for _ in range(int(input())):
        name = input()
        score = float(input())

        data = [name, score]
        name_grade.append(data)

    name_grade.sort(key=lambda x: x[1])
    # print(name_grade)

    # find the second lowest
    idx = next((len(name_grade) - i - 1 for i,
              lst in enumerate(reversed(name_grade)) if name_grade[0][1] in lst), -1)
    # print(idx)

    result = list()
    for a, b in name_grade:
        if name_grade[idx+1][1] == b:
            result.append(a)
    
    result.sort()
    for name in result:
        print(name)