# Ближайшие бары

На основании открытых данных (data.mos.ru), скрипт определяет:

- самый большой бар;
- самый маленький бар;
- самый близкий бар (текущие gps-координаты пользователь введет с клавиатуры).

# Как использовать

Сначала получаем десериализацию JSON, с помощью функции:
```python
load_data(file_path)
```
где
  file_path - путь до файла с произвольными данными в формате JSON.
Если по указанному пути нет файла, то попытаемся его забрать с URLа
```python
url_json = 'https://apidata.mos.ru/v1/features/1796?api_key=...'
response = urlopen(url_json)
```

В случае успеха, выполняется функции и получаем результат:
```python
print ("самый большой бар: ", get_biggest_bar(bars_json['features']))
print ("самый маленький бар: ", get_smallest_bar(bars_json['features']))
print("самый близкий бар: ", get_closest_bar(bars_json['features']))
```
где
  bars_json - JSON, загруженный из файла.

В функции **get_closest_bar** (определение ближайшего бара), значения gps-координат *longitude* и *latitude*, пользователь вводит с клавиатуры
```python
longitude = float(input('Enter longitude:'))
latitude = float(input('Enter latitude:'))
```

Импортируемые модули
```python
import json #кодирование и декодирование данных
import os #для работы с ОС
import re #работа с регулярными выражениями
from math import sqrt
from urllib.request import urlopen #работа с HTTP
```

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```bash

$ python bars.py
# Пример ответа
самый большой бар:  Спорт бар «Красная машина»
самый маленький бар:  Сушистор
Enter longitude:33
Enter latitude:32.1
самый близкий бар:  Корпорация Бар
```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
