from aoc.utils import local_path
from aoc.day20.second.arrangement import arrange_tiles
from aoc.day20.second.monsters import find_water_roughness, generate_image_from_tiles
from aoc.day20.second.tiles import Tile


def parse_input(path_to_file):
    with open(path_to_file) as input_file:
        return list(map(Tile.parse, input_file.read().split('\n\n')))


def main():
    input_filename = '../input'
    tiles = parse_input(local_path(__file__, input_filename))
    print('== Arranging tiles ...')
    arranged_tiles = arrange_tiles(tiles)
    print('== Tiles arranged. Generating image ...')
    image = generate_image_from_tiles(arranged_tiles)
    print('== Image generated. Finding water roughness ...')
    roughness = find_water_roughness(arranged_tiles, image)

    print(roughness)


if __name__ == '__main__':
    main()
