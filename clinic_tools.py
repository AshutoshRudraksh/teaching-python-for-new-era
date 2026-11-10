
def average_age(ages):
    total = sum(ages)
    return total / len(ages)


def count_by_condition(records):
    counts = {}
    for record in records:
        condition = record["condition"]
        if condition in counts:
            counts[condition] = counts[condition] + 1
        else:
            counts[condition] = 1
    return counts


def older_names(records, age_limit):
    names = []
    for record in records:
        if record["age"] >= age_limit:
            names.append(record["name"])
    return names
