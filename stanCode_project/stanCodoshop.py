"""
name:Chasel Fan
file:stanCodoshop.py
-----------------------------------------------
SC101 - Assignment3
Adapted from Nick Parlante's Ghost assignment by
Jerry Liao.

-----------------------------------------------

TODO:
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the square of the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (int): squared distance between red, green, and blue pixel values

    """
    return ((red - pixel.red) ** 2 + (green - pixel.green) ** 2 + (blue - pixel.blue) ** 2) ** (0.5)


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    total_r=0
    total_g=0
    total_b=0
    # it return a list that put average red,blue,and green
    for p in pixels:
        total_r+=p.red
    avg_r=total_r/len(pixels)
    for p in pixels:
        total_g+=p.green
    avg_g=total_g/len(pixels)
    for p in pixels:
        total_b+=p.blue
    avg_b=total_b/len(pixels)
    lst=[int(avg_r),int(avg_g),int(avg_b)]
    return lst


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    red=get_average(pixels)[0]
    green=get_average(pixels)[1]
    blue=get_average(pixels)[2]
    best_pixel=pixels[0]
    # it make the first distance of RGB always smaller
    min=float('inf')
    for p in pixels:
        n=get_pixel_dist(p,red,green,blue)
        # it return the shortest distance of RGB
        if n<min:
            min=n
            best_pixel=p
    return best_pixel

def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    # it make a window that is as big as the picture
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    ######## YOUR CODE STARTS HERE #########
    # Write code to populate image and create the 'ghost' effect
    for x in range(width):
        for y in range(height):
            pixels=[]
            for img in images:
                # it make a list to get the best pixel
                pixel=img.get_pixel(x,y)
                pixels.append(pixel)
            best_pixel=get_best_pixel(pixels)
            # it make result (x,y) became best_pixel(x,y)
            result_p=result.get_pixel(x,y)
            result_p.red=best_pixel.red
            result_p.green=best_pixel.green
            result_p.blue=best_pixel.blue
    ######## YOUR CODE ENDS HERE ###########
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    # it make the picture to be a landscape
    solve(images)


if __name__ == '__main__':
    main()
