def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[j]< arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]

    return arr
arr=[10,70,60,40,30]
print(selection_sort(arr))
