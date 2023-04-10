import calendar


def print_month(month, year):
    month_view = calendar.monthcalendar(year, month)
    prev_month = calendar.monthcalendar(year, month - 1) if month > 1 else calendar.monthcalendar(year - 1, 12)
    next_month = calendar.monthcalendar(year, month + 1) if month < 12 else calendar.monthcalendar(year + 1, 1)
    for number_day in range(0, len(month_view[0])):
        if month_view[0][number_day] == 0:
            month_view[0][number_day] = prev_month[len(prev_month) - 1][number_day]
        if month_view[len(month_view) - 1][number_day] == 0:
            month_view[len(month_view) - 1][number_day] = next_month[0][number_day]
    return month_view


if __name__ == '__main__':
    calendar.prmonth(2017, 11)
    month = print_month(11, 2017)
    for i in range(0, len(month)):
        print(month[i])
