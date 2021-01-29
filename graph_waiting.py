#%%
import matplotlib.pyplot as plotG
from pandas import DataFrame

wait_gp_FCFS = []

wait_gp_SJF = []

wait_gp_RR = []

# import file "./" run with python and jupyter
f = open("./data_of_time/FCFS/sixtyWaitingTime.txt","r")
for i in f:
    wait_gp_FCFS.append(int(i.strip("\n")))
f.close()

f = open("./data_of_time/SJF/sixtyWaitingTime.txt","r")
for i in f:
    wait_gp_SJF.append(int(i.strip("\n")))
f.close()

f = open("./data_of_time/RR/sixtyWaitingTime.txt","r")
for i in f:
    wait_gp_RR.append(int(i.strip("\n")))
f.close()

Data= {'waiting time(FCFS)': wait_gp_FCFS, 'waiting time(SJF)': wait_gp_SJF,'waiting time(RR)': wait_gp_RR}
dataF = DataFrame(Data,columns=['waiting time(FCFS)','waiting time(SJF)','waiting time(RR)'])
dataF.plot(kind="line")
plotG.xlabel('processes')
plotG.ylabel('waiting time')
plotG.title('60 processes')
plotG.grid(True)

