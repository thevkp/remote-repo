def bs(arr, key):
  start = 0
  end = len(arr) - 1
  
  while start <= end:
    mid = start + (end - start) // 2
    
    if arr[mid] == key:
      return mid
    elif arr[mid] < key:
      start = mid + 1
    else:
      end = mid - 1

  return -1


arr = list(map(int, input("Enter space separated numbers: ").split()))

key = int(input("Enter the key"))

print(bs(arr, key))