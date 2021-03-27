# LAB 2 TASK 1

# languages = ["Python", "C#", "JS", "PHP", "Java"]
#
# print(type(languages))
# print(' '.join(map(str, languages)))
# print(languages[0] + ' ' + languages[len(languages) - 1])
#
# languages.append('C++')
#
# print(' '.join(map(str, languages)))
#
# print(languages.count('Python'))
#
# languages.append('Python')
# languages.append('Python')
# languages.append('Python')
#
# print(languages.count('Python'))
#
# more = ["Rust", "Cobol"]
#
# languages.extend(more)
#
# print(' '.join(map(str, languages)))
#
# newLanguages = []
#
# for i in range(len(languages)):
#     if newLanguages.count(languages[i]) == 0:
#         newLanguages.append(languages[i])
#
# print(' '.join(map(str, newLanguages)))

# LAB 2 TASK 3
# text = input("Podaj ciag z przecinakimi: ")
#
# elements = text.split(',')
#
# for i in range(len(elements)):
#     elements[i] = str(i) + elements[i]
#
# newText = ','.join(elements)
#
# print(text)
# print(newText)

# LAB 2 TASK 5 - not finished
# number = int(input("Podaj ilosc list: "))
#
# source = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
#
# n = 0
# nElements = len(source) / number
# print(nElements)
# listOfList = []
#
# tempList = []
#
# for i in range(len(source) - 1):
#     tempList.append(source[i])
#     if i > nElements * n:
#         listOfList.append(tempList)
#         tempList = []
#         n = n + 1
#
# print(','.join(source))
# print(listOfList)

# LAB 2 TASK 6
# employee = {
#     'imie': 'Julia',
#     'nazwisko': 'Nowak',
#     'miasto': 'Poznań',
#     'imionaDzieci': ['Anna', 'Paweł', 'Dariusz']
# }
#
# print(employee)
# print(type(employee))
#
# print(employee['imionaDzieci'])
# print(employee['imionaDzieci'][1])
#
# employee['telefon'] = '999888777'
# employee['wiek'] = 32
# del employee['imionaDzieci']
#
# print(employee)


def division(a, b):
    if b == 0:
        return "Error division by 0"
    else:
        return a / b


print(division(49, 0))
