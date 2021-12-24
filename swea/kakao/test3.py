from math import ceil

def solution(fees, records):
    answer = []
    car_dict = {}
    last_time = "23:59"
    for r in records:
        time, number, inout = r.split()
        if car_dict.get(number) is None:
            car_dict[number] = [convert(time)]
        else:
            car_dict[number].append(convert(time))
    
    for car, time in car_dict.items():
        n = len(time)
        if n % 2 != 0:
            print(time)
            time.append(convert(last_time))
    print(car_dict)
        
    return answer

def convert(time):
    hour, minute = time.split(":")
    return int(hour) * 60 + int(minute)

print(convert("23:59"))



print(int(3.4))