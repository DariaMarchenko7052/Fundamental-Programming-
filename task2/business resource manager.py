from collections import deque

# --- 1. ООП: Класс Работника ---
class Employee:
    def __init__(self, name, department, base_salary, kpi):
        self.name = name
        self.department = department
        self.base_salary = base_salary
        self.kpi = kpi  # Показатель эффективности в %
        
        # 3. ARRAY (Массив): Хранение зарплат по месяцам
        self.monthly_salaries = [] 
        
        # 5. LINKEDLIST (Связный список / FIFO очередь): Задачи
        self.tasks = deque()

    def get_calculated_salary(self):
        """ 6. IF-ELSE: Логика начисления бонуса по KPI """
        if self.kpi >= 90:
            bonus = self.base_salary * 0.20  # +20% премия
            total_salary = self.base_salary + bonus
            return total_salary
        else:
            return self.base_salary

    def add_salary_to_history(self):
        """Добавляет текущую рассчитанную зарплату в массив месяцев"""
        current = self.get_calculated_salary()
        self.monthly_salaries.append(current)

    def add_task(self, task_name):
        self.tasks.append(task_name)

    def complete_task(self):
        """Очередь FIFO: берем задачу с начала (слева)"""
        if self.tasks:
            return self.tasks.popleft()
        return None

    def __repr__(self):
        # Показываем статус (с бонусом или без)
        status = " С премией!" if self.kpi >= 90 else "Стандарт"
        return f"[{self.department}] {self.name} | ЗП: {self.get_calculated_salary()} грн ({status}) | Задач в очереди: {len(self.tasks)}"


# --- 1. ООП: Класс Менеджера ---
class BusinessManager:
    def __init__(self):
        # 4. LIST (Список): База работников
        self.employees = []

    def add_employee(self, name, dept, salary, kpi):
        emp = Employee(name, dept, salary, kpi)
        self.employees.append(emp)
        print(f" Добавлен работник: {name}")

    def search_employee(self, search_name):
        """ :Поиск по имени """
        results = [e for e in self.employees if search_name.lower() in e.name.lower()]
        return results

    def sort_by_salary(self):
        """ Сортировка по итоговой зарплате (по убыванию) """
        if self.employees:
            self.employees.sort(key=lambda emp: emp.get_calculated_salary(), reverse=True)
            print("↕️ База отсортирована по зарплатам (от больших к меньшим).")
        else:
            print("База пуста.")

    def remove_employee(self, name):
        """ БОНУС: Удаление из базы """
        initial_count = len(self.employees)
        self.employees = [e for e in self.employees if e.name.lower() != name.lower()]
        if len(self.employees) < initial_count:
            print(f"️ Работник {name} удален из системы.")
        else:
            print(f" Работник {name} не найден.")

    def display_all(self):
        print("\n--- База сотрудников ---")
        if not self.employees:
            print("Пусто.")
        for emp in self.employees:
            print(emp)
        print("------------------------\n")


# --- 7. WHILE: Основной цикл программы ---
def main():
    manager = BusinessManager()
    
    # Добавим тестовые данные сразу для удобства
    manager.add_employee("Анна", "IT", 50000, 95)   # Получит премию (KPI > 90)
    manager.add_employee("Иван", "HR", 45000, 80)   # Без премии
    manager.add_employee("Олег", "IT", 55000, 92)   # Получит премию

    while True:
        print("\n=== Business Resource Manager ===")
        print("1. Показать всех сотрудников")
        print("2. Добавить сотрудника")
        print("3. Найти сотрудника по имени")
        print("4. Сортировать по зарплате")
        print("5. Удалить сотрудника")
        print("6. Добавить задачу Анне (Тест FIFO)")
        print("7. Выполнить задачу Анны (Тест FIFO)")
        print("0. Выйти")
        
        choice = input("Выберите действие (0-7): ")

        if choice == '1':
            manager.display_all()
        
        elif choice == '2':
            name = input("Имя: ")
            dept = input("Отдел: ")
            salary = float(input("Базовая зарплата: "))
            kpi = float(input("Текущий KPI (0-100): "))
            manager.add_employee(name, dept, salary, kpi)
        
        elif choice == '3':
            name = input("Введите имя для поиска: ")
            found = manager.search_employee(name)
            if found:
                for f in found: print(f)
            else:
                print("Никто не найден.")
                
        elif choice == '4':
            manager.sort_by_salary()
            manager.display_all()
            
        elif choice == '5':
            name = input("Кого удалить (точное имя)?: ")
            manager.remove_employee(name)
            
        elif choice == '6':
            # Демонстрация LinkedList
            anna = manager.employees[0] # Берем первого для теста
            task = input("Введите название задачи: ")
            anna.add_task(task)
            print(f" Задача '{task}' добавлена в очередь Анны.")
            
        elif choice == '7':
            anna = manager.employees[0]
            task = anna.complete_task()
            if task:
                print(f" Анна выполнила задачу: {task}")
            else:
                print("У Анны нет задач в очереди.")
                
        elif choice == '0':
            print("Выход из программы...")
            break  # Выход из цикла while
            
        else:
            print(" Неверный ввод, попробуйте еще раз.")

if __name__ == "__main__":
    main()
