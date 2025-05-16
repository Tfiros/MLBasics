import math

input_train_set = open("Train-set.txt", "r")
input_test_set = open("Test-set", "r")
train_set = [i.rstrip() for i in input_train_set]
test_set = [i.rstrip() for i in input_test_set]

def knn(a, b, c, d, k, list_of_vec):
    distances = []
    for i in list_of_vec:
        vec = i.split(",")
        distance = math.sqrt(
            (a - float(vec[0])) ** 2 + (b - float(vec[1])) ** 2 + (c - float(vec[2])) ** 2 + (d - float(vec[3])) ** 2)
        distances.append([distance, vec[4]])

    distances.sort()
    distances = distances[:k]

    appearances = dict()
    for i in distances:
        if i[1] not in appearances:
            appearances[i[1]] = 1
        else:
            appearances[i[1]] += 1

    max_value = [0, ""]
    for i in appearances:
        if appearances[i] > max_value[0]:
            max_value[0] = appearances[i]
            max_value[1] = i

    return max_value[1]


testing = True
while testing:
    k = int(input("Enter K "))
    print("Enter 1 to run tests with provided vector")
    print("Enter 2 to run tests using files")
    print("Enter 3 to exit program")
    inp = input()
    if int(inp) == 1:
        print("Enter 4 numbers vector for training")
        v1 = float(input("Enter first value "))
        v2 = float(input("Enter second value "))
        v3 = float(input("Enter third value "))
        v4 = float(input("Enter fourth value "))

        winner = knn(v1,v2,v3,v4,k,train_set)
        print("Result from train_set is "+winner)
    elif int(inp) == 2:
        counter_of_succeses = 0
        for i in test_set:
            vec = i.split(",")
            if knn(float(vec[0]), float(vec[1]), float(vec[2]), float(vec[3]), k, train_set) == (vec[4]):
                counter_of_succeses += 1
        print("The accuracy is: " + str((counter_of_succeses / len(test_set)) * 100))
    elif int(inp) == 3:
        testing = False
    else:
        print("Invalid input")


