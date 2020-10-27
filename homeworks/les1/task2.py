time_sec = input('Время в секундах\n>>>')
if int(time_sec) >= 3600:
    hours = int(time_sec) // 3600
    minutes = (int(time_sec) % 3600) // 60
    seconds = (int(time_sec) % 3600) % 60
    print('{0}:{1}:{2}'.format(hours,minutes,seconds)
elif int(time_sec) < 3600 and int(time_sec) >= 60:
    minutes = int(time_sec) // 60
    print(minutes)
    seconds = int(time_sec) % 60
    print('00:{0}:{1}'.format(minutes,seconds))
else:
    seconds = int(time_sec) % 60
    print('00:00:{0}'.format(seconds))
