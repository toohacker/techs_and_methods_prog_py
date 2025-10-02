countries_temperature = [
    ['Thailand', [75.2, 77, 78.8, 73.4, 68, 75.2, 77]],
    ['Germany', [57.2, 55.4, 59, 59, 53.6]],
    ['Russia', [35.6, 37.4, 39.2, 41, 42.8, 39.2, 35.6]],
    ['Poland', [50, 50, 53.6, 57.2, 55.4, 55.4]]
]


def f_to_c(f):
    return round(((f - 32) * 5 / 9), 1)

for [ctr, tmp] in countries_temperature:
    s = sum(tmp)
    avg_temp = s / len(tmp)
    print(ctr, '-', f_to_c(avg_temp))
