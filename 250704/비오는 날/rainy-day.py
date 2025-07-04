n = int(input())
date = []
day = []
weather = []

for _ in range(n):
    d, dy, w = input().split()
    date.append(d)
    day.append(dy)
    weather.append(w)

# Please write your code here.
class Rainday:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

rainday = [Rainday(date, day, weather) for date, day, weather \
            in zip(date, day, weather)]

target = min((r for r in rainday if r.weather == "Rain"), key = lambda x: x.date)

print(f"{target.date} {target.day} {target.weather}")