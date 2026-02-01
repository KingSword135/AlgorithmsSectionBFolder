import math

def calcDistance(points1, points2):
    return math.sqrt(math.pow((points1[0] - points2[0]),2) + math.pow((points1[1] - points2[1]),2))

def getMinDistance(points_list):

    length = len(points_list)
    closestDistance = 9999
    closestPairs = None
    for i in range(length):
        for j in range(i + 1, length):
            if (calcDistance(points_list[i],points_list[j]) < closestDistance):
                closestDistance = calcDistance(points_list[i],points_list[j])
                closestPairs = (points_list[i],points_list[j])
    
    return closestDistance, closestPairs

if __name__ == "__main__":
    
    points_list = []
    length = int(input("How many point pairs do you want in your list? "))

    for i in range(length):
        point1 = float(input("Enter point 1: "))
        point2 = float(input("Enter point 2: "))
        sub_array = []
        sub_array.append(point1)
        sub_array.append(point2)
        points_list.append(sub_array)

    minDist, minPoints = getMinDistance(points_list)
    print(f"Minimum distance is: {minDist:.3f}, closest points are {minPoints}")

