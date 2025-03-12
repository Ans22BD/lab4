from datetime import datetime

date1 = datetime(2024, 2, 10, 12, 0, 0)
date2 = datetime(2024, 2, 18, 15, 30, 0)

difference_in_seconds = abs((date2 - date1).total_seconds())
print("Разница в секундах:", difference_in_seconds)