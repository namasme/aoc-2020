from aoc.day21.first.solution import parse_input
from aoc.utils import local_path


def build_allergens_to_ingredients_map(foods):
    '''
    Adapted from the solution to the first part.
    '''
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

    return allergen_to_ingredients


def eliminate_determinates(allergen_to_ingredients):
    sorted_items = sorted(
        allergen_to_ingredients.items(),
        key=lambda item: len(item[1])
    )
    sorted_allergens, sorted_ingredients = zip(*sorted_items)

    determined = set()
    assignments = {}

    changed = True

    while changed:
        changed = False

        for allergen, candidates in sorted_items:
            if len(candidates - determined) == 1:
                assignments[allergen] = list(candidates - determined)[0]
                determined.add(assignments[allergen])
                changed = True

    return assignments


def canonical_dangerous_ingredient_list(allergen_to_ingredient):
    return ','.join(
        [
            item[1]
            for item in sorted(
                    allergen_to_ingredient.items(),
                    key=lambda item: item[0]
            )
        ]
    )


def main():
    input_filename = '../input'
    foods = parse_input(local_path(__file__, input_filename))
    allergen_to_ingredients = build_allergens_to_ingredients_map(foods)
    allergen_to_ingredient = eliminate_determinates(allergen_to_ingredients)

    print(canonical_dangerous_ingredient_list(allergen_to_ingredient))


if __name__ == '__main__':
    main()
