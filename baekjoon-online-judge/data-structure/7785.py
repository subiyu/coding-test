n = int(input())
people = set()

for _ in range(n):
    person, recode = input().split(" ")
    if recode == "enter":
        people.add(person)
    elif recode == "leave":
        people.remove(person)

people = list(people)
people = sorted(people, reverse=True)
[print(p) for p in people]