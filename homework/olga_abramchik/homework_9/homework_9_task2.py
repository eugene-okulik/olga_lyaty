# Есть такой список:
# temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22,
#                 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]
# С помощью функции map или filter создайте из этого списка новый список с жаркими днями.
# Будем считать жарким всё, что выше 28.
# Распечатайте из нового списка самую высокую температуру самую низкую и среднюю


temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27,
                22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]

hot_temperatures = filter(lambda t: t > 28, temperatures)

hot_temperatures_new = list(hot_temperatures)
print('Список с жаркими днями: ', hot_temperatures_new)
print('Максимальная температура: ', max(hot_temperatures_new))
print('Минимальная температура: ', min(hot_temperatures_new))
print('Средняя температура: ', round((sum(hot_temperatures_new) / len(hot_temperatures_new)), 1))
