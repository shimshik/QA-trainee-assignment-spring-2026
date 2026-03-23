# Инструкция по запуску тестов

## 1. Склонировать репозиторий

git clone https://github.com/shimshik/QA-trainee-assignment-spring-2026.git
cd QA-trainee-assignment-spring-2026

## 2. Активировать виртуальное окружение

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate

## 3. Установите зависимости

pip install -r requirements.txt

## 4. Запустите тесты

pytest tests/
