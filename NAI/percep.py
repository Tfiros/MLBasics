import random

input_train_set = open("Train-set.csv", "r")
input_test_set = open("Test-set.csv", "r")
train_set = [i.rstrip() for i in input_train_set]
test_set = [i.rstrip() for i in input_test_set]


class Perceptron:
    def __init__(self, learning_rate, number_of_iterations):
        self.weights = [random.uniform(-1, 1) for _ in range(number_of_iterations)]
        self.threshold = random.uniform(-1, 1)
        self.learning_rate = learning_rate
    def activation(self, vector):
        result = 0
        for i in range(len(vector)):
            result += float(vector[i]) * self.weights[i]
        if result >= self.threshold:
            return 1
        else:
            return 0

    def delta(self, vector, target_output, actual_output):
        for i in range(len(self.weights)):
            self.weights[i] = self.weights[i] + (self.learning_rate * (actual_output - target_output) * vector[i])
        self.threshold = self.threshold + (self.learning_rate * (-1))



testing = True
while testing:
    print("Type 1 to run tests with perceptron using files")
    print("Type 2 to run tests with perceptron on user vectors")
    print("Type 3 to stop training")
    mode = int(input("Enter your choice: "))
    alfa_const = float(input("Enter your alpha"))
    match mode:
        case 1:
            perceptron = Perceptron(alfa_const,4)
            actuall = 0
            for element in train_set:
                vector = [float(x) for x in element.split(",")[:-1]]
                if element.split(",")[-1] == "Iris-setosa":
                    actuall = 1
                else:
                    actuall = 0
                perceptron.delta(vector, perceptron.activation(vector), actuall)
            print("1 is interpreted as Iris-setosa, 0 is interpreted as Iris-versicolor")
            iris_setosa = 0
            iris_versicolor = 0
            succeses =0
            for element in test_set:
                if (perceptron.activation([float(x) for x in element.split(",")[:-1]]) == 1) and element.split(",")[-1] == "Iris-setosa":
                        iris_setosa+=1
                        succeses+=1
                elif (perceptron.activation([float(x) for x in element.split(",")[:-1]]) == 0) and element.split(",")[-1] == "Iris-versicolor":
                        iris_versicolor+=1
                        succeses+=1
            accuracy = (succeses/len(test_set))*100
            print("Overall accuracy is " + str(accuracy))
            print("Iris-setosa accuracy is " + str((iris_setosa/15)*100))
            print("Iris-versicolor accuracy is " + str((iris_versicolor/15)*100))
            perceptron = None
            del perceptron
        case 2:
            amount_of_numbers= int(input("Type the amount of numbers in your vector"))
            vector = []
            for i in range(amount_of_numbers):
                vector.append(float(input("Enter a number: ")))
            perceptr = Perceptron(alfa_const, amount_of_numbers)
            print("The result of the perceptron is: " + str(perceptr.activation(vector)))
        case 3:
            testing = False
            break



