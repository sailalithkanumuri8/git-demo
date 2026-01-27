"""
Utility functions for data analysis
"""

def find_max(numbers):
    if not numbers:
        return None
    return max(numbers)

def find_min(numbers):
    if not numbers:
        return None
    return min(numbers)

def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

if __name__ == "__main__":
    data = [23, 45, 67, 12, 89, 34]
    print(f"Data: {data}")
    print(f"Max: {find_max(data)}")
    print(f"Min: {find_min(data)}")
    print(f"Average: {calculate_average(data):.2f}")

