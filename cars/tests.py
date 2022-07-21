
from datetime import date, timedelta
allert2 = date.today() - timedelta(days=30)


now = date(year=2022, month=3, day=7)
termin = date(year=2022, month=4, day=8)
print(now)
print(termin)
print(now + timedelta(days=30))

if termin < now:
    print('po terminie')
elif termin < now + timedelta(days=30):
    print('mniej niz 30 dni do konca')
else:
    print('ok')


