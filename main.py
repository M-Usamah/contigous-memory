#First fit

def first_fit(block_size, len_m, process_size, len_n):
  allocatıon = [-1]*len_n

  for i in range(len_n):
    for j in range(len_m):
      if block_size[j] >= process_size[i]:
        allocatıon[i] = j
        block_size[j]-= process_size[i]
        break
  print(" Process No. Process Size      Block n")

  for i in range(len_n):
    print(" ", i + 1, "         ", process_size[i],
                          "            ", end = " ")
    if allocatıon[i] != -1:
      print(allocatıon[i] + 1)
    else:
      print("Not Allocated")


#Best fit
def best_fit(block_size, len_m, process_size, len_n):
  
	allocation = [-1] * len_n
	for i in range(len_n):
		best_idx = -1
		for j in range(len_m):
			if block_size[j] >= process_size[i]:
				if best_idx == -1:
					best_idx = j
				elif block_size[best_idx] > block_size[j]:
					best_idx = j
		if best_idx != -1:
			allocation[i] = best_idx
			block_size[best_idx] -= process_size[i]

	print("Process No. Process Size	 Block no.")
	for i in range(len_n):
		print(i + 1, "		 ", process_size[i],
								end = "		 ")
		if allocation[i] != -1:
			print(allocation[i] + 1)
		else:
			print("Not Allocated")
	
# Worst fit
def worstFit(block_size, len_m, process_size, len_n):

	allocation = [-1] * len_n
	for i in range(len_n):
		
		wstIdx = -1
		for j in range(len_m):
			if block_size[j] >= process_size[i]:
				if wstIdx == -1:
					wstIdx = j
				elif block_size[wstIdx] < block_size[j]:
					wstIdx = j

		if wstIdx != -1:
			

			allocation[i] = wstIdx


			block_size[wstIdx] -= process_size[i]

	print("Process No. Process Size Block no.")
	for i in range(len_n):
		print(i + 1, "		 ",
			process_size[i], end = "	 ")
		if allocation[i] != -1:
			print(allocation[i] + 1)
		else:
			print("Not Allocated")

print("it works")
if __name__ == '__main__':
    block_size = [100, 500, 200, 300, 600]
    process_size = [212, 417, 112, 426]
    len_m = len(block_size)
    len_n = len(process_size)
    print("First fit")
    first_fit(block_size, len_m, process_size, len_n)
    print("\nBest fit")
    best_fit(block_size, len_m, process_size, len_n)
    print("\nWorst fit")
    best_fit(block_size, len_m, process_size, len_n)