#Human readable duration format
def format_duration(seconds):
    # Helper function to format the time units
    def format_unit(value, unit_name):
        if value > 0:
            return f"{value} {unit_name}{'' if value == 1 else 's'}"
        return ""
    
    if seconds == 0:
        return "now"
    
    # Define time units in seconds
    year_sec = 365 * 24 * 3600
    day_sec = 24 * 3600
    hour_sec = 3600
    minute_sec = 60
    
    # Calculate years, days, hours, minutes and seconds
    years, seconds = divmod(seconds, year_sec)
    days, seconds = divmod(seconds, day_sec)
    hours, seconds = divmod(seconds, hour_sec)
    minutes, seconds = divmod(seconds, minute_sec)
    
    # Create a list of formatted units
    units = [
        format_unit(years, "year"),
        format_unit(days, "day"),
        format_unit(hours, "hour"),
        format_unit(minutes, "minute"),
        format_unit(seconds, "second")
    ]
    
    # Remove empty units and join with commas and "and"
    non_empty_units = [unit for unit in units if unit]
    if not non_empty_units:
        return "now"
    
    if len(non_empty_units) == 1:
        return non_empty_units[0]
    return ', '.join(non_empty_units[:-1]) + ' and ' + non_empty_units[-1]
#Twice linear
import heapq
def dbl_linear(n):

    min_heap = [1]
    seen = {1}
    
    for _ in range(n + 1):
        current = heapq.heappop(min_heap)
        next_y = 2 * current + 1
        next_z = 3 * current + 1
        if next_y not in seen:
            seen.add(next_y)
            heapq.heappush(min_heap, next_y)
        
        if next_z not in seen:
            seen.add(next_z)
            heapq.heappush(min_heap, next_z)
    return current
#N Linear
import heapq
def n_linear(m, n):
    min_heap = [1]
    seen = {1}
    
    current_value = 1
    for _ in range(n + 1):
        current_value = heapq.heappop(min_heap)
        for factor in m:
            new_value = current_value * factor + 1
            if new_value not in seen:
                seen.add(new_value)
                heapq.heappush(min_heap, new_value)
    return current_value
#Matrix Determinant

import numpy as np
def determinant(matrix):
    return np.linalg.det(matrix).round()

#method two

def determinant(matrix):
  
    def get_minor(matrix, row, col):
        return [ [matrix[i][j] for j in range(len(matrix[i])) if j != col] for i in range(len(matrix)) if i != row ]

    # Base case: 1x1 matrix
    if len(matrix) == 1:
        return matrix[0][0]
 
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


    det = 0
    for c in range(len(matrix)):
    
        sign = (-1) ** c
        minor = get_minor(matrix, 0, c)
        det += sign * matrix[0][c] * determinant(minor)

    return det