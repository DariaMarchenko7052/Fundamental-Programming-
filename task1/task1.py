class Student:
    def __init__(self, first_name, last_name, student_id, avg_grade, passport, science_work):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id
        self.avg_grade = avg_grade
        self.passport = passport
        self.science_work = science_work

    def show_info(self):
        print(f"{self.first_name} {self.last_name} | Балл: {self.avg_grade}")


group = [
    Student("Анна", "Иванова", "ST001", 91, "МК123456", True),
    Student("Игорь", "Петров", "ST002", 78, "МК654321", False),
    Student("Мария", "Сидорова", "ST003", 88, "МК111222", True),
    Student("Олег", "Коваленко", "ST004", 84, "МК333444", False),
    Student("Елена", "Мороз", "ST005", 95, "МК555666", True),
    Student("Дмитрий", "Литвин", "ST006", 87, "МК777888", False),
    Student("Светлана", "Бондарь", "ST007", 82, "МК999000", False),
]


# отбираем стипендиатов
def split_students(students):
    normal = []     # обычная стипендия
    advanced = []   # Кабмин/Президент
    failed = []      # не прошли

    for st in students:
        if st.avg_grade > 85:
            normal.append(st)  # все с баллом >85 получают обычную

            if st.science_work:
                advanced.append(st)  # + научка - специальная
        else:
            failed.append(st)

    return normal, advanced, failed


normal_list, advanced_list, failed_list = split_students(group)


# сортировка (по убыванию)
normal_list.sort(key=lambda st: st.avg_grade, reverse=True)
advanced_list.sort(key=lambda st: st.avg_grade, reverse=True)


print("ПРОШЛИ на обычну стипендию:")
for st in normal_list:
    st.show_info()


print("\nКАНДИДАТЫ на стипнедию президента Украины илим кабинета министров Укоаины:")
for st in advanced_list:
    st.show_info()


print("\nНЕ ПРОШЛИ:")
for st in failed_list:
    st.show_info()


print("\nПроверка через while (не прошли):")
i = 0
while i < len(failed_list):
    st = failed_list[i]
    print(f"{st.first_name} {st.last_name} - не прошёл")
    i += 1
