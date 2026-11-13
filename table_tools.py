
def day_total(row):
    return row["checkups"] + row["diabetes"] + row["blood_pressure"]


def column_total(table, column):
    total = 0
    for row in table:
        total = total + row[column]
    return total


def busiest_day(table):
    best_day = None
    best_total = 0
    for row in table:
        if day_total(row) > best_total:
            best_total = day_total(row)
            best_day = row["day"]
    return best_day


def average_wait(table):
    waits = []
    for row in table:
        waits.append(row["avg_wait"])
    return sum(waits) / len(waits)
