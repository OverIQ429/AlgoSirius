import numpy as np

class Algoritm_without_grafs():
    def __init__(self, list, aim):
        self.matrix = list

    def max_el(self):
        max_el = []
        for el in self.matrix:
            max_check = 0
            numbs = [int(num) for num in str(el[0])]
            for step in numbs:
                if step > max_check:
                    max_check = step
            max_el.append(max_check)
        self.kill_all(max_el)

    def kill_all(self, max_el):
        new_matrix = []
        iter = -1
        for el in self.matrix:
            numbs = [int(num) for num in str(el[0])]
            matrix_lexel = []
            iter += 1
            for step in numbs:
                step = (step - max_el[iter]) * -1
                matrix_lexel.append(step)
            new_matrix.append(matrix_lexel)
        self.min_el_row(new_matrix)

    def min_el_row(self, new_matrix):
        for el in new_matrix:
            min_check = el[0]
            for step in el:
                if step < min_check:
                    min_check = step
            for step in el:
                step -= min_check
        self.min_el_columb(new_matrix)

    def min_el_columb(self, new_matrix):
        for j in range(len(new_matrix[0])):
            min_check = new_matrix[0][j]
            for i in range(len(new_matrix)):
                step = new_matrix[i][j]
                if step < min_check:
                    min_check = step
            for i in range(len(new_matrix)):
                new_matrix[i][j] = new_matrix[i][j] - min_check
        self.alone_ziro(new_matrix)

    def create_empty_matrix(self, matrix):
        new_check_matrix = []
        for el in matrix:
            local_massiv = []
            for step in el:
                if step != 0:
                    local_massiv.append(1)
                else:
                    local_massiv.append(0)
            new_check_matrix.append(local_massiv)
        return new_check_matrix

    def create_another_matrix(self, matrix):
        new_check_matrix = []
        for el in matrix:
            local_massiv = []
            for step in el:
                local_massiv.append(step)
            new_check_matrix.append(local_massiv)
        return new_check_matrix

    def close_elements(self, matrix):
        matrix = np.array(matrix)
        rows, cols = matrix.shape
        zeros = [(i, j) for i in range(rows) for j in range(cols) if matrix[i][j] == 0]

        # Список для хранения закрытых элементов
        closed_elements = set()
        used_zeros = []
        # Используем доступные нули, чтобы закрыть элементы
        used_rows = set()
        used_cols = set()

        for zero in zeros:
            i, j = zero
            if i not in used_rows and j not in used_cols:
                # Закрываем все элементы в строке и столбце
                for col in range(cols):
                    closed_elements.add((i, col))
                    matrix[i][col] = -1  # Закрашиваем элемент
                for row in range(rows):
                    closed_elements.add((row, j))
                    matrix[row][j] = -1  # Закрашиваем элемент
                used_rows.add(i)
                used_cols.add(j)
                used_zeros.append(zero)
            # Ограничиваем количество используемых нулей
            if len(used_rows) >= len(zeros):
                break

        return matrix, used_zeros

    def alone_ziro(self, matrix):
        new_check_matrix, used_zeros = self.close_elements(matrix)
        all_zeros = np.all(new_check_matrix == -1)
        if all_zeros:
            self.anser(matrix, used_zeros)
        else:
            another_matrix = self.create_another_matrix(matrix)
            for colo in range(len(another_matrix)):
                colom = []
                for el in another_matrix:
                    colom.append(el[colo])
                count_of_zeros = colom.count(0)
                if count_of_zeros > 1:
                    for el in another_matrix:
                        el[colo] = "n"
            save_zone = []
            for j in range(len(another_matrix)):
                count_of_zeros = another_matrix[j].count(0)
                if count_of_zeros > 0:
                    for i in range(len(another_matrix[j])):
                        if another_matrix[j][i] == "n":
                            save_zone.append((j, i))
                        else:
                            another_matrix[j][i] = "n"
            min_check = 0
            for el in another_matrix:
                for step in el:
                    if step != "n":
                        min_check = step
            for el in another_matrix:
                for step in el:
                    if step != "n":
                        if step < min_check:
                            min_check = step
            new_another_matrix = []

            for el in another_matrix:
                local_val = []
                for step in el:
                    if step != "n":
                        step -= min_check
                    local_val.append(step)
                new_another_matrix.append(local_val)
            self.anser1(new_another_matrix, save_zone, min_check, matrix)

    def anser1(self, new_matrix, save_zone, min, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                for g in range(len(new_matrix)):
                    for h in range(len(new_matrix[g])):
                        if i == g and j == h and new_matrix[g][h] != "n":
                            matrix[i][j] = new_matrix[g][h]
        for s in save_zone:
            matrix[s[0]][s[1]] += min
        self.alone_ziro(matrix)

    def anser(self, matrix, used_zeros):
        full_sum = 0
        new_matrix = []
        for zeros in used_zeros:
            print(zeros[0] + 1,zeros[1] + 1)
            for el in self.matrix:
                numbs = [int(num) for num in str(el[0])]
                new_matrix.append(numbs)
            full_sum += new_matrix[zeros[0]][zeros[1]]
        print(full_sum)

list = [[73695],
        [75756],
        [76889],
        [31657],
        [24995]]
Algor = Algoritm_without_grafs(list, min)
Algor.max_el()
