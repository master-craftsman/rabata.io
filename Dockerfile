# Используем официальный образ Python
FROM python:3.11

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файлы проекта в рабочую директорию
COPY . .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Устанавливаем Playwright и необходимые браузеры
RUN pip install playwright
RUN playwright install

# Устанавливаем Allure
RUN apt-get update && apt-get install -y allure

# Запускаем тесты
CMD ["sh", "-c", "pytest tests/*.py --alluredir=allure-results  && allure serve allure-results"]
