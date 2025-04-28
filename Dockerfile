# Базовий імедж
FROM python:3.9
LABEL maintainer="kovalukilla271@gmail.com"

ENV PYTHOUNNBUFFERED 1

# Робоча директорія
WORKDIR /airport_project

# Копіюємо залежності
COPY requirements.txt .

# Встановлюємо залежності
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо проєкт
COPY . .

# Вказуємо команду запуску
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]