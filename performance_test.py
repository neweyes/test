import time
import random
from quicksort import quicksort

def test_performance(size=1000, runs=5):
    print(f"Testing performance with arrays of size {size}")
    
    total_custom = 0
    total_builtin = 0
    
    for i in range(runs):
        # Generate random array
        test_array = [random.randint(0, 10000) for _ in range(size)]
        test_array_copy = test_array.copy()
        
        # Test custom quicksort
        start = time.time()
        quicksort(test_array)
        end = time.time()
        custom_time = end - start
        total_custom += custom_time
        
        # Test Python's built-in sort
        start = time.time()
        sorted(test_array_copy)
        end = time.time()
        builtin_time = end - start
        total_builtin += builtin_time
        
        print(f"Run {i+1}: Custom quicksort: {custom_time:.6f}s, Built-in sort: {builtin_time:.6f}s")
    
    print(f"\nAverage over {runs} runs:")
    print(f"Custom quicksort: {total_custom/runs:.6f}s")
    print(f"Built-in sort: {total_builtin/runs:.6f}s")

if __name__ == "__main__":
    test_performance()
    test_performance(size=10000, runs=3)