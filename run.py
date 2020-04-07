import argparse

import cv2

from img_stitch import ImageStitcher


def run():
    # Driving Function + Argument Handling
    parser = argparse.ArgumentParser(description='Panoramic Stitch')
    parser.add_argument(
        'input', nargs='+',
        help='The input image files')
    parser.add_argument(
        '-o', required=True, dest='output',
        help='Where to put the resulting stitched image')
    parser.add_argument(
        '-b', '--base', type=int,
        help='Base Image Index')
    args = parser.parse_args()

    stitch = ImageStitcher()
    if args.base is not None:
        stitch.center = args.base
    for infile in args.input:
        stitch.add_image(infile)
    result = stitch.stitch()

    cv2.imwrite(args.output, cv2.cvtColor(result, cv2.COLOR_RGBA2BGRA))


if __name__ == '__main__':
    try:
        feature_finder = cv2.xfeatures2d.SIFT_create()
        matcher = cv2.BFMatcher_create(cv2.NORM_L2)
    except AttributeError:
        print("Install Sift")
    run()
