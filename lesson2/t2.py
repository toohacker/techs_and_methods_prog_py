queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
]

total = len(queries)
stats = {}

for q in queries:
    words = len(q.split())
    stats[words] = stats.get(words, 0) + 1

for words, count in stats.items():
    percent = round(count / total * 100, 2)
    print(f'Поисковых запросов, содержащих {words} слов(а): {percent}%')