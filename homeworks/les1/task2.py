time_sec = input('Время в секундах\n>>>')
if int(time_sec) >= 3600:
    hours = int(time_sec) // 3600
    minutes = (int(time_sec) % 3600) // 60
    seconds = (int(time_sec) % 3600) % 60
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
elif int(time_sec) < 3600 and int(time_sec) >= 60:
    minutes = int(time_sec) // 60
    seconds = int(time_sec) % 60
    print(f"{0:02}:{minutes:02}:{seconds:02}")
else:
    seconds = int(time_sec) % 60
    print(f"{0:02}:{0:02}:{seconds:02}")
