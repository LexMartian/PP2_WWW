from datetime import date, timedelta
import datetime

dt = date.today() - timedelta(5)
print('5 days before :',dt)

print()

yesterday = date.today() - timedelta(1)
print("Yesterday was: ", yesterday)
today = yesterday + timedelta(1)
print("Today is: ", today)
tomorrow = today + timedelta(1)
print("Tomorrow will be: ", tomorrow)

print()

dt = datetime.datetime.today().replace(microsecond=0)
print(dt)