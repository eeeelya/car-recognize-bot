from abc import ABC


class Table(ABC):
    def __init__(self, conn):
        self.conn = conn

    def add_launch(self):
        pass