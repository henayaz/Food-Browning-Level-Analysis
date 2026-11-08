"""Load and preview a food image (first image-processing step)."""
from pathlib import Path
import cv2
import matplotlib.pyplot as plt


def main():
    image_path = Path(__file__).resolve().parents[1] / 'data' / 'samples' / 'food.jpg'
    image = cv2.imread(str(image_path))
    if image is None:
        print(f'Image not found: {image_path}')
        print('Place a food photo named food.jpg inside data/samples/.')
        return

    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    print(f'Image size: {rgb_image.shape[1]} x {rgb_image.shape[0]} pixels')
    plt.imshow(rgb_image)
    plt.title('Original Food Image')
    plt.axis('off')
    plt.show()


if __name__ == '__main__':
    main()
