import os
import glob
from PIL import Image
import imagehash

def main():
    images = []
    for image in glob.iglob(f"{os.getcwd()}/assets/*"):
        if str(imagehash.average_hash(Image.open(image))) in images:
            os.remove(image)
        else:
            images.append(str(imagehash.average_hash(Image.open(image))))

if __name__ == "__main__":
    main()