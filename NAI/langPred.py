import os
import string
import math


class Perceptron:
    def __init__(self, stala_uczenia, vec_len, nazwa):
        self.vec_wag = [1.1] * vec_len
        self.prog = 0.0
        self.stala_uczenia = stala_uczenia
        self.nazwa = nazwa

    def compute_y(self, vec_x):
        result = 0
        for i in range(len(vec_x)):
            result += float(vec_x[i]) * self.vec_wag[i]
        if result >= self.prog:
            return 1
        else:
            return 0

    def learn(self, vec_x, actual_output):
        y = self.compute_y(vec_x)
        for i in range(len(self.vec_wag)):
            self.vec_wag[i] = self.vec_wag[i] + (self.stala_uczenia * (actual_output - y) * float(vec_x[i]))
        self.prog = self.prog - (actual_output - y) * self.stala_uczenia


class Trainer:
    def __init__(self, perceptron, train_data):
        self.perceptron = perceptron
        self.train_data = train_data

    def train(self):
        for train_vec in self.train_data:
            if self.perceptron.nazwa == train_vec[1]:
                actual_output = 1
            else:
                actual_output = 0
            vec_len = vector_length(train_vec[0])
            normalized_vecX = [coord / vec_len for coord in train_vec[0]]
            self.perceptron.learn(normalized_vecX, actual_output)


def filter_and_transform(tekst):
    letter_count = {letter: 0 for letter in string.ascii_lowercase}
    for znak in tekst.lower():
        if znak in string.ascii_lowercase:
            letter_count[znak] += 1
    total_letters = sum(letter_count.values())
    letter_proportions = [count / total_letters for count in letter_count.values()]
    return letter_proportions


def vector_length(vec):
    squared_sum = sum([coord ** 2 for coord in vec])
    length = math.sqrt(squared_sum)
    return length


def iloczyn_skalarny(vector1, vector2):
    result = 0
    for i in range(len(vector1)):
        result += (vector1[i] * vector2[i])
    return result


data_folder = "data"
train_data = []
for foldername in os.listdir(data_folder):
    folder_path = os.path.join(data_folder, foldername)
    if os.path.isdir(folder_path):
        for filename in os.listdir(folder_path):
            vecX_and_name = []
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "r", encoding="utf-8") as file:
                text = file.read()
                vec_pocz = filter_and_transform(text)
                vecX_and_name.append(vec_pocz)
                vecX_and_name.append(foldername)
            train_data.append(vecX_and_name)

languages = [folder for folder in os.listdir(data_folder) if os.path.isdir(os.path.join(data_folder, folder))]
print(languages)

vec_perceptron = []
for language in languages:
    perceptron = Perceptron(0.1, 26, language)
    train = Trainer(perceptron, train_data)
    train.train()
    vec_perceptron.append(perceptron)

normalized_w = []
for p in vec_perceptron:
    normalized_weights = p.vec_wag
    vec_len = vector_length(normalized_weights)
    normalized_weights = [coord / vec_len for coord in normalized_weights]
    normalized_w.append(normalized_weights)

while True:
    with open("data/data.txt", "r", encoding="utf-8") as file:
        test = input("Podaj tekst do rozpoznania języka (wpisz '1' aby wyjść z programu): ")
        if test == "1":
            break
        test = file.read()
        test = filter_and_transform(test)

        vec_len = vector_length(test)
        normalized_vecX = [coord / vec_len for coord in test]

        results = []

        for vec in normalized_w:
            il_skalarny = iloczyn_skalarny(vec, normalized_vecX)
            results.append(il_skalarny)

        max_index = results.index(max(results))
        detected_language = languages[max_index]

        print("=" * 100)
        print("Wykryty język:", detected_language)
        print("=" * 100)
