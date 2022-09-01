class process:
    def __init__(self,name,rafaga,time):
        self.name=name
        self.rafaga=rafaga
        self.time=time

    def set_running_data(self,startTime,finishTime):
        self.startTime=startTime
        self.finishTime=finishTime
        self.waitingTime=self.startTime-self.time
        self.systemTime=self.finishTime-self.time

    def display(self):
        print(self.name , "\t", end="")
        print(self.rafaga , "\t", end="")
        print(self.time , "\t")

    def display_start_finish(self):
        print(self.name , "\t", end="")
        print(self.rafaga , "\t", end="")
        print(self.time , "\t", end="")
        print(self.startTime , "\t", end="")
        print(self.finishTime , "\t")

def bubbleSort(arr):
    n = len(arr)
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    swapped = False
    # Traverse through all array elements
    for i in range(n-1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n-i-1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j].time > arr[j + 1].time:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if not swapped:
            # if we haven't needed to make a single swap, we
            # can just exit the main loop.
            return


if __name__ == "__main__":

    processList=[]
    halt=False

    print("\t\t Welcome, this is FIFO dispatch algorithm \n\n")
    while(not halt):
        try:
            name=input("type process abreviated-name: ")
            rafaga=int(input("type process rafaga: "))
            time=int(input("type process arrival time: "))
        except:
            print("input not valid")
            halt=True
            continue

        p1=process(name,rafaga,time)
        processList.append(p1)
        print("\n\n")
        print("add more processes? 1:true, anything else: false\n")
        choice=1
        try:
            choice=int(input())
        except:
            print("input not valid")
            halt=True
            continue
        if choice != 1:
            halt=True

    print("NAME\tRAFAGA\tTIME\t \n\n")
    for p in processList:
        p.display()

    print("\n\n")
    bubbleSort(processList)

    print("\n\n Ordered by arrival time: \n")
    print("NAME\tRAFAGA\tTIME\t \n\n")
    for p in processList:
        p.display()

    tam=len(processList)
    i=0
    temp=0
    rafagaAcumulada=0
    while (i < tam):
        while temp < i:
            rafagaAcumulada+=processList[temp].rafaga
            temp+=1
        processList[i].set_running_data(rafagaAcumulada,rafagaAcumulada+p.rafaga)
        rafagaAcumulada=0
        temp=0
        i+=1

    print("\n\nNAME\tRAFAGA\tTIME\tstart\tfinish \n\n")
    for p in processList:
        p.display_start_finish()

    tam=len(processList)
    i=0
    WT_total=0
    ST_total=0
    while (i < tam):
        WT_total+=processList[i].waitingTime
        ST_total+=processList[i].systemTime
        i+=1
    WT_average=WT_total/tam
    ST_average=ST_total/tam

    print("\n\n")
    print("Waiting Time average: ",str(WT_average))
    print("System Time average: ",str(ST_average))


    print("\n\n\nEND OF LINE")
