from time import time
import matplotlib.pyplot as plt
from perlin_noise import PerlinNoise
def noise(octocts,width,height):
    noiseList=[]
    for n in range(octocts):
        noiseList.append(PerlinNoise(octaves=3*(n+1),seed=time()))
    noise1 = PerlinNoise(octaves=3)
    noise2 = PerlinNoise(octaves=6)
    noise3 = PerlinNoise(octaves=12)
    noise4 = PerlinNoise(octaves=24)

    xpix, ypix = width,height
    pic = []
    for i in range(xpix):
        row = []
        for j in range(ypix):
            noise_val=0
            for m in range(octocts):
                noise_val+=noiseList[m]([i/xpix,j/ypix])/(m+1)
            # noise_val = noise1([i/xpix, j/ypix])
            # noise_val += 0.5 * noise2([i/xpix, j/ypix])
            # noise_val += 0.25 * noise3([i/xpix, j/ypix])
            # noise_val += 0.125 * noise4([i/xpix, j/ypix])
            row.append(noise_val)
        pic.append(row)
    return pic