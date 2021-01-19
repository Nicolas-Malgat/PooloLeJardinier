from vegetables.vegetable import Vegetable
import vegetables as veg

class Garden:
    vegetable_types_counter = int(0)
    vegetable_types_list = list()

    def __init__(self, size=30) -> None:
        self.__size = size

        self.plantation = list()

    def add(self, cls):
        if not isinstance(cls, veg.Vegetable):
            return

        if (self.get_nb_graine() + cls.get_nb_graine()) not in range(self.__size):
            difference = self.__size - self.get_nb_graine()

            # print('/!\ Difference de', difference)

            reste = type(cls)(cls.get_nb_graine() - difference) # instancie un nouveau veg

            cls.set_nb_graine(difference)
            self.__add_vegetable(cls)

            return reste

        self.__add_vegetable(cls)
        return None

    def __add_vegetable(self, veg: Vegetable):
        if type(veg) not in Garden.vegetable_types_list:
            Garden.vegetable_types_counter += 1
            Garden.vegetable_types_list.append(type(veg))
        self.plantation.append(veg)

    def get_nb_graine(self):
        return sum(
            [legume.get_nb_graine() for legume in self.plantation]
        )
