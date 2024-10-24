def math_relev(n_value, a_values, d_strings):
    relevant = []
    for symbol in d_strings:
        relevant_value = 0
        for i in range(n_value):
            relevant_value += a_values[i] * symbol[i]
        relevant.append((symbol, relevant_value))
    relevant.sort(key=lambda x: x[1], reverse=True)
    return relevant
def form_relev_values(n_value, a_values, d_strings, q_array):
    anser = []
    for element in q_array:
        if element[0] == 1:
            relevant = math_relev(n_value, a_values, d_strings)
            relevant.sort(key = lambda x: x[1], reverse=True)
            max_value = [x[0] for x in relevant[:element[1]]]
            anser.append(max_value)
        if element[0] == 2:
            for key,value in enumerate(d_strings):
                if key == element[1]:
                    for i,step in enumerate(value):
                        if step == element[2]:
                            value[i] = element[3]
    return anser

def imput_values(n_value):
    a_values = list(map(int, input("Параметры:").split()))[:n_value]
    while 10^8 < n_value < 0:
        a_values = list(map(int, input("Параметры:").split()))[:n_value]
    d_value = int(input("Количество обьектов для ранжирования:"))
    while 100000 < d_value < 0 and d_value * n_value > 100000:
        d_value = int(input("Количество обьектов для ранжирования:"))
    d_strings = []
    for _ in range(d_value):
        i_object = list(map(int, input("i-обьекты:").split()))[:n_value]
        while 100000000 < sum(i_object) < 0:
            i_object = list(map(int, input("i-обьекты:").split()))[:n_value]
        d_strings.append(i_object)
    q_value = int(input("Количество запросов к системе ранжировки:"))
    while 100000 < q_value < 0 :
        q_value = int(input("Количество запросов к системе ранжировки:"))
    q_array = []
    for _ in range(q_value):
        q_object = list(map(int, input("Запрос:").split()))
        q_array.append(q_object)
    anser = form_relev_values(n_value, a_values, d_strings, q_array)
    print(anser)


n_value = int(input("Количество параметров в формуле ранжирования:"))
while 100 < n_value < 1:
    n_value = int(input("Количество параметров в формуле ранжирования:"))
imput_values(n_value)