
def grade(dic: dict):
    grade = 0.0
    for i,j in dic.items():
        if (len(j[1]) == 0):
            continue
        elif(len(j[1]) == 1):
            grade += j[0] * sum(j[1])
        else:
            grade+=(j[0]* (sum(j[1])/len(j[1])))
    return grade*100

if __name__ == '__main__':
    # In the dictionary first part of the value is the percentage of grade,
    # The second part of the value is the grade you received on the category

    dic_303 = {"Homework":  [.1,[1,1]],
           "Classwork": [.1,[1,1]],
           "Quiz_1":  [.1, [41/54]],
           "Quiz_2": [.1, [63/64]],
           "Quiz_3": [.1,[52/64]],
           "Mid_term": [.25, [61/64]],
           "Final":[.25,[.83]]
           }

    dic_401 = {"Programming_Assignment": [.4, [0.65, .90, 1, 1]], #4 Assignments
               "Theory_Assignment": [.1, [.8, .934]], #2 Assignments
               "Test_1": [.15, [.88]],
               "Test_2": [.15, [.72]],
               "Test_3": [.2, [80/93]],
               }


    print(grade(dic_303))
