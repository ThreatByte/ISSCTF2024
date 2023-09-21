import datetime
import dkim

with open('C:/your/path', 'r') as file:
    data = file.read()
    date = datetime.datetime(2023,8,20,13,6,0)
    for x in range(1000):
        date += datetime.timedelta(seconds=1)
        modified = data.replace('<placeholder>', date.strftime('%H:%M:%S'))
        toDecode = bytes (modified,"ascii")
        print(date.strftime('%H:%M:%S'))
        if(dkim.verify(toDecode)):
         print('Answer: ' + str(date))
        break
