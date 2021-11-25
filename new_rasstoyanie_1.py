# Программа принимает два многоугольника ("kvadr" и "treug"), которые задаются через список вершин.
# Кадая вершина задаётся списком, содержащим два элемента, которые являются координатами вершины.
# Вершины для каждого многоугольника указываются последовательно по часовой стрелке или против.
#
# Сначала программа находит минимальное расстояние между всеми парами вершин.
#
# Затем программа последовательно для каждой вершины второго многоугольника и каждого ребра первого многоугольника
# проверяет, куда попадает перпендикуляр, опущенный из данной вершины на прямую, которой принадлежит данное ребро.
# Это делается с помощью функции proekcia_na_otrezok().
# Если он попадает на само ребро (за исключением его крайних точек), то с помощью функции rasst_point_line()
# измеряется расстояние от вершины до ребра, и это расстояние добавляется в список array_rasst_point_line.
# Крайние точки ребра исключаются, поскольку, если перпендикуляр попадает в одну из них, то это соответствует ситуации
# расчёта расстояния между двумя вершинами двух многоугольников, что уже сделано ранее.
#
# Далее фигуры меняются ролями, и проводится проверка и, при необходимости, измерение и добавление в список
# расстояния от вершин первого многоугольника до рёбер второго.
#
# Когда проверены все возможные пары вершин и рёбер, полученный массив расстояний сортируется, выводя на первую
# позицию минимальное расстояние.
#
# На последнем шаге сравнивается минимальное расстояние между парами вершин и минимальное расстояние
# между парами вершин и рёбер.
# Наименьшее из них выводится как результат работы программы.


import sys
import math


def take_data():
    str_1 = ''
    str_2 = ''

    file_in = open('input_points.txt')
    str_1 = file_in.readline()
    str_2 = file_in.readline()
    file_in.close()


    lst_1 = str_1.split()
    lst_2 = str_2.split()


    def is_number(str):
        try:
            float(str)
            return True
        except ValueError:
            return False

    def input_to_int_list(lst_1):
        points_for_fig = []
        for i in lst_1:
            tmp_str_2 = ''
            for j in i:
                if j != ',' and j != ' ':
                    tmp_str_2 += j
            if is_number(tmp_str_2):
                tmp_lst = int(tmp_str_2)
                points_for_fig.append(tmp_lst)
        return points_for_fig

    points_for_fig_1 = []
    points_for_fig_1 = input_to_int_list(lst_1)


    points_for_fig_2 = []
    points_for_fig_2 = input_to_int_list(lst_2)


    a = 0
    b = 0
    if len(points_for_fig_1) % 2 == 0:
        a = 1

    if len(points_for_fig_2) % 2 == 0:
        b = 1

    if a == 1 and b == 1:
        return points_for_fig_1, points_for_fig_2
    elif a != 1 and b == 1:
        print('Первый набор координат содержит нечётное количество точек')
        print('Работа программы остановлена')
        sys.exit()
    elif a == 1 and b != 1:
        print('Второй набор координат содержит нечётное количество точек')
        print('Работа программы остановлена')
        sys.exit()
    elif a != 1 and b != 1:
        print('Оба набора координат содержат нечётное количество точек')
        print('Работа программы остановлена')
        sys.exit()


def points_to_coords(arr_1):
    kvadr = []
    k = -1
    for i in range(len(arr_1)):
        if i % 2 == 0:
            kvadr.append([0, 0])
            k += 1
            kvadr[k][0] = arr_1[i]
        else:
            kvadr[k][1] = arr_1[i]
    return kvadr

def calculate_distance(kvadr, treug):
    # координаты вершин двух многоугольников
    #kvadr = [[-7, -1], [-7, 3], [-1, -1], [-6, -2]]
    #treug = [[0, 0], [10, 10], [11, 10], [40, 0], [39, -1]]

    min_rasst = 0
    first = True

    # поиск минимального расстояния между парами вершин
    for kv_v in kvadr:
        for tr_v in treug:
            if first:
                min_rasst = math.sqrt((tr_v[0] - kv_v[0]) ** 2 + (tr_v[1] - kv_v[1]) ** 2)
            else:
                current_rasst = math.sqrt((tr_v[0] - kv_v[0]) ** 2 + (tr_v[1] - kv_v[1]) ** 2)
                if current_rasst < min_rasst:
                    min_rasst = current_rasst
            first = False


    kvadrat = []
    treugol = []

    for i in kvadr:
        kvadrat.append(i)
    kvadrat.append(kvadr[0])

    for i in treug:
        treugol.append(i)
    treugol.append(treug[0])

    # функцмя расчёта расстояния от точки до прямой
    def rasst_point_line(pointX, pointY, lineX1, lineY1, lineX2, lineY2):
        a = lineY2 - lineY1
        b = lineX1 - lineX2
        c = lineX2 * lineY1 - lineX1 * lineY2
        dis = (math.fabs(a * pointX + b * pointY + c)) / (math.pow(a * a + b * b, 0.5))
        return dis

    # функция, которая проверяет, попадает ли перпендикуляр, опущенный из точки на прямую,
    # непосредственно на ребро многоугольника
    def proekcia_na_otrezok(pointX, pointY, lineX1, lineY1, lineX2, lineY2):
        if 0 < (lineX2 - pointX) * (lineX2 - lineX1) + (lineY2 - pointY) * (lineY2 - lineY1) < (lineX2 - lineX1) * (
                lineX2 - lineX1) + (lineY2 - lineY1) * (lineY2 - lineY1):
            return True

    array_rasst_point_line = []

    # нахождение расстояний от вершин второго многоугольника до рёбер первого многоугольника
    for i in treug:
        for j in range(len(kvadrat) - 1):
            if proekcia_na_otrezok(i[0], i[1], kvadrat[j][0], kvadrat[j][1], kvadrat[j + 1][0],
                                   kvadrat[j + 1][1]) is True:
                array_rasst_point_line.append(
                    rasst_point_line(i[0], i[1], kvadrat[j][0], kvadrat[j][1], kvadrat[j + 1][0], kvadrat[j + 1][1]))

    # нахождение расстояний от вершин первого многоугольника до рёбер второго многоугольника
    for i in kvadr:
        for j in range(len(treugol) - 1):
            if proekcia_na_otrezok(i[0], i[1], treugol[j][0], treugol[j][1], treugol[j + 1][0],
                                   treugol[j + 1][1]) is True:
                array_rasst_point_line.append(
                    rasst_point_line(i[0], i[1], treugol[j][0], treugol[j][1], treugol[j + 1][0], treugol[j + 1][1]))


    array_rasst_point_line.sort()


    if len(array_rasst_point_line) == 0:
        print(min_rasst)
        return min_rasst
    else:
        if min_rasst <= array_rasst_point_line[0]:
            print(min_rasst)
            return min_rasst
        else:
            print(array_rasst_point_line[0])
            return min_rasst


def main():
    arr_1, arr_2 = take_data()

    kvadr = points_to_coords(arr_1)
    treug = points_to_coords(arr_2)

    result = calculate_distance(kvadr, treug)

    return result


main()

