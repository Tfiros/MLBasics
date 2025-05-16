import os
import math
import string

class Perceptron:
    def __init__(self, learning_rate, number_of_iterations,name):
        self.weights = [1] * number_of_iterations
        self.threshold = 0
        self.learning_rate = learning_rate
        self.name = name
    def activation(self, vector):
        result = 0
        for i in range(len(vector)):
            result += float(vector[i]) * self.weights[i]
        if result >= self.threshold:
            return 1
        else:
            return 0

    def delta(self, vec_x, actual_output):
        y = self.activation(vec_x)
        for i in range(len(self.weights)):
            self.weights[i] = self.weights[i] + (self.learning_rate * (actual_output - y) * float(vec_x[i]))
        self.threshold = self.threshold - (actual_output - y) * self.learning_rate


def train(percep, train_data):
    for train_vec in train_data:
        if percep.name == train_vec[1]:
            actual_output = 1
        else:
            actual_output = 0
        vec_len = vec_length(train_vec[0])
        normalized_vecX = [coord / vec_len for coord in train_vec[0]]
        percep.delta(normalized_vecX, actual_output)

def transform_text(text):
    letter_count = {letter: 0 for letter in string.ascii_lowercase}
    for element in text.lower():
        if element in string.ascii_lowercase:
            letter_count[element] += 1
    total_letters = sum(letter_count.values())
    letter_proportions = [count / total_letters for count in letter_count.values()]
    return letter_proportions

data_folder = "data"
train_data = []
for foldername in os.listdir(data_folder):
    folder_path = os.path.join(data_folder, foldername)
    if os.path.isdir(folder_path):
        for filename in os.listdir(folder_path):
            input_vec_with_lang = []
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "r", encoding="utf-8") as file:
                text = file.read()
                start_vec = transform_text(text)
                input_vec_with_lang.append(start_vec)
                input_vec_with_lang.append(foldername)
            train_data.append(input_vec_with_lang)

def vec_length(vec):
    squared_sum = sum([coord ** 2 for coord in vec])
    length = math.sqrt(squared_sum)
    return length

def scalar(vector1, vector2):
    result = 0
    for i in range(len(vector1)):
        result += (vector1[i] * vector2[i])
    return result

languages = [folder for folder in os.listdir(data_folder) if os.path.isdir(os.path.join(data_folder, folder))]


while True:
    print("Enter 1 to run tests")
    print("Enter 2 to end testing")
    mode = int(input("Enter your choice: "))
    match mode:
        case 1:
            lr = float(input("Enter learning rate: "))
            perceptron_layer = []
            for language in languages:
                perceptron = Perceptron(lr, 26, language)
                for i in range(100): train(perceptron, train_data)
                perceptron_layer.append(perceptron)

            normalized_we = []
            for p in perceptron_layer:
                normalized_weights = p.weights
                vec_len = vec_length(normalized_weights)
                normalized_weights = [coord / vec_len for coord in normalized_weights]
                normalized_we.append(normalized_weights)

            with open("data/data.txt", "r", encoding="utf-8") as file:
                text = file.read()
                normalized_text = transform_text(text)

                text_len = vec_length(normalized_text)
                normalized_input_vec = [coord / text_len for coord in normalized_text]

                results = []

                for vec in normalized_we:
                    il_skalarny = scalar(vec, normalized_input_vec)
                    results.append(il_skalarny)

                max_index = results.index(max(results))
                detected_language = languages[max_index]

                print("Wykryty jezyk to: ",detected_language)
        case 2:
            break