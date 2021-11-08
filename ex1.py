"""""""""
Gil Diamant, 314978312
"""""""""

import matplotlib.pyplot as plt
import numpy as np
import sys

#get the the input and intilaize it.
def input_process():
    image_fname, centroids_fname, out_fname = sys.argv[1], sys.argv[2], sys.argv[3]
    z = np.loadtxt(centroids_fname)
    orgin_pixels = plt.imread(image_fname)
    pixels = orgin_pixels.astype \
                 (float) / 255
    pixels = pixels.reshape(-1, 3)
    return pixels, z, out_fname


def main():
    pixels, z, out_fname = input_process()
    f = open(out_fname, "w+")
    new_z = z
    for i in range(20):
        old_z = new_z
        new_z = k_means(pixels, new_z)
        f.write(f"[iter {i}]:{','.join([str(i) for i in new_z])} \n")
        if np.array_equal(old_z, new_z):
            break
    f.close()


def k_means(pixels, z):
    new_z = []
    # first step in the algorithm
    pixels_centroids = []
    for i in range(len(z)): pixels_centroids.append([])
    for pixel in pixels:
        index = 0
        min_dist = np.linalg.norm(pixel - z[0], axis=0)
        for i in range(len(z)):
            centroid = z[i]
            dist = np.linalg.norm(pixel - centroid, axis=0)
            if min_dist > dist:
                min_dist = dist
                index = i
        pixels_centroids[index].append(pixel)
    # second step in the algorithm
    for i in range(len(z)):
        related_pixels = []
        if len(pixels_centroids[i]) == 0:
            continue
        else:
            for rel_pixel in pixels_centroids[i]:
                related_pixels.append(rel_pixel)
        sum = np.sum(related_pixels, 0)
        new_z.append(np.round(np.divide(sum, len(related_pixels)), 4))
    return new_z


if __name__ == '__main__':
    main()
