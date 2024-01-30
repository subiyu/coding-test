from collections import deque


def solution(cacheSize, cities):
    answer = 0
    cache = deque([0] * cacheSize)

    for city in cities:
        city = city.lower()
        if city not in cache:
            answer += 5
            cache.append(city)
            if len(cache) > cacheSize:
                cache.popleft()
        else:
            answer += 1
            cache.remove(city)
            cache.append(city)

    return answer