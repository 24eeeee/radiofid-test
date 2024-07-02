import queue

import src.utils as utils


class Conveyor:
    """
    Класс конвейера, с методом run, поэтапно выполняющим задачи из очереди
    """

    def __init__(self):
        self.q = queue.Queue()
    
    def run(self):
        while not self.q.empty():
            task, args = self.q.get()
            if task not in utils:
                raise ValueError(f'No such util for task {task}')

            task.execute(*args)
