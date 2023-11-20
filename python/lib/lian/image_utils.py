import cv2
import matplotlib.pyplot as plt
import numpy as np
from skimage.measure import label, regionprops


class ImageUtils:
    @staticmethod
    def read(filename):
        return cv2.cvtColor(cv2.imread(filename, cv2.IMREAD_GRAYSCALE), cv2.COLOR_BGR2RGB)

    @staticmethod
    def save(image, filename):
        cv2.imwrite(filename, cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
        print(f'Image saved: {filename}')

    @staticmethod
    def show(image):
        plt.imshow(image)
        plt.show()

    @staticmethod
    def binarize(image):
        blurred = cv2.medianBlur(image, 5)
        _, thresh = cv2.threshold(blurred, 225, 255, cv2.THRESH_BINARY)
        cleaned = ImageUtils.__remove_noise(thresh)
        return ImageUtils.__binarize(cleaned)

    @staticmethod
    def draw_the_path(image, path, color=[255, 0, 0]):
        for point in path:
            image[point.y, point.x] = color

    @staticmethod
    def __remove_noise(image):
        labeled = label(image, 255, connectivity=2)
        regions = regionprops(labeled)
        amount = area_sum = avg_area = 0
        for region in regions:
            area_sum += region.area
            amount += 1
        avg_area = area_sum / amount
        for region in regions:
            bbox = region.bbox
            if region.area < avg_area * 0.1:
                labeled[bbox[0]:bbox[3], bbox[1]:bbox[4]] = [0, 0, 0]
        return labeled

    @staticmethod
    def __binarize(image):
        r, g, b = image[:, :, 0], image[:, :, 2], image[:, :, 1]
        r = np.where(r > 0, 255, 0)
        g = np.where(g > 0, 255, 0)
        b = np.where(b > 0, 255, 0)
        binarized = np.int64(
            np.all(np.dstack(tup=(r, g, b))[:, :, :-1] == 0, axis=2))
        return binarized
