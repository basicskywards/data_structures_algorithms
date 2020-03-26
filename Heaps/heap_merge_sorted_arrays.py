import heapq
import sys
import random
# Time complexity O(nlogk)
# n: total elements
# k: number of sorted arrays/sequences

def merge_sorted_arrays(sorted_arrays):
	min_heap = []

	# build a list of iterators for each array in sorted arrays
	sorted_arrays_iters = [iter(x) for x in sorted_arrays]
	#print(sorted_arrays_iters)
	# put first element from each iterator in min_heap
	for i, it in enumerate(sorted_arrays_iters):
		first_element = next(it, None)
		if first_element is not None:
			heapq.heappush(min_heap, (first_element, i))

	#print(min_heap)
	result = []
	while min_heap:
		smallest_entry, smallest_array_i = heapq.heappop(min_heap)
		smallest_array_iter = sorted_arrays_iters[smallest_array_i]
		result.append(smallest_entry)
		next_element = next(smallest_array_iter, None)
		if next_element is not None:
			heapq.heappush(min_heap, (next_element, smallest_array_i))

	return result

def main():
    S = [[1, 5, 10], [2, 3, 100], [2, 12, 2**64 - 1]]
    print('Inputs: ', S)
    print('\nOutputs: ', merge_sorted_arrays(S))

    for _ in range(100):
        n = int(sys.argv[1]) if len(sys.argv) == 2 else random.randint(1, 5)

        S = []
        for i in range(n):
            S.append(
                sorted(
                    random.randint(-9999, 9999)
                    for j in range(random.randint(1, 10))))
        print('\nInputs: ', S)
        print('\nOutputs: ', merge_sorted_arrays(S))

if __name__ == '__main__':
	main()