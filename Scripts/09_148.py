import datetime as dt

today = dt.date.today()
curYear = today.year
end = dt.date(curYear, 12, 31)

delta = end - today


print(dt.date.today().strftime('%Y'))

print(delta.days, 'days')
