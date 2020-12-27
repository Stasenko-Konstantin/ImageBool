proc start(arr1, arr2: seq[int]) =
  echo """

1 - Пересечение
2 - Слияние
3 - Исключающее или
4 - Отрицание 1
5 - Отрицание 2
6 - Выход
7 - Повтор"""

proc fileToV(name: string): seq[int] =
  var arr: seq[int]
  var file: string = readFile(name)
  for i in file:
    if i == '0':
      arr.add(0)
    elif i == '1':
      arr.add(1)
  return arr

let arr1: seq[int] = fileToV("i1.txt") 
let arr2: seq[int] = fileToV("i2.txt")

start(arr1, arr2)