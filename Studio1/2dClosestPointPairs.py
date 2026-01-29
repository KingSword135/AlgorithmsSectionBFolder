import math, webbrowser

def calcDistance(points1, points2):
    return math.sqrt(math.pow((points1[0] - points2[0]),2) + math.pow((points1[1] - points2[1]),2))

def getMinDistance(points_list):

    length = len(points_list)
    minimumDistance = 9999
    for i in range(length):
        for j in range(i + 1, length):
            if (calcDistance(points_list[i],points_list[j]) < minimumDistance):
                minimumDistance = calcDistance(points_list[i],points_list[j])
    
    return minimumDistance

if __name__ == "__main__":
    
    points_list = []
    length = int(input("How many point pairs do you want in your list? "))
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

    for i in range(length):
        point1 = float(input("Enter point 1: "))
        point2 = float(input("Enter point 2: "))
        sub_array = []
        sub_array.append(point1)
        sub_array.append(point2)
        points_list.append(sub_array)

    min = getMinDistance(points_list)
    print(f"Minimum distance is: {min:.3f}")
    webbrowser.open_new_tab(url)

