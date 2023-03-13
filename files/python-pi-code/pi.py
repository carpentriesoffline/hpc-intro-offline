import numpy as np
import sys
import datetime

def inside_circle(total_count):
	x = np.random.uniform(size=total_count)
	y = np.random.uniform(size=total_count)
	radii = np.sqrt(x * x + y * y)
	count = len(radii[np.where(radii<=1.0)])
	return count

def main():
	n_samples = int(sys.argv[1])
	start_time = datetime.datetime.now()
	counts = inside_circle(n_samples)
	my_pi = 4.0 * counts / n_samples
	end_time = datetime.datetime.now()
	elapsed_time = (end_time - start_time).total_seconds()
	size_of_float = np.dtype(np.float64).itemsize
	memory_required = 3 * n_samples * size_of_float / (1024**3)
	print(f"Pi: {my_pi}, memory: {memory_required} GiB, time: {elapsed_time} s")

if __name__ == '__main__':
	main()