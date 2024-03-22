import argparse
from pathlib import Path

from PIL import Image


def main(img_path: Path, output: Path):
    img = Image.open(img_path).convert("RGB")
    output.mkdir(parents=True, exist_ok=True)
    img.getchannel(0).save(output / 'channel1.png')
    img.getchannel(1).save(output / 'channel2.png')
    img.getchannel(2).save(output / 'channel3.png')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--img_path', '-i', type=Path, help='Path to the image to split into the RGB channels.')
    parser.add_argument('--output', '-o', type=Path, help='Path to the output directory.')
    args = parser.parse_args()
    main(**args.__dict__)
