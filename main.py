class process:
    def __init__(self,name,rafaga,time):
        self.name=name
        self.rafaga=rafaga
        self.time=time

    def running_data(self,starTime,finishTime):
        self.starTime=starTime
        self.finishTime=finishTime

    def display(self):
        print(self.name , "\t", end="")
        print(self.rafaga , "\t", end="")
        print(self.time , "\t", end="")


if __name__ == "__main__":

    processList=[]
    halt=False

    print("\t\t Welcome \n\n")
    while(not halt):
        name=input("type process name: ")
        rafaga=int(input("type process rafaga: "))
        time=int(input("type process arrival time: "))

        p1=process(name,rafaga,time)
        processList.append(p1)
        print("\n\n")
        print("add more processes? 1:true, anything else: false\n")
        choice=int(input())
        if choice != 1:
            halt=True

    print("\n\n")
    for p in processList:
        p.display()


    print("\n\n\nEND OF LINE")
