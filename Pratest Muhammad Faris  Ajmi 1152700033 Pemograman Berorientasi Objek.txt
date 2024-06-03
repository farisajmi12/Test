# Pseudocode : Sorting_Algorithm
# Sort(A:list of sortable item)
#     n = length(A)
#     for i from 0 to n-1 do:
#     swapped = False
#     for j from 0 to n-i-1 do:
#         if A[j] > A[j+1] then:
#         swap A[j] with A[j+]
#         swapped = true
#     if not swapped then:
#     break
# end procedure

def sort(A):
    n = len(A)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                swapped = True
        if not swapped:
            break
    return A

A = [100, 99, 97, 98, 96]
sorted_A = sort(A)
print(sorted_A)