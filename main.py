import vegetables as veg
from gardener import Gardener
from garden import Garden

garden1 = Garden(size=1)
garden2 = Garden(size=1)
garden3 = Garden(size=1)

gardener = Gardener(garden1, garden2, garden3)

gardener.plant(
    {"vegetable": "carrot"}, 
)

gardener.plant(
    {"vegetable": "pickle", "nb_graine": 8}, 
    {"vegetable": "tomato", "nb_graine": 5}, 
)

print(
    gardener.get_seed()
)
