import random
import sys

# time complexity O(k)
def sampling_random(A, k):
	for i in range(k):
		rand_id = random.randint(i, len(A) - i)
		A[i], A[rand_id] = A[rand_id], A[i]

def main():
    # if len(sys.argv) == 2:
    #     n = int(sys.argv[1])
    #     k = random.randint(1, n)
    # elif len(sys.argv) == 3:
    #     n = int(sys.argv[1])
    #     k = int(sys.argv[2])
    # else:
    #     n = random.randint(1, 10)
    #     k = random.randint(1, n)
    n = 20
    k = 2

    A = list(range(n))
    print('len: {} k: {}'.format(n, k))

    print('before: ', *A)

    sampling_random(A, k)
    print('after:  ', *A)
    print('sampling results: ', *A[:k])



if __name__ == '__main__':
    main()