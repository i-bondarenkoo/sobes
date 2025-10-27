from enum import Enum


class TaskStatus(str, Enum):
    new = "new"
    done = "done"
    in_process = "in_process"


class Task:
    def __init__(self, title: str, description: str, priority: int):
        Task.verify_priority(priority)
        self.__title = title
        self.__description = description
        self.__priority = priority
        self.__status = TaskStatus.new

    @property
    def title(self):
        return self.__title

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, new_status):
        if isinstance(new_status, TaskStatus):
            self.__status = new_status
        elif isinstance(new_status, str):
            try:
                self.__status = TaskStatus(new_status.lower().strip())
            except ValueError:
                raise ValueError(f"Недопустимое значение статуса - {new_status}")
        else:
            raise TypeError("Статус должен быть строкой или объектом TaskStatus")

    @classmethod
    def verify_priority(cls, priority):
        if not isinstance(priority, int):
            raise TypeError("Приоритет должен быть целым числом")
        if not 1 <= priority <= 5:
            raise ValueError("Приоритет должен быть числом в диапазоне [1, 5]")

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, new_description):
        if not isinstance(new_description, str):
            raise TypeError("Описание должно быть строкой")
        if len(new_description) == 0:
            raise ValueError("Строка не должна быть пустой")
        self.__description = new_description

    def __str__(self):
        return f"Объект класса - {self.__class__.__name__}: название - {self.__title}, описание - {self.__description}, приоритет - {self.__priority}, статус задачи - {self.__status.value}"


class TaskManager:
    def __init__(self):
        self.tasks: list[Task] = []

    def add_task(self, task: Task):
        for elements in self.tasks:
            if elements.title == task.title:
                raise AttributeError("Задача с таким именем уже существует")
        if isinstance(task, Task):
            self.tasks.append(task)

    def add_more_tasks(self, *task):
        d1 = {}
        for elements in self.tasks:
            d1["title"] = elements.title
            print(d1)
        for new_el in task:
            if new_el.title in d1.keys():
                raise ValueError("Задача с таким названием уже добавлена в список")
            self.tasks.append(new_el)

    def __str__(self):
        values = "\n".join(str(task) for task in self.tasks)
        return f"Список {self.__class__.__name__}, элементы списка [{values}]"


t1 = Task("Тестовая задача 1", "Проверка", 4)
t2 = Task("Тестовая задача 1", "Проверка", 1)
t3 = Task("Тестовая задача 3", "Проверка", 2)

tm = TaskManager()
tm.add_task(t1)
tm.add_more_tasks(t1, t2)
print(tm)
