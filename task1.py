users = [
    {"name": "Alice", "age": 25, "email": "alice@‌‌example.com"},
    {"name": "Bob", "age": 17},
    {"name": "Charlie", "age": 30, "email": "charlie@‌‌example.com"},
    {"name": "David", "email": "david@‌‌example.com"}
    ]

#первый вариант
namelist = [i['name'] for i in users if 'name' in i and 'age' in i and i['age'] >= 18 and 'email' in i]

#‌ второй вариант
namelist = [i['name'] for i in users if {'name', 'age', 'email'}.issubset(i) and i['age'] >= 18]

#‌ третий вариант
namelist = [i['name'] for i in users if ({'name', 'age', 'email'}.issubset(i) and i['age'] >= 18)]
