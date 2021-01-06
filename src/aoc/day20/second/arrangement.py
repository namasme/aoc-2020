from math import sqrt

from aoc.utils.spatial import Direction

from .tiles import TileTransformation


def to_coordinates(index, width):
    return (index % width, index // width)


def to_index(coordinates, width):
    x, y = coordinates
    return y * width + x


def has_tile_above(index, width):
    _, y = to_coordinates(index, width)
    return y > 0


def has_tile_leftwards(index, width):
    x, _ = to_coordinates(index, width)
    return x > 0


def arrange_tiles(tiles):
    width = int(sqrt(len(tiles)))
    total_candidates = len(tiles) * TileTransformation.SIZE
    pickup = [0]
    stack = []
    used_tiles = set()

    while len(stack) < len(tiles):
        stack_index = len(stack)

        for candidate_id in range(pickup[-1], total_candidates):
            transformation_id, tile_index = to_coordinates(
                candidate_id, TileTransformation.SIZE,
            )

            if tile_index in used_tiles:
                continue

            transformation = TileTransformation.from_id(transformation_id)
            transformed_tile = transformation.apply(tiles[tile_index])

            restriction_above = (
                not has_tile_above(stack_index, width)
                # material implication ftw
                or stack[stack_index - width].borders.borders_match(
                    Direction.D, transformed_tile.borders, Direction.U,
                )
            )
            restriction_left = (
                not has_tile_leftwards(stack_index, width)
                or stack[stack_index - 1].borders.borders_match(
                    Direction.R, transformed_tile.borders, Direction.L,
                )
            )

            if not (restriction_above and restriction_left):
                continue

            pickup[-1] = candidate_id + 1
            pickup.append(0)
            stack.append(transformed_tile)
            used_tiles.add(tile_index)
            break
        else:  # backtrack
            stack.pop()
            pickup.pop()
            _, tile_index = to_coordinates(
                pickup[-1] - 1, TileTransformation.SIZE,
            )

            used_tiles.remove(tile_index)

    return stack
