def time_calculation(distance, velocity):
    time = distance / velocity
    print(time)

print("距離を入力してください")
distance = int(input())
print("速度を入力してください")
velocity = int(input())
time_calculation(distance, velocity)