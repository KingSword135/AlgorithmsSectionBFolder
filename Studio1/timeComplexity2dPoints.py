import numpy as np, matplotlib.pyplot as plt
import ClosestPointPairs
import random, time, webbrowser

def fillRandom(point_array):
    for i in range(0, i):
        sublist = []
        sublist.append(random.random(-20,20))
        sublist.append(random.random(-20,20))
        point_array
    

input_sizes = np.linspace(2,302,300,dtype=int)
times = []

for i in input_sizes:

    points_array = []
    for i in range(0, i):
        sublist = []
        sublist.append(random.uniform(-20,20))
        sublist.append(random.uniform(-20,20))
        points_array.append(sublist)

    start = time.time()
    ClosestPointPairs.getMinDistance(points_array)
    end = time.time()
    times.append(end - start)

plt.figure(figsize=(8,5))
plt.plot(input_sizes,times,label='O(n^2) 2D Closest Point',color='green')
plt.xlabel("Input Size (n)")
plt.ylabel("Time Required (seconds)")
plt.legend()
plt.grid(False)
plt.show()
url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
webbrowser.open_new_tab(url)