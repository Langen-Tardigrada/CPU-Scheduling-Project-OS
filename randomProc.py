import random

# declare 3 objects list brust time processes
twenty_proc = []
forty_proc = []
sixty_proc = []


# random 20 processes
# declare counter for upper bound part of number of brust times
in20 = 0
in40 = 0
in40_2 = 0
i = 0
while i<20:
    x = random.randint(1,100)
    i += 1
    
    # condition: number of brust times have 20%(value35,50),40%(value20,30),40%(value2,8)
    if x>0 and x<=20 and in20<4:    
        twenty_proc.append(random.randint(35,40))
        in20 += 1
    elif x>20 and x<=60 and in40<8:
        twenty_proc.append(random.randint(20,30))
        in40 += 1
    elif x>60 and x<=100 and in40_2<8:
        twenty_proc.append(random.randint(2,8))
        in40_2 += 1
    else:
        i -= 1

print(twenty_proc, len(twenty_proc))


# random 40 processes
# declare counter for upper bound part of number of brust times
in20 = 0
in40 = 0
in40_2 = 0
i = 0
while i<40:
    x = random.randint(1,100)
    i += 1

    # condition: number of brust times have 20%(value35,50),30%(value20,30),50%(value2,8)
    if x>0 and x<=20 and in20<8:    
        forty_proc.append(random.randint(35,40))
        in20 += 1
    elif x>20 and x<=50 and in40<12:
        forty_proc.append(random.randint(20,30))
        in40 += 1
    elif x>50 and x<=100 and in40_2<20:
        forty_proc.append(random.randint(2,8))
        in40_2 += 1
    else:
        i -= 1

print(forty_proc, len(forty_proc))


# random 60 processes
# declare counter for upper bound part of number of brust times
in20 = 0
in40 = 0
in40_2 = 0
i = 0
while i<60:
    x = random.randint(1,100)
    i += 1

    # condition: number of brust times have 10%(value35,50),20%(value20,30),70%(value2,8)
    if x>0 and x<=10 and in20<6:    
        sixty_proc.append(random.randint(35,40))
        in20 += 1
    elif x>10 and x<=30 and in40<12:
        sixty_proc.append(random.randint(20,30))
        in40 += 1
    elif x>30 and x<=100 and in40_2<42:
        sixty_proc.append(random.randint(2,8))
        in40_2 += 1
    else:
        i -= 1

print(sixty_proc, len(sixty_proc))

# create 3 files

# ---20 processes
f = open("./process/twentyProcess.txt","w")
for i in range(20):
    f.write(str(twenty_proc[i])+'\n') 
f.close()

# --40 processes
f = open("./process/fortyProcess.txt","w")
for i in range(40):
    f.write(str(forty_proc[i])+'\n')
f.close()

# ---60 processes
f = open("./process/sixtyProcess.txt","w")
for i in range(60):
    f.write(str(sixty_proc[i])+'\n')
f.close()