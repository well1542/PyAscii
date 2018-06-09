#! /usr/bin/env python3
# coding: utf-8
from AsciiArt import AsciiArt
import argparse

def init():
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    parser.add_argument('--scaling_ratio', type=float, default=0.5)
    parser.add_argument('--output_type', type=int, default=2)
    args = parser.parse_args()
    return (args.file, args.scaling_ratio, args.output_type)

def main():
    img_path, scaling_ratio, output_type = init()
    filename = img_path.split('.')[0]
    asciiart = AsciiArt(img_path)
    if output_type == 0:
        asciiart.save_as_txt_file(scaling_ratio, filename)
    elif output_type == 1:
        asciiart.save_as_html_file(scaling_ratio, filename)
    elif output_type == 2:
        asciiart.save_as_txt_file(scaling_ratio, filename)
        asciiart.save_as_html_file(scaling_ratio, filename)
    else:
        raise ValueError('Possible values are 0, 1 and 2.')


if __name__ == '__main__':
    main()
