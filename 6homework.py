from datetime import datetime, timedelta
from collections import Counter

def anser(list):
    date_range = []
    for el in list:
        start_date = el[0]
        end_date = el[1]
        start = datetime.strptime(start_date, '%Y-%m-%d')
        end = datetime.strptime(end_date, '%Y-%m-%d')
        current_date = start
        while current_date <= end:
            date_range.append(current_date.strftime('%Y-%m-%d'))
            current_date += timedelta(days=1)
    date_counts = Counter(date_range)
    most_common = date_counts.most_common(1)
    if most_common:
        return most_common[0]
    else:
        return None


list = [("2024-09-15", "2024-09-15"), ("2024-09-14", "2024-09-21")]
print(anser(list))