def heaptify(arr, idx, heap_size):
    print(arr)
    left = idx * 2 + 1
    right = idx * 2 + 2
    largest = idx
    if left < heap_size and arr[left] > arr[largest]:
        largest = left
    if right < heap_size and arr[right] > arr[largest]:
        largest = right

    if idx != largest:
        arr[largest], arr[idx] = arr[idx], arr[largest]
        heaptify(arr, largest, heap_size)


def heap_sort(arr):
    n = len(arr)
    print("what")
    for i in range(n // 2 - 1, -1, -1): # 최대 힙 만들기
        print(i)
        heaptify(arr, i, n)


    print("정렬")
    for i in range(n - 1, 0, -1):  # 정렬 > root값을 말단으로 보내고 나버지로 다시 최대 힙 구성
        arr[0], arr[i] = arr[i], arr[0]
        heaptify(arr, 0, i)
    return arr

arr = [6, 1, 3, 4, 5, 2, 8, 7]
arr = heap_sort(arr)

print(arr)