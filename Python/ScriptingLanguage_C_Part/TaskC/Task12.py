"""
    Дан текст, в котором присутствуют даты в формате d.hh:mm:ss (d. или d.hh: могут отсутствовать).
    Нужно сложить все эти даты и вывести результирующую в том же формате. (30 баллов)

"""
# (?<!:)([0-5][0-9]):([0-5][0-9])(?!:) mm:ss
# (?<![.])([0-1][0-9]|[2][0-3]):([0-5][0-9]):([0-5][0-9])(?!:) hh:mm:ss
# ([0-9])+[.]([0-1][0-9]|[2][0-3]):([0-5][0-9]):([0-5][0-9])(?!:) d.hh:mm:ss
import re
from datetime import timedelta


def data_sum(text):
    time_count = timedelta()
    mmss = re.compile(r"(?<!:)([0-5][0-9]):([0-5][0-9])(?!:)")
    hhmmss = re.compile(r"(?<![.])([0-1][0-9]|[2][0-3]):([0-5][0-9]):([0-5][0-9])(?!:)")
    dhhmmss = re.compile(r"([0-9]+)[.]([0-1][0-9]|[2][0-3]):([0-5][0-9]):([0-5][0-9])(?!:)")
    mmss_time = re.findall(mmss, text)
    hhmmss_time = re.findall(hhmmss, text)
    dhhmmss_time = re.findall(dhhmmss, text)
    for i in mmss_time:
        time_count += timedelta(minutes=int(i[0]), seconds=int(i[1]))
    for i in hhmmss_time:
        time_count += timedelta(hours=int(i[0]), minutes=int(i[1]), seconds=int(i[2]))
    for i in dhhmmss_time:
        time_count += timedelta(days=int(i[0]), hours=int(i[1]), minutes=int(i[2]), seconds=int(i[3]))
    s = str(time_count).replace(" days, ", ".")
    return s


def main():
    print(data_sum("5.10:55:10 115.09:45:15 14.50:20:15 14:18:45 27:48:52 19:09 25:23:23"))


if __name__ == '__main__':
    main()
