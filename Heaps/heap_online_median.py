import random
import heapq
import sys

# Time complexity O(logn) per element, for insertion & extraction from a heap


def median_online(stream):
	resutl = []
	min_heap = [] # to store the larger half of stream (right hand side)
	max_heap = [] # to store the smaller half of stream, NOTE: values in max_heap are negative

	for e in stream:
		# add one new element to right hand side (min_heap) & pop 1 element which is added to left hand side (max_heap)

		heapq.heappush(max_heap, -heapq.heappushpop(min_heap, e)) # heapq with negative element for max_heap since heapq only has min_heap

		# make sure size equal if even elements
		# if odd elements, right hand side (min_heap) must has 1 more element
		if len(max_heap) > len(min_heap):
			heapq.heappush(min_heap, -heapq.heappop(max_heap))

		resutl.append(1/2 * (min_heap[0] + (-max_heap[0])) if len(min_heap) == len(max_heap) else min_heap[0])
		print('online median -- ', resutl[-1])

def small_test():
	print('\nSmall test:\n')
	stream = [1, 0, 3, 4, 2, 0, 1]
	median_online(iter(stream))
	print('\nsolution: ', [1, 0.5, 1, 2, 2, 1.5, 1])

def main():
	num = int(sys.argv[1]) if len(sys.argv) == 2 else random.randint(1, 100)
	stream = [random.randint(1, 10000) for _ in range(num)]
	print(*stream, sep='\n')
	print('\n online median \n')
	median_online(iter(stream))

if __name__ == '__main__':
	main()

	small_test()

