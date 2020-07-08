import calendar
import datetime

def check_leap_year(year):
    if calendar.isleap(year):
        return True
    else:
        return False

today = datetime.date.today()
last_year = today.year - 1
year = last_year
date = today.strftime('%m月%d日')

# 昨年、現在、来年の閏年判定
for judge in range(3):
    if check_leap_year(year):
         print(f"{year}年{date}は閏年です。")
    else:
        print(f"{year}年{date}は閏年ではありません。")
    year += 1
