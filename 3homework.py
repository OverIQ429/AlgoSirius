def get_relevance(weights, features):
  """
  Вычисляет релевантность объекта по формуле.

  Args:
    weights: Список весов для каждого признака.
    features: Список значений признаков объекта.

  Returns:
    Релевантность объекта.
  """
  return sum(w * f for w, f in zip(weights, features))

def process_query(weights, objects, query):
  """
  Обрабатывает запрос.

  Args:
    weights: Список весов для каждого признака.
    objects: Список объектов.
    query: Запрос.

  Returns:
    Список индексов самых релевантных объектов,
    или None, если запрос на изменение признака.
  """
  if query[0] == 1:
    # Запрос на выдачу самых релевантных объектов
    relevances = [get_relevance(weights, obj) for obj in objects]
    sorted_indices = sorted(range(len(objects)), key=lambda i: relevances[i], reverse=True)
    return sorted_indices[:query[1]]
  elif query[0] == 2:
    # Запрос на изменение признака
    objects[query[1] - 1][query[2] - 1] = query[3]
    return None
  else:
    raise ValueError("Неверный тип запроса")

n = int(input("Количество параметров в формуле ранжирования:"))
weights = list(map(int, input().split()))
d = int(input("оличество обьектов для ранжирования:"))
objects = [list(map(int, input().split())) for _ in range(d)]
q = int(input("Количество запросов к системе ранжировки:"))

for _ in range(q):
  query = list(map(int, input().split()))
  result = process_query(weights, objects, query)
  if result is not None:
    print(*result)