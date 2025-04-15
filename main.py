from quicksort import quicksort

def main():
    # Test with a random array
    test_array = [3, 6, 8, 10, 1, 2, 1, 5, 7, 9]
    print("Original array:", test_array)
    
    # Sort the array
    sorted_array = quicksort(test_array)
    print("Sorted array:", sorted_array)
    
    # Additional test cases
    print("\nAdditional test cases:")
    print(f"Empty array: {quicksort([])}")
    print(f"Single element: {quicksort([42])}")
    print(f"Already sorted: {quicksort([1, 2, 3, 4, 5])}")
    print(f"Reverse sorted: {quicksort([5, 4, 3, 2, 1])}")
    print(f"Duplicate elements: {quicksort([3, 3, 3, 3])}")

if __name__ == "__main__":
    main()