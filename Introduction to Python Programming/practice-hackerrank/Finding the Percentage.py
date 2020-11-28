if __name__ == "__main__":
    n = int(input())
    student_marks = {}

    for _ in range(n):
        name, *marks_list = input().split()
        score = list(map(float, marks_list))
        student_marks[name] = score
    query_name = input()

    print("{:.2f}".format(sum(student_marks[query_name]) / 3.0))