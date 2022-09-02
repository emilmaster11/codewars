stunde = 3600000
minute = 60000
sekunde = 1000
zahl_milli = stunde + minute + sekunde

print(zahl_milli)


def past(h, m, s):
  stunde = 3600000 * h
  minute = 60000 * m
  sekunde = 1000 * s

  zahl_milli = stunde + minute + sekunde
  return zahl_milli