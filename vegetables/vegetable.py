import abc

class Vegetable(abc.ABC):
    def __init__(self, nb_graine) -> None:
        self.nb_graine = nb_graine
    
    def get_nb_graine(self) -> int:
        return self.nb_graine

    def set_nb_graine(self, nb_graine) -> None:
        self.nb_graine = nb_graine