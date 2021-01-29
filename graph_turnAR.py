#%%
import matplotlib.pyplot as plotG
from pandas import DataFrame

turn_gp_FCFS= []

turn_gp_SJF = []

turn_gp_RR = []

# import file "./" run with python and jupyter
f = open("./data_of_time/FCFS/sixtyTurnARTime.txt","r")
for i in f:
    turn_gp_FCFS.append(int(i.strip("\n")))
f.close()

f = open("./data_of_time/SJF/sixtyTurnARTime.txt","r")
for i in f:
    turn_gp_SJF.append(int(i.strip("\n")))
f.close()

f = open("./data_of_time/RR/sixtyTurnARTime.txt","r")
for i in f:
    turn_gp_RR.append(int(i.strip("\n")))
f.close()

Data= {'turn around time(FCFS)': turn_gp_FCFS, 'turn around time(SJF)': turn_gp_SJF,'turn around time(RR)': turn_gp_RR}
dataF = DataFrame(Data,columns=['turn around time(FCFS)','turn around time(SJF)','turn around time(RR)'])
dataF.plot(kind="line")
plotG.xlabel('processes')
plotG.ylabel('waiting time')
plotG.title('60 processes')
plotG.grid(True)


# %%
