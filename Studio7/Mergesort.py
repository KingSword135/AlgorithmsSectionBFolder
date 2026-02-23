def MergeSort(array):

    if (len(array)) <= 1:
        return array
    mid = len(array) // 2
    left_array = array[:mid]
    right_array = array[mid:]

    sorted_left_half = MergeSort(left_array)
    sorted_right_half = MergeSort(right_array)

    return merge(sorted_left_half,sorted_right_half)

def merge(left_half, right_half):
    array_result = []
    i = 0
    j = 0
    while (i < len(left_half) and j < len(right_half)):
        if (left_half[i] < right_half[j]):
            array_result.append(left_half[i])
            i += 1
        else:
            array_result.append(right_half[j])
            j += 1
    
    array_result.extend(left_half[i:])
    array_result.extend(right_half[j:])
    return array_result

if __name__ == "__main__":
    array = [873,452,978,123]
    array = MergeSort(array)
    print(array)