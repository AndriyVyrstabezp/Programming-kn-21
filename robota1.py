class Route:
    def __init__(self, start, finish, *distances):
        self.start = start
        self.finish = finish
        self.distances = list(distances)

    def __str__(self):
        return (f"Маршрут: {self.start} -> {self.finish}, "
                f"Довжина: {self.total_distance()} км, "
                f"Привали: {self.rest_stops_count()}")

    def total_distance(self):
        return sum(self.distances)

    def rest_stops_count(self):
        return len(self.distances) - 1

    def longest_segment(self):
        return max(self.distances, default=0)

 
    def __lt__(self, other):
        return self.total_distance() < other.total_distance()

    def __le__(self, other):
        return self.total_distance() <= other.total_distance()

    def __gt__(self, other):
        return self.total_distance() > other.total_distance()

    def __ge__(self, other):
        return self.total_distance() >= other.total_distance()

    def __eq__(self, other):
        return self.total_distance() == other.total_distance()


routes = [
    Route("Кваси", "Дземброня", 8, 8, 12, 18, 12),
    Route("Львів", "Славське", 15, 10, 5, 20),
    Route("Татарів", "Говерла", 10, 10, 15, 10),
    Route("Івано-Франківськ", "Буковель", 25, 20, 30),
    Route("Рахів", "Ясіня", 7, 14, 7),
    Route("Косів", "Верховина", 10, 10, 15),
    Route("Драгобрат", "Говерла", 12, 18, 12),
    Route("Ужгород", "Мукачево", 20, 10, 30, 25),
    Route("Чернівці", "Хотин", 10, 20, 30),
    Route("Трускавець", "Моршин", 12, 18, 24, 30),
]

routes.sort()


def routes_with_max_rest_stops(routes):
    max_stops = 0
    for route in routes:
        if route.rest_stops_count() > max_stops:
            max_stops = route.rest_stops_count()

    result = []
    for route in routes:
        if route.rest_stops_count() == max_stops:
            result.append(route)
    return result


def route_with_longest_segment(routes):
    longest_route = routes[0]
    for route in routes:
        if route.longest_segment() > longest_route.longest_segment():
            longest_route = route
    return longest_route


def routes_with_point(routes, point):
    result = []
    for route in routes:
        if route.start == point or route.finish == point:
            result.append(route)
    return result


print("Усі маршрути:")
for route in routes:
    print(route)

print("\nМаршрути з максимальною кількістю привалів:")
for route in routes_with_max_rest_stops(routes):
    print(route)

print("\nМаршрут з найдовшим переходом:")
print(route_with_longest_segment(routes))

point = "Говерла"
print(f"\nМаршрути, що починаються або закінчуються в точці {point}:")
for route in routes_with_point(routes, point):
    print(route)
