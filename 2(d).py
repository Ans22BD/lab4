from datetime import datetime, timedelta

current_date = datetime.now()
yesterday = current_date - timedelta(days=1)
tomorrow = current_date + timedelta(days=1)

print("Вчера:", yesterday.strftime("%Y-%m-%d"))
print("Сегодня:", current_date.strftime("%Y-%m-%d"))
print("Завтра:", tomorrow.strftime("%Y-%m-%d"))