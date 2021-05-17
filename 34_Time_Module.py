# Time Module
import time
timetaken = time.time()
k = 0
while(k < 3):
    print("Happy Birthday!")
    time.sleep(2)
    k += 1
print(f"The wile loop ran in", time.time()-timetaken, "Second")
print("----------------------------------------")
timetaken2 = time.time()
for i in range(3):
    print("Happy Birthday!")
    time.sleep(2)
print(f"The for loop ran in", time.time()-timetaken2, "Second")
