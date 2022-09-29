'''
This code traverses a list 'a window at a time' and finds the maximum element
'''
numbers = [num for num in range(10, 0, -1)]
window_size = 5
previous_max = current_max = 0

for i in range(0, len(numbers) - window_size + 1):
    if i == 0:
        current_max = max(numbers[i : i + window_size])
    else:
        current_max = max([previous_max] + [numbers[i]])
        
    previous_max = max(numbers[i + 1: i + window_size - 1])
    
    print(current_max, previous_max)
