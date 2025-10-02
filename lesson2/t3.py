results = {
    'vk': {'revenue': 103, 'cost': 98},
    'yandex': {'revenue': 179, 'cost': 153},
    'facebook': {'revenue': 103, 'cost': 110},
    'adwords': {'revenue': 35, 'cost': 34},
    'twitter': {'revenue': 11, 'cost': 24},
}

for source, data in results.items():
    revenue = data['revenue']
    cost = data['cost']
    roi = (revenue / cost - 1) * 100
    data['ROI'] = round(roi, 2)

print(results)