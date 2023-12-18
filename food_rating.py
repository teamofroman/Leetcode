from typing import List
from collections import defaultdict
from sortedcontainers import SortedList


class FoodRatings:
    class Food:
        def __init__(self, name, cuisine, rating) -> None:
            self.name = name
            self.cuisine = cuisine
            self.rating = rating

        def __eq__(self, __value: object) -> bool:
            return (
                self.name == __value.name
                and self.cuisine == __value.cuisine
                and self.rating == __value.rating
            )

        def __ne__(self, __value: object) -> bool:
            return not self.__eq__(__value)

        def __lt__(self, __value: object) -> bool:
            if self.rating < __value.rating:
                return True

            if self.rating == __value.rating:
                if self.name > __value.name:
                    return True

            return False

        def __le__(self, __value: object) -> bool:
            return self.__lt__(__value) or self.__eq__(__value)

    def __init__(
        self, foods: List[str], cuisines: List[str], ratings: List[int]
    ):
        self.foods = {}
        self.cuisines = defaultdict(lambda: SortedList())

        for i in range(len(foods)):
            new_food = self.Food(foods[i], cuisines[i], ratings[i])

            self.foods[new_food.name] = new_food

            self.cuisines[new_food.cuisine].add(new_food)

    def changeRating(self, food: str, newRating: int) -> None:
        old_food = self.foods[food]
        self.cuisines[old_food.cuisine].remove(old_food)
        self.foods[food].rating = newRating
        self.cuisines[old_food.cuisine].add(old_food)

    def highestRated(self, cuisine: str) -> str:
        return self.cuisines[cuisine][-1].name


if __name__ == '__main__':
    foods = ["czopaaeyl", "lxoozsbh", "kbaxapl"]
    cuisines = ["dmnuqeatj", "dmnuqeatj", "dmnuqeatj"]
    ratings = [11, 2, 15]

    obj = FoodRatings(foods, cuisines, ratings)
    obj.changeRating("czopaaeyl", 12)
    print(obj.highestRated("dmnuqeatj"))
    obj.changeRating("kbaxapl", 8)
    obj.changeRating("lxoozsbh", 5)
    print(obj.highestRated("dmnuqeatj"))
