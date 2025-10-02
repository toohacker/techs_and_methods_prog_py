stats = {'facebook': 55, 'yandex': 115, 'vk': 120, 'google': 99, 'email': 42, 'ok': 98}

max_ch = None
max_s = 0

for channel, sales in stats.items():
    if sales > max_s:
        max_s = sales
        max_ch = channel

print(f'Максимальный объем продаж на рекламном канале: {max_ch}')