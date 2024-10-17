class Process:
    def __init__(self, pid, burst_time, arrival_time):
        self.pid = pid
        self.burst_time = burst_time
        self.arrival_time = arrival_time
        self.remaining_time = burst_time
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0

def srtf_scheduling(processes):
    n = len(processes)
    current_time = 0
    completed = 0
    completed_processes = []

    while completed < n:
        # Get all processes that have arrived and have remaining time
        available_processes = [p for p in processes if p.arrival_time <= current_time and p.remaining_time > 0]

        if not available_processes:
            current_time += 1
            continue

        # Select the process with the shortest remaining time
        shortest_process = min(available_processes, key=lambda x: x.remaining_time)
        shortest_process.remaining_time -= 1
        current_time += 1

        # If the process is completed
        if shortest_process.remaining_time == 0:
            completed += 1
            shortest_process.completion_time = current_time
            shortest_process.turnaround_time = shortest_process.completion_time - shortest_process.arrival_time
            shortest_process.waiting_time = shortest_process.turnaround_time - shortest_process.burst_time
            completed_processes.append(shortest_process)

    return completed_processes

# Example usage
process_list = [
    Process(pid=1, burst_time=6, arrival_time=2),
    Process(pid=2, burst_time=8, arrival_time=0),
    Process(pid=3, burst_time=7, arrival_time=1),
    Process(pid=4, burst_time=3, arrival_time=3)
]

completed = srtf_scheduling(process_list)

print("PID\tArrival\tBurst\tCompletion\tTurnaround\tWaiting")
for p in completed:
    print(f"{p.pid}\t{p.arrival_time}\t{p.burst_time}\t{p.completion_time}\t\t{p.turnaround_time}\t\t{p.waiting_time}")

