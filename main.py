
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
    
    dic_303 = {"Homework":  [.1,[1,1]],
           "Classwork": [.1,[1,1]],
           "Quiz_1":  [.1, [.796875]],
           "Quiz_2": [.1, [1]],
           "Quiz_3": [.1,[1]],
           "Mid_term": [.25, [.9]],
           "Final":[.25,[.9]]
           }

    dic_401 = {"Programming_Assignment": [.4, [0.65, 1, 1, 1]], #4 Assignments
               "Theory_Assignment": [.1, [.8, 1]], #2 Assignments
               "Test_1": [.15, [.88]],
               "Test_2": [.15, [.80]],
               "Test_3": [.2, [.80]],
               }


    print(grade(dic_401))
