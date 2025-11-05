import csv
from importlib.metadata import files
import sys, os
import pathlib

def ultra_simple_converter(log_file, csv_file):
    """Сверхпростая конвертация - только данные"""

    with open(log_file, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    # Ищем строку с полями
    fields = None
    for line in lines:
        if line.startswith('#fields'):
            fields = line.strip().split('\t')[1:]
            break

    if not fields:
        print("Не найдены поля в файле!")
        return

    # Собираем данные
    data_rows = []
    for line in lines:
        line = line.strip()
        if line and not line.startswith('#'):
            data_rows.append(line.split('\t'))

    # Записываем в CSV
    with open(csv_file, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(fields)  # заголовок
        writer.writerows(data_rows)  # все данные

    print(f"Успешно! Создан {csv_file}")
    print(f"Записей: {len(data_rows)}")
    print(f"Поля: {', '.join(fields)}")

def list_files(folder: str, pattern: str = "*"):
    """Возвращает список путей к файлам, соответствующим pattern."""
    return [p for p in pathlib.Path(folder).glob(pattern) if p.is_file()]

directoryInput = "C:\\Users\\kwert\\desktop\\testDataset"
directoryOutput = "C:\\Users\\kwert\\PycharmProjects\\AI_For_detect_Trafik_Anomaly\\normalDataset"
files = list_files(directoryInput, "*.log")
for i in files:
    name = i.name
    ultra_simple_converter(directoryInput + "\\" + name, directoryOutput + "\\" + name.split(".")[0] + ".csv")