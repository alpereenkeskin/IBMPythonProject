def euclidean_distance(point1, point2):
    dx = point2[0] - point1[0]
    dy = point2[1] - point1[1]
    return (dx**2 + dy**2)**0.5


points = [(1, 2), (4, 7), (3, 5), (0, 0)]
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = euclidean_distance(points[i], points[j])
        distances.append(dist)
min_distance = min(distances)

print(f"iki nokta arası uzaklık: {distances}")
print(f"Minimum uzaklık: {min_distance:.6f}")
