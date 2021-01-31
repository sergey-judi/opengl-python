from abc import ABC, abstractmethod


class IDrawable(ABC):

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def get_point_data(self):
        pass

