import re

text = """
Игра окончена!

Победители:
    1. 🐾🐮Флёппа🐉 - 👨🏼‍⚕️️Доктор
    2. Воробушек - 🧙🏼 Бомж
    3. 🐙 - 👨🏼 Мирный Житель
    4. Кто я - 🕵🏼 Комиссар Каттани
    5. 𝕄𝕖𝕤𝕤𝕖𝕟𝕘𝕖𝕣 𝕠𝕗 𝔻𝕒𝕣𝕜𝕟𝕖𝕤𝕤 ℍ𝕖𝕝𝕔𝕦𝕣𝕥 🐮 - 💃 Любовница
    6. . - 🐺 Оборотень
    7. Лешка - 💣 Камикадзе

Другие пользователи:
    8. 𝐤o𝐭𝐲𝐮𝐜𝐢 𝐞𝐩😍 - 🤵🏻 Дон
    9. Andrey#жду23f🐮 - 🤵🏻 Дон

Игра длилась: 5 минут учти их может больше или меньше
"""
ir = [1, 3]
# Используем регулярные выражения для извлечения информации
pattern = re.compile(r'\d+\.\s+(.+?)\s+-\s+(.+)')
matches = pattern.findall(text)

print(matches)

for i in ir:
    print(f'{matches[i-1][0]} - {matches[i-1][1]}')

# Создаем словарь с именами пользователей и их ролями
# winners = {name: role for name, role in matches}
# # Выводим результат
# print("Победители и их роли:")
# for name, role in winners.items():
#     print(f"{name} - {role}")
