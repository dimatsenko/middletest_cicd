from task_manager import TaskManager


def main():
    manager = TaskManager()

    while True:
        print("\n--- Task Management System ---")
        print("1. Додати завдання")
        print("2. Видалити завдання")
        print("3. Показати список (за пріоритетом)")
        print("4. Показати список (за датою)")
        print("5. Виконати та видалити завдання")
        print("0. Вихід")

        choice = input("\nОберіть дію: ")

        if choice == '1':
            desc = input("Введіть опис: ")
            try:
                prio = int(input("Пріоритет (1-5): "))
                if 1 <= prio <= 5:
                    new_id = manager.add_task(desc, prio)
                    print(f"Успішно! Створено завдання з ID: {new_id}")
                else:
                    print("Помилка: Пріоритет має бути від 1 до 5.")
            except ValueError:
                print("Помилка: Введіть ціле число.")

        elif choice == '2':
            try:
                tid = int(input("Введіть ID завдання для видалення: "))
                if manager.delete_task(tid):
                    print("Завдання видалено.")
                else:
                    print("Завдання з таким ID не знайдено.")
            except ValueError:
                print("Помилка: ID має бути числом.")

        elif choice in ['3', '4']:
            sort_type = 'priority' if choice == '3' else 'date'
            tasks = manager.get_sorted_tasks(sort_by=sort_type)
            if not tasks:
                print("Список порожній.")
            else:
                for task in tasks:
                    print(task)

        elif choice == '5':
            try:
                tid = int(input("Введіть ID виконаного завдання: "))
                if manager.mark_completed(tid):
                    print(f"Завдання {tid} виконано та прибрано зі списку.")
                else:
                    print("ID не знайдено.")
            except ValueError:
                print("Помилка: Введіть коректне ID.")

        elif choice == '0':
            print("До побачення!")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")


if __name__ == "__main__":
    main()