#%%
# Shortest Remaining Time First (SRTF) 

# save data from FCFS
wait_gp = []
turn_gp = []

# Function to find the waiting time 
# for all processes 
def findWaitingTime(processes, n, wt): 
	rt = [0] * n 

	# Copy the burst time into rt[] 
	for i in range(n): 
		rt[i] = processes[i][1] 
	complete = 0
	t = 0
	minm = 999999999
	short = 0
	check = False

	# Process until all processes gets 
	# completed 
	while (complete != n): 
		
		# Find process with minimum remaining 
		# time among the processes that 
		# arrives till the current time` 
		for j in range(n): 
			if ((processes[j][2] <= t) and (rt[j] < minm) and rt[j] > 0): 
				minm = rt[j] 
				short = j 
				check = True
		if (check == False): 
			t += 1
			continue
			
		# Reduce remaining time by one 
		rt[short] -= 1

		# Update minimum 
		minm = rt[short] 
		if (minm == 0): 
			minm = 999999999

		# If a process gets completely 
		# executed 
		if (rt[short] == 0): 

			# Increment complete 
			complete += 1
			check = False

			# Find finish time of current 
			# process 
			fint = t + 1

			# Calculate waiting time 
			wt[short] = (fint - processes[short][1] -processes[short][2]) 

			if (wt[short] < 0): 
				wt[short] = 0
		
		# Increment time 
		t += 1

# Function to calculate turn around time 
def findTurnAroundTime(processes, n, wt, tat): 
	
	# Calculating turnaround time 
	for i in range(n): 
		tat[i] = processes[i][1] + wt[i] 

# Function to calculate average waiting 
# and turn-around times. 
def findavgTime(processes, n): 
	wt = [0] * n 
	tat = [0] * n 

	# Function to find waiting time 
	# of all processes 
	findWaitingTime(processes, n, wt)

	# Function to find turn around time 
	# for all processes 
	findTurnAroundTime(processes, n, wt, tat) 

	# Display processes along with all details 
	print("Processes Burst Time	 Waiting", "Time	 Turn-Around Time") 
	total_wt = 0
	total_tat = 0
	for i in range(n): 

		total_wt = total_wt + wt[i] 
		total_tat = total_tat + tat[i] 

		# save data to array
		wait_gp.append(wt[i])
		turn_gp.append(tat[i])
		print(" ", processes[i][0], "\t\t", processes[i][1], "\t\t", wt[i], "\t\t", tat[i]) 


	print("\nAverage waiting time = %.5f "%(total_wt /n) ) 
	print("Average turn around time = ", total_tat / n) 

	# save text file
	f = open("./data_of_time/SJF/twentyWaitingTime.txt","w")
	for i in range(n):
		f.write(str(wait_gp[i])+'\n')
	f.close()

	f = open("./data_of_time/SJF/twentyTurnARTime.txt","w")
	for i in range(n):
		f.write(str(turn_gp[i])+'\n')
	f.close()
	
# Driver code 
if __name__ =="__main__": 
	
	# Process id's 
    proc = []

	#20 processes
    f = open("../process/twentyProcess.txt","r")
    for i in f:
        proc.append(int(i.strip("\n")))
    
    proc_id = []
    for i in range(len(proc)):
        if(i==0):
            proc_id.append([i+1,proc[i],i+1])
        else:
            proc_id.append([i+1,proc[i],i])
    
    n = len(proc)
	
    findavgTime(proc_id, n)

