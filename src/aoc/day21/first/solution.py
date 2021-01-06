import attr

from aoc.utils import local_path


@attr.s
class Food:
    ingredients = attr.ib()
    allergens = attr.ib()

    @staticmethod
    def parse(line):
        allergens_start = line.index('(contains ')
        ingredients = line[:allergens_start].split()
        allergens = line[allergens_start:][len('(contains '):-1].split(', ')

        return Food(ingredients, allergens)


def find_safe_ingredients(foods):
    allergen_to_ingredients = {}

    for food in foods:
        for allergen in food.allergens:
            if allergen not in allergen_to_ingredients:
                allergen_to_ingredients[allergen] = set(food.ingredients)
            else:
                allergen_to_ingredients[allergen] = (
                    allergen_to_ingredients[allergen].intersection(
                        food.ingredients
                    )
                )

    all_ingredients = {
        ingredient
        for food in foods
        for ingredient in food.ingredients
    }

    return all_ingredients - set.union(*allergen_to_ingredients.values())


def solve(foods):
    safe_ingredients = find_safe_ingredients(foods)

    return sum(
        map(len, [
            safe_ingredients.intersection(food.ingredients)
            for food in foods
        ])
    )


def parse_input(path_to_file):
    with open(path_to_file) as input_file:
        return [
            Food.parse(line.strip())
            for line in input_file
        ]


def main():
    input_filename = '../input'
    foods = parse_input(local_path(__file__, input_filename))

    print(solve(foods))


if __name__ == '__main__':
    main()
