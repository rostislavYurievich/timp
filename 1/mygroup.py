groupmates = [
    {
        "name": "Ростислав",
        "surname": "Рыков",
        "exams": ["История", "Физика", "Мат. анализ"],
        "marks": [3, 3, 3]
    },
    {
        "name": "Артем",
        "surname": "Кубышев",
        "exams": ["История", "Физика", "Мат. анализ"],
        "marks": [4, 2, 4]
    },
    {
        "name": "Макар",
        "surname": "Петров",
        "exams": ["История", "Физика", "Мат. анализ"],
        "marks": [5, 4, 5]
    },
    {
        "name": "Роман",
        "surname": "Ошкин",
        "exams": ["История", "Физика", "Мат. анализ"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Акбар",
        "surname": "Салиев",
        "exams": ["История", "Физика", "Мат. анализ"],
        "marks": [4, 4, 4]
    }
]

def func(mark):
    print("Имя".ljust(15), "Фамилия".ljust(10),"Экзамены".ljust(30),"Оценки".ljust(20))
    for i in groupmates:
        temp = i["marks"]
        if (sum(temp)/len(temp))>mark:
            print(str(i["name"]).ljust(15), str(i["surname"]).ljust(10),str(i["exams"]).ljust(30), str(i["marks"]).ljust(20))

a = int(input("Введите среднюю оценку "))
func(a);
