def findWaitingTime(processes, n, bt, wt):
    wt[0] = 0
    for i in range(1, n):
        wt[i] = bt[i - 1] + wt[i - 1]

def findTurnAroundTime(processes, n, bt, wt, tat):
    for i in range(n):
        tat[i] = bt[i] + wt[i]

def findavgTime(processes, n, bt):
    wt = [0] * n
    tat = [0] * n
    total_wt = 0
    total_tat = 0
    findWaitingTime(processes, n, bt, wt)
    findTurnAroundTime(processes, n, bt, wt, tat)

    print("Processes Burst time Waiting time Turn around time")
    for i in range(n):
        total_wt += wt[i]
        total_tat += tat[i]
        print(f" {i + 1}\t\t{bt[i]}\t {wt[i]}\t\t {tat[i]}")

    print(f"Average waiting time = {total_wt / n}")
    print(f"Average turn around time = {total_tat / n}")

if __name__ == "__main__":
    processes = [1, 2, 3]
    n = len(processes)
    burst_time = [10, 5, 8]
    findavgTime(processes, n, burst_time)
