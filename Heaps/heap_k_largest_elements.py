
import heapq
# naive, time O(klogn)
# good, time O(klogk)
	# logk: insert/extract from max_heap

def k_largest_in_binary_heap(A, k):
	if k <= 0:
		return []

	candidate_max_heap = []
	candidate_max_heap.append((-A[0], 0))
	result = []
	#print(candidate_max_heap)
	for _ in range(k):
		candidate_idx = candidate_max_heap[0][1]
		#print(candidate_idx)
		result.append(-heapq.heappop(candidate_max_heap)[0])
		
		left_child_idx = 2 * candidate_idx + 1
		if left_child_idx < len(A):
			heapq.heappush(candidate_max_heap, (-A[left_child_idx], left_child_idx))
		
		right_child_idx = 2 * candidate_idx + 2
		if right_child_idx < len(A):
			heapq.heappush(candidate_max_heap, (-A[right_child_idx], right_child_idx))

	return result


def main():
	max_heap = [97, 84, 93, 83, 81, 90, 79, 83, 55, 42, 21, 73]
	result = k_largest_in_binary_heap(max_heap, 3)
	expected_result = [97, 93, 90]
	print('Inputs: ', max_heap)
	print('Result: ', result)
	print('expected_result: ', expected_result)

if __name__ == '__main__':
	main()