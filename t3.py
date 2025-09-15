boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Kira', 'Emma', 'Trisha']

if len(boys) != len(girls):
    raise Exception('Внимание, кто-то может остаться без пары!')

boys.sort()
girls.sort()

pairs = (zip(boys, girls))


print("Идеальные пары: ")

for (boy, girl) in pairs:
    print(f'{boy} и {girl}')

