def count_appearances(data):  # Формирование словаря, который считает количество вхождений того или иного значения
    result = {}
    for x in data:
        if x not in result:
            result[x] = 1
        else:
            result[x] += 1
    return result


def mode_stat(data):  # Мода выборки
    data_dict = count_appearances(data)
    modes = []
    max_count = 0

    for key in data_dict:
        if data_dict[key] > max_count:
            max_count = data_dict[key]
            modes.clear()
            modes.append(key)
        elif data_dict[key] == max_count:
            modes.append(key)
    return modes


def median(data):  # Вычисление медианы
    data.sort()
    if len(data) % 2 == 0:
        return (data[int(len(data)/2) - 1] + data[int(len(data)/2)]) / 2
    else:
        return data[(int(len(data) + 1) / 2 - 1)]


def arithmetic_average(data):  # Среднее арифметическое
    return sum(data)/len(data)


def variance_sampling(data):  # Дисперсия для выборки (корректировка по n-1)
    avg = arithmetic_average(data)
    t_sum = 0
    for x in data:
        t_sum += ((x - avg) ** 2)
    return t_sum/(len(data)-1)


def standard_deviation(data):  # Среднеквадратическое отклонение для выборки (корректировка по n-1)
    return variance_sampling(data)**0.5


def range_sampling(data):  # Размах выборки
    return max(data)-min(data)


def standard_error(data):  # Стандартное отклонение
    return standard_deviation(data)/(len(data)**0.5)


def z_transformation(data, avg_general):
    return (arithmetic_average(data) - avg_general)/standard_error(data)


sample_data = [1, 5, 2, 7, 1, 9, 3, 8, 5, 9]

print(standard_deviation(sample_data))
print(range_sampling(sample_data))
print(mode_stat(sample_data))
print(median(sample_data))
