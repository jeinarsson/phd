

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt


inp='''Sat Aug 22 15:20:42 2015 +0200
  15234
Sat Aug 22 10:11:45 2015 +0200
  13727
Fri Aug 21 17:45:37 2015 +0200
  13727
Thu Aug 20 22:01:57 2015 +0200
  13120
Thu Aug 20 17:28:41 2015 +0200
  13450
Wed Aug 19 17:37:41 2015 +0200
  12419
Wed Aug 19 14:05:52 2015 +0200
  11576
Tue Aug 18 21:50:24 2015 +0200
  10927
Tue Aug 11 16:55:14 2015 +0200
  10250
Tue Aug 11 14:15:17 2015 +0200
   9923
Mon Aug 10 08:57:49 2015 +0200
   6391'''
import dateutil
import StringIO
import sys
buf = StringIO.StringIO(inp)
if not sys.stdin.isatty():
  buf = sys.stdin
x = []
y= []
while(True):
  d = buf.readline().strip()
  if not d:
    break

  date = dateutil.parser.parse(d)
  if date < dateutil.parser.parse('Tue Aug 18 21:50:24 2015 +0200'):
    break

  n = int(buf.readline().strip())
  x.append(date)
  y.append(n)

n0=y[-1]
z = [p-n0 for p in y]
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())
plt.plot(x,z)
plt.gcf().autofmt_xdate()
plt.show()