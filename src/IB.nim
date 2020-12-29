import math

proc imprint(arr1, arr2: seq[int]) = 
  
  proc help(arr: seq[int], i: int) = 
    if arr[i] == 0:
      write(stdout, "-")
    else:
      write(stdout, "#")

  var 
    i = 0
    j = 0
    l = 79
  while i < 3082:
    if i == 0 and j == 0:
      write(stdout, "")
    elif i < l and j == 0:
      help(arr1, i)
    elif i == l and j == 0:
      write(stdout, " | ")
      j = 1
      i = l - 79
    elif i < l and i >= 0 and j == 1:
      help(arr2, i)
    elif i == l and j == 1:
      j = 0
      l += 79
      write(stdout, "\n")
    i += 1

proc start(arr1, arr2: seq[int]) =
  imprint(arr1, arr2)
  echo """

1 - Пересечение
2 - Слияние
3 - Исключающее или
4 - Отрицание 1
5 - Отрицание 2
6 - Выход
7 - Повтор"""

  case readLine(stdin)
  of "1": first(arr1, arr2)
  of "2": second(arr1, arr2)
  of "3": third(arr1, arr2)
  of "4": fourth(arr1, arr2)
  of "5": fourth(arr2, arr1)
  of "6": quit(QuitSuccess)
  of "7": main()
  else: start(arr1, arr2)

proc first(arr1, arr2: seq[int]) =
  var
    arr1 = arr1
    arr2 = arr2
  for i in 0..arr1.len:
    arr1[i] = arr1[i] * arr2[i]
  start(arr1, arr2)

proc second(arr1, arr2: seq[int]) =
  var
    arr1 = arr1
    arr2 = arr2
  for i in 0..arr1.len:
    if arr1[i] == 1 or arr2[i] == 1:
      arr1[i] = 1
    else:
      arr1[i] = 0
  start(arr1, arr2)

proc third(arr1, arr2: seq[int]) =
  var
    arr1 = arr1
    arr2 = arr2
  for i in 0..arr1.len:
    arr1[i] = (arr1[i] - arr2[i]) ^ 2
  start(arr1, arr2)

proc fourth(arr1, arr2: seq[int]) =
  var
    arr1 = arr1
    arr2 = arr2
  for i in 0..arr1.len:
    if arr1[i] == 0:
      arr1[i] = 1
    else:
      arr1[i] = 0
  start(arr1, arr2)

proc fileToV(name: string): seq[int] =
  var 
    arr: seq[int]
    file: string = readFile(name)
  for i in file:
    if i == '0':
      arr.add(0)
    elif i == '1':
      arr.add(1)
  return arr

proc main() =
  var 
    arr1: seq[int] = fileToV("i1.txt") 
    arr2: seq[int] = fileToV("i2.txt")

  start(arr1, arr2)

main()