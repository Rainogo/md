import numpy as np

def euclidean_distance(p, q):
    return np.sqrt(np.sum((p - q) ** 2))

def average_distance_to_cluster(point, cluster):
    distances = [euclidean_distance(point, x) for x in cluster]
    return np.mean(distances)

def find_nearest_cluster(point, clusters, current_cluster):
    min_distance = float('inf')
    nearest_cluster = None
    
    for cluster in clusters:
        if not np.array_equal(cluster, current_cluster):  # Excluir el cluster actual
            avg_distance = average_distance_to_cluster(point, cluster)
            if avg_distance < min_distance:
                min_distance = avg_distance
                nearest_cluster = cluster
    
    return nearest_cluster, min_distance

# Datos de ejemplo
data = np.array([
    [1, 2], [2, 3], [3, 4],  # Cluster 1
    [10, 10], [11, 11], [12, 12],  # Cluster 2
    [20, 20], [21, 21], [22, 22]   # Cluster 3
])

# Clusters definidos (en este caso de ejemplo)
clusters = [
    data[:3],   # Cluster 1
    data[3:6],  # Cluster 2
    data[6:]    # Cluster 3
]

point = np.array([1, 2])  # Punto del cual se quiere encontrar el cluster más cercano
current_cluster = clusters[0]  # Suponiendo que el punto pertenece al primer cluster

nearest_cluster, min_distance = find_nearest_cluster(point, clusters, current_cluster)
print("Cluster más cercano:", nearest_cluster)
print("Distancia mínima promedio:", min_distance)
