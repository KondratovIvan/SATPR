import numpy as np

# Task 1

matrix = np.loadtxt(open("task1.csv", "rb"), delimiter=",", skiprows=0)

print(matrix)

sumArr = []

for i in range(len(matrix[0])):
    sum = 0
    for j in range(len(matrix) - 1):
        sum += matrix[i][j] * matrix[len(matrix) - 1][j]
    sumArr.append(sum)
    sum = 0

print("Sum: " + str(sumArr))

print("Answer: " + str(max(sumArr)))

print("=================================================")

# Task 2

matrix = np.loadtxt(open("task2.csv", "rb"), delimiter=",", skiprows=0)


print(matrix)

for i in range(len(matrix[0])):
    temp = []
    weight = matrix[len(matrix)-1][i]

    for j in range(len(matrix) - 1):
        temp.append(matrix[j][i])

    for j in range(len(matrix) - 1):

        if weight > 0:
            matrix[j][i] = (
                    (matrix[j][i] - min(temp)) / (max(temp) - min(temp)))
        else:

            matrix[j][i] = (max(temp) - matrix[j][i]
                            ) / (max(temp) - min(temp))

print(matrix)

resultList = []

for i in range(len(matrix[0])):
    result = 0

    for j in range(len(matrix) - 1):
        result += matrix[i][j] * abs(matrix[len(matrix)-1][j])

    resultList.append(result)

print(resultList)