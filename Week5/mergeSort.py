def merge(left, right, compare):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result
        
def compare(num1, num2):
    return num1 < num2

def mergeSort(L, compare):
    if len(L) < 2:
        return L[:]
    else:
        mid = int(len(L)/2)
        left = mergeSort(L[:mid], compare)
        right = mergeSort(L[mid:], compare)
        return merge(left, right, compare)

L = [2,-5,3,0,15,1,6,9,4,7,-6]
print mergeSort(L, compare)
