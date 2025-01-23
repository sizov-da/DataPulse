import chardet

file_path = "/Users/sizov/Desktop/Log-WAUZZZ4G8BN028205.txt"

# Определяем кодировку файла
with open(file_path, "rb") as f:
    raw_data = f.read()
    result = chardet.detect(raw_data)
    encoding = result['encoding']
    print(f"Определённая кодировка: {encoding}")

# Читаем и перекодируем
if encoding:
    with open(file_path, "r", encoding=encoding, errors="ignore") as f:
        content = f.read()

    with open("/Users/sizov/Desktop/Log-UTF8.txt", "w", encoding="utf-8") as f:
        f.write(content)

    print("Файл успешно перекодирован в UTF-8!")
