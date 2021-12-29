def solution(lines):
    answer = 0
    time_list = []
    for line in lines:
        date, time, duration = line.split()
        time_list.append(make_seconds(time, duration))
        
    n = len(lines)
    for i in range(n):
        candi = 0
        for j in range(i, n):
            if time_list[i][1] > time_list[j][0] - 1000:
                candi += 1
        answer = max(answer, candi)
        
    return answer

def make_seconds(time_string, duration):
    hour_string, min_string, second_string = time_string.split(":")
    final_time = (int(hour_string) * 3600 + int(min_string) * 60)  * 1000 + int(float(second_string)*1000)
    duration_time = int(float(duration.replace("s", "")) * 1000)
    first_time = (final_time - duration_time) + 1
    if first_time <= 0:
        return (0, final_time)
    return (first_time, final_time)

