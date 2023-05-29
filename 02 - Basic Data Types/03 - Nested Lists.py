if __name__ == '__main__':
    students = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
        scores.append(score)
        
    sec_low = sorted(set(scores))[1]
    
    for student in sorted(students):
        if student[1] == sec_low:
            print(student[0])
