import requests

def download_robots_txt(url, file_path):
    try:
        response = requests.get(url + '/robots.txt', timeout=5)
        response.raise_for_status()

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(response.text)

        print(f"Файл {file_path} успішно завантажено.")
    except requests.exceptions.RequestException as e:
        print(f"Помилка при завантаженні: {e}")

# Приклад використання:
download_robots_txt("https://en.wikipedia.org", "wikipedia_robots.txt")
