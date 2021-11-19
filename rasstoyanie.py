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


import math

# координаты вершин двух многоугольников
kvadr = [[-7, -1], [-7, 3], [-1, -1], [-6, -2]]
treug = [[0, 0], [10, 10], [11, 10], [40, 0], [39, -1]]

min_rasst = 0
first = True

# поиск минимального расстояния между парами вершин
for kv_v in kvadr:
    for tr_v in treug:
        if first:
            min_rasst = math.sqrt((tr_v[0] - kv_v[0])**2 + (tr_v[1] - kv_v[1])**2)
        else:
            current_rasst = math.sqrt((tr_v[0] - kv_v[0]) ** 2 + (tr_v[1] - kv_v[1]) ** 2)
            if current_rasst < min_rasst:
                min_rasst = current_rasst
        first = False

print("Minimalnoe rasstoyanie mezdu parami vershin: ")
print(min_rasst)
print()

#
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
        if proekcia_na_otrezok(i[0], i[1], kvadrat[j][0], kvadrat[j][1], kvadrat[j + 1][0], kvadrat[j + 1][1]) is True:
            array_rasst_point_line.append(rasst_point_line(i[0], i[1], kvadrat[j][0], kvadrat[j][1], kvadrat[j + 1][0], kvadrat[j + 1][1]))

# нахождение расстояний от вершин первого многоугольника до рёбер второго многоугольника
for i in kvadr:
    for j in range(len(treugol) - 1):
        if proekcia_na_otrezok(i[0], i[1], treugol[j][0], treugol[j][1], treugol[j + 1][0], treugol[j + 1][1]) is True:
            array_rasst_point_line.append(rasst_point_line(i[0], i[1], treugol[j][0], treugol[j][1], treugol[j + 1][0], treugol[j + 1][1]))


print("Spisok rasstoyaniy mezdu vershinami i rebrami: ")
print(array_rasst_point_line)

array_rasst_point_line.sort()

print()
print("Etot ze spisok posle sortirovki: ")
print(array_rasst_point_line)
print()

if len(array_rasst_point_line) == 0:
    print("Minimalnoe rasstoyanie mezdu figurami =", round(min_rasst, 3))
else:
    if min_rasst <= array_rasst_point_line[0]:
        print("Minimalnoe rasstoyanie mezdu figurami =", round(min_rasst, 3))
    else:
        print("Minimalnoe rasstoyanie mezdu figurami =", round(array_rasst_point_line[0], 3))