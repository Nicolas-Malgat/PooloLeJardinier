from garden import Garden
import vegetables as veg
import itertools

class Gardener:
    def __init__(self, *gardens: Garden) -> None:

        self.gardens_list = gardens

        self.gardens = iter(gardens)
        self.mygarden = next(self.gardens)
        self.mygarden_index = 1
        print(f'Gardener works on Garden n°{self.mygarden_index}')


    def plant(self, *legumes: veg.Vegetable):
        """Recupere un instance du legume passe en parametre et 
        """
        legumes = [self.__get_vegetable(dict) for dict in legumes ]

        for leg in legumes:

            reste = self.mygarden.add(leg)
            print(f"Gardener plants {leg.get_nb_graine()} {type(leg).__name__}.s")

            if reste:
                legumes.insert(legumes.index(leg) + 1, reste)
                self.__next_garden()
                continue

    @staticmethod
    def __get_vegetable(legume_dict):
        
        legume = legume_dict['vegetable']

        nb_graine = 0
        try:
            nb_graine = legume_dict['nb_graine']
        except KeyError:
            pass

        vegetable_classes = {
            "tomato": veg.Tomato,
            "pickle": veg.Pickle,
            "carrot": veg.Carrot,
        }

        try:
            legume = vegetable_classes[legume](nb_graine)
        except KeyError:
            raise Exception("Ce legume n'existe pas !")
        
        return legume

    def __next_garden(self):
        try:
            self.mygarden = next(self.gardens)
        except StopIteration:
            raise Exception("Gardener doesnt have any garden to work :'(")
        
        self.mygarden_index += 1
        print(f'Gardener now works on Garden n°{self.mygarden_index}')

    def get_seed(self):
        count = sum(g.get_nb_graine() for g in self.gardens_list)
        jardins_utilises = [g for g in self.gardens_list if g.get_nb_graine() != 0]
        return f"{count} graines dans {len(jardins_utilises)} jardins ({len(self.gardens_list)} jardins disponibles)"
