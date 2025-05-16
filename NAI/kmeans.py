import math
import random

def load_data(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            data.append([float(x) for x in line.strip().split(',')])
    return data
def euclidean_distance(point1, point2):
    return math.sqrt(sum([(x - y) ** 2 for x, y in zip(point1, point2)]))

def initialize_centroids(data, k):
    centroids = random.sample(data, k)
    return centroids

def assign_to_clusters(data, centroids):
    clusters = [[] for _ in range(len(centroids))]
    for point in data:
        distances = [euclidean_distance(point, centroid) for centroid in centroids]
        cluster_index = distances.index(min(distances))
        clusters[cluster_index].append(point)
    return clusters

def update_centroids(clusters):
    centroids = []
    for cluster in clusters:
        if cluster:
            centroid = [sum(coords) / len(cluster) for coords in zip(*cluster)]
            centroids.append(centroid)
        else:
            centroids.append(random.choice(clusters)[0])  # If a cluster is empty, choose a random point as centroid
    return centroids

def kmeans(data, k, max_iterations=100):
    centroids = initialize_centroids(data, k)

    for _ in range(max_iterations):
        clusters = assign_to_clusters(data, centroids)
        new_centroids = update_centroids(clusters)

        if new_centroids == centroids:
            break
        centroids = new_centroids

    return clusters, centroids

def within_cluster_sum_of_squares(cluster):
    centroid = [sum(coords) / len(cluster) for coords in zip(*cluster)]
    return sum([euclidean_distance(point, centroid) ** 2 for point in cluster])

def total_within_cluster_sum_of_squares(clusters):
    return sum([within_cluster_sum_of_squares(cluster) for cluster in clusters])

def main():
    file_path = "train-set.csv"
    while True:
        print("Should you wish to quit enter 'q' as k")
        k = int(input("Podaj liczbę klastrów k: "))
        if k == "q": break
        data = load_data(file_path)
        clusters, centroids = kmeans(data, k)
        for i, cluster in enumerate(clusters):
            print(f"Grupa {i+1}: {len(cluster)} obserwacji")
        print(f"Suma kwadratów odległości wewnątrz klastrów: {total_within_cluster_sum_of_squares(clusters)}")

main()
