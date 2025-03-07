## Zadanie 1
# numbers = [3, 7, 2, 8, 5, 10]
# numbers.append(12)
# numbers.remove(7)
# numbers.sort()
# najwieksza_wartosc = max(numbers)
# najmniejsza_wartosc = min(numbers)
# print(numbers)
# print(najwieksza_wartosc)
# print(najmniejsza_wartosc)

## Zadanie 2
# numbers = [12, 5 , 8, 3, 17, 24, 1, 9]
# even_numbers = [num for num in numbers if num%2==0]
# print(even_numbers)

## Zadanie 3
# numbers = [1, 2, 3, 4, 5]
# sqr_numbers = [num**2 for num in numbers]
# print(sqr_numbers)

## Zadanie 4
# words = ["Python", "is", "great"]
# dlugosc = [len(word) for word in words]
# print(dlugosc)

## Zadanie 5
# values = [4, 2, 8, 4, 2, 9, 1, 8]
# unique_values = list(dict.fromkeys(values))
# print(unique_values)

## Zadanie 6
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# middle_value = matrix[1][1]
# print(middle_value)
# sum_matrix = sum(sum(row) for row in matrix)
# print(sum_matrix)

## Zadanie 7
# data = (10, 20, 30, 40, 50)
# #data[1]=25
# data_list = list(data)
# data_list[1]=25
# data=tuple(data_list)
# print(data)

## Zadanie 8
# coordinates = (15.5, 42.3)
# x,y = coordinates
# print(x,y)

## Zadanie 9
# a = (1, 2, 3)
# b = (4, 5, 6)
# krotka = a+b
# print(krotka)
# print(3 in a)

## Zadanie 10
# student = {"name": "Anna", "age": 22, "major": "Computer Science"}
# student["grades"] = [4.5, 5.0, 3.5]
# student["age"] = 23
# del student["major"]
# # student.pop("major")
# print(student)

## Zadanie 11
# words = ["apple", "banana", "apple", "orange", "banana", "apple"]
# appearance = {}
# appearance = {word: words.count(word) for word in set(words)}
# # for word in set(words):
# #     appearance[word] = words.count(word)
# print(appearance)

## Zadanie 12
# person = {"name": "John", "age": 30, "city": "New York"}
# for key,value in person.items():
#     print(key +": " + str(value))

## Zadanie 13
# students = {
#     "Alice": {"math": 4, "english": 5, "history": 3},
#     "Bob": {"math": 3, "english": 3, "history": 4}
# }
# students["Andrzej"] = {"math":5, "english": 5, "history": 5}
# average = {name: sum(grades.values())/len(grades) for name, grades in students.items()}
# print(average)

## Zadanie 14
# colors = {"red": "#FF0000", "green": "#00FF00", "blue": "#0000FF"}
# new_colors = {value: key for key,value in colors.items()}
# print(new_colors)

## Zadanie 15
numbers = {"a": 2, "b": 3, "c": 4}
sqr_numbers = {key: value**2 for key, value in numbers.items()}
print(sqr_numbers)

