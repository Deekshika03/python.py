def nextSmaller(arr):
    stack = []
    result = [-1] * len(arr)

    for i in range(len(arr)):

        while stack and arr[i] < arr[stack[-1]]:
            j = stack.pop()
            result[j] = arr[i]

        stack.append(i)

    return result


arr = [5, 7, 3, 8, 2, 6]

print(nextSmaller(arr))

############################################################################################

def nextGreater(arr):
    stack = []
    result = [-1] * len(arr)

    for i in range(len(arr) - 1, -1, -1):

        while stack and stack[-1] <= arr[i]:
            stack.pop()

        if stack:
            result[i] = stack[-1]

        stack.append(arr[i])

    return result


arr = [4, 5, 2, 10, 8]

print(nextGreater(arr)) 

################################################################################################


#without using result
def nextGreater(arr):
    stack = []

    for i in range(len(arr) - 1, -1, -1):

        current = arr[i]

        while stack and stack[-1] <= current:
            stack.pop()

        if stack:
            arr[i] = stack[-1]
        else:
            arr[i] = -1

        stack.append(current)

    return arr


arr = [4, 5, 2, 10, 8]

print(nextGreater(arr))

***************************************************************************************************

def nextSmaller(arr):
    stack = []

    for i in range(len(arr) - 1, -1, -1):

        current = arr[i]

        while stack and stack[-1] >= current:
            stack.pop()

        if stack:
            arr[i] = stack[-1]
        else:
            arr[i] = -1

        stack.append(current)

    return arr


arr = [4, 5, 2, 10, 8]

print(nextSmaller(arr))
