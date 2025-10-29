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

    @title.setter
    def title(self, new_title: str):
        if isinstance(new_title, str) and len(new_title) > 0:
            self.__title = new_title

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
    DEL_ELEM = "./? "

    def __init__(self):
        self.tasks: list[Task] = []

    def add_task(self, task: Task):
        if not isinstance(task, Task):
            raise TypeError("Задача должна быть объектом Task")
        for elements in self.tasks:
            if elements.title == task.title:
                raise AttributeError("Задача с таким именем уже существует")
        self.tasks.append(task)

    def find_task(self, title: str):
        if not isinstance(title, str):
            raise TypeError("Название задачи должно быть строкой")
        for task in self.tasks:
            if task.title == title:
                return task
        raise ValueError("Задача не найдена")

    def add_more_tasks(self, *task):
        d1 = {e1.title: e1.title for e1 in self.tasks}
        for e2 in task:
            if e2.title not in d1.keys():
                d1[e2.title] = e2.title
                self.tasks.append(e2)
            else:
                raise ValueError("Задача с таким названием уже существует")
        # print(d1)

    def remove_task(self, title: str):
        check_task = self.find_task(title)
        self.tasks.remove(check_task)

    def update_task(self, title: str, **kwargs):
        current_task = self.find_task(title)
        if kwargs.get("new_title") is not None:
            current_task.title = kwargs["new_title"]
        if kwargs.get("new_description") is not None:
            current_task.description = kwargs["new_description"]

    def __str__(self):
        values = "\n".join(str(task) for task in self.tasks)
        return f"Список {self.__class__.__name__}, элементы списка [{values}]"


t1 = Task("тестовая задача 1", "проверка", 4)
t2 = Task("тестовая задача 2", "проверка", 1)
t3 = Task("тестовая задача 3", "проверка", 2)
t4 = Task("написать декоратор", "декоратор для подсчета времени", 2)
tm = TaskManager()
tm.add_task(t3)
print(tm)
# tm.add_more_tasks(t2, t4)
# print(tm)
# print("-----")
# tm.remove_task("написать декоратор")
# print(tm)
tm.update_task("тестовая задача 3", new_description="22", new_title="jopa")
print(tm)
