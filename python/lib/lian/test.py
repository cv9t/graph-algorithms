from image_utils import ImageUtils
from point import Point
from lian import Lian


def main():
    image = ImageUtils.read('./map.bmp')
    binarized = ImageUtils.binarize(image)
    lian = Lian(binarized)
    start = Point(175, 304)
    end = Point(1277, 689)
    delta = 8
    max_angle = 16
    path = lian.search(start, end, delta, max_angle)
    if len(path) != 0:
        ImageUtils.draw_the_path(image, path)
        ImageUtils.save(image, f'results/d-{delta}-ma-{max_angle}.png')
    else:
        print('Path wasn\'t found')


if __name__ == '__main__':
    main()
