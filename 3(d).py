from datetime import datetime

current_time = datetime.now().replace(microsecond=0)
print("Текущее время без микросекунд:", current_time)