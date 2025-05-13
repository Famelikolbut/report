# Инструкция для запуска проекта

1. Клонирование репозитория
```
git clone <URL репозитория>
cd <название репозитория>
```

2. Создание виртуального окружения и установка зависимостей
```
python3 -m venv venv   
source venv/bin/activate  # venv\Scripts\Activate
pip install -r requirements.txt
```

3. Запуск скрипта
```
main.py data1.csv data2.csv data3.csv --report payout
```

Результат:

![Скриншот](report(3).PNG)

4. Запуск тестов
```
pytest
```