
def selection_sort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if arr[min] > arr[j]:
                min = j
                
        arr[i], arr[min] = arr[min], arr[i]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
 
if __name__ == '__main__':

    array = []
    total = int(input("How many elements you want to insert: "))
    for i in range(total):
        num = float(input(f"Enter the percentage of student {i+1} : "))
        array.append(num)
    
    selection_sort(array)
    print ("\n(Selection Sort)\nSorted array : ", array)
    
    bubbleSort(array)
    print("\n(Bubble sort)\nSorted array : ", array)

