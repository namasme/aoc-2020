from math import sqrt

from aoc.utils.spatial import Point2D
from .tiles import TileContent, TileTransformation


def hstack(*matrices):
    return [
        ''.join(combined_row)
        for combined_row in zip(*matrices)
    ]


def generate_image_from_tiles(arranged_tiles):
    width = int(sqrt(len(arranged_tiles)))

    image_rows = sum([
        hstack(*[
            tile.content.rows
            for tile in arranged_tiles[row_start:row_start+width]
        ])
        for row_start in range(0, len(arranged_tiles), width)  # width == height
    ], [])

    return image_rows


def positions_from_mask(mask):
    return [
        Point2D(n_column, n_row)
        for n_row, row in enumerate(mask)
        for n_column, char in enumerate(row)
        if char == '#'
    ]


def match_pattern(mask, haystack):
    mask_height = len(mask)
    mask_width = len(mask[0])
    matches_positions = []

    for h_row_n, h_row in enumerate(haystack[:1-mask_height]):
        for h_column_n, char in enumerate(h_row[:1-mask_width]):
            for offset in positions_from_mask(mask):
                position = offset + Point2D(h_column_n, h_row_n)

                if haystack[position.y][position.x] != '#':
                    break
            else:
                matches_positions.append(Point2D(h_column_n, h_row_n))

    return matches_positions


def roughness(image):
    return sum(row.count('#') for row in image)


def find_water_roughness(arranged_tiles, image):
    monster_mask = [
        '                  # ',
        '#    ##    ##    ###',
        ' #  #  #  #  #  #   ',
    ]
    content = TileContent(monster_mask)
    tranquil_positions = set()

    for transformation_id in range(TileTransformation.SIZE):
        transformation = TileTransformation.from_id(transformation_id)
        transformed_mask = transformation.apply(content).rows
        tranquil_positions.update(match_pattern(transformed_mask, image))

    return roughness(image) - len(tranquil_positions) * roughness(monster_mask)
