class SJF:
    def processData(self):
        with open('input.txt') as file:
            lines = [line.rstrip() for line in file]
            lines = list(map(int, lines))

            # print(lines[0])
        process_data = []
        count = 1
        for i in range(1,(lines[0] + 1)):
            temporary = []
            process_id = lines[count]

            arrival_time = lines[count + 1]

            burst_time = lines[count + 2]
            count = count + 3
            temporary.extend([process_id, arrival_time, burst_time, 0])

            # 0 la chua hoan thanh, 1 la da hoan thanh (trang thai cua process)

            process_data.append(temporary)
            
        SJF.schedulingProcess(self, process_data)

    def schedulingProcess(self, process_data):
        start_time = []
        exit_time = []
        b_time = 0
        process_data.sort(key=lambda x: x[1])

        # sap xep Arrival Time theo thu tu tu be den lon

        for i in range(len(process_data)):
            ready_queue = []
            temp = []
            normal_queue = []
            # print(process_data)

            for j in range(len(process_data)):
                if (process_data[j][1] <= b_time) and (process_data[j][3] == 0):
                    temp.extend([process_data[j][0], process_data[j][1], process_data[j][2]])
                    ready_queue.append(temp)
                    temp = []
                elif process_data[j][3] == 0:
                    temp.extend([process_data[j][0], process_data[j][1], process_data[j][2]])
                    normal_queue.append(temp)
                    temp = []

            if len(ready_queue) != 0:
                ready_queue.sort(key=lambda x: x[2])

                # sap xep Burst Time

                start_time.append(b_time)
                b_time = b_time + ready_queue[0][2]
                end_time = b_time
                exit_time.append(end_time)
                for k in range(len(process_data)):
                    if process_data[k][0] == ready_queue[0][0]:
                        break
                process_data[k][3] = 1
                process_data[k].append(end_time)
                # print(process_data)

            elif len(ready_queue) == 0:
                # so sanh arrival time cua hang doi
                if b_time < normal_queue[0][1]:
                    b_time = normal_queue[0][1]
                start_time.append(b_time)
                b_time = b_time + normal_queue[0][2]
                end_time = b_time
                exit_time.append(end_time)
                for k in range(len(process_data)):
                    if process_data[k][0] == normal_queue[0][0]:
                        break
                process_data[k][3] = 1
                process_data[k].append(end_time)
                # print(process_data)

        # print(process_data)
        t_time = SJF.calculateTurnaroundTime(self, process_data)
        w_time = SJF.calculateWaitingTime(self, process_data)
        SJF.printData(self, process_data, t_time, w_time)



    def calculateTurnaroundTime(self, process_data):
        total_turnaround_time = 0
        for i in range(len(process_data)):
            turnaround_time = process_data[i][4] - process_data[i][1]

            # turnaround_time = completion_time - arrival_time

            total_turnaround_time = total_turnaround_time + turnaround_time
            process_data[i].append(turnaround_time)
        average_turnaround_time = total_turnaround_time / len(process_data)

        # average_turnaround_time = total_turnaround_time / no_of_processes

        return average_turnaround_time


    def calculateWaitingTime(self, process_data):
        total_waiting_time = 0
        for i in range(len(process_data)):
            waiting_time = process_data[i][5] - process_data[i][2]
            '''
            waiting_time = turnaround_time - burst_time
            '''
            total_waiting_time = total_waiting_time + waiting_time
            process_data[i].append(waiting_time)
        average_waiting_time = total_waiting_time / len(process_data)

        # average_waiting_time = total_waiting_time / no_of_processes


        return average_waiting_time



    def printData(self, process_data, average_turnaround_time, average_waiting_time):
        print(process_data)
        file = open("output.txt", "a+")
        process_data.sort(key=lambda x: x[0])

        # sap xep theo Process ID

        print("Process_ID  Arrival_Time  Burst_Time      Completed  Completion_Time  Turnaround_Time  Waiting_Time")

        for i in range(len(process_data)):
            for j in range(len(process_data[i])):
                # res = process_data[i][j], end="				"
                print(process_data[i][j], end="				")

            print()


        print(f'Average Turnaround Time: {average_turnaround_time}')
        file.write(f'Average Turnaround Time: {average_turnaround_time}')
        file.write("\n")
        print(f'Average Waiting Time: {average_waiting_time}')
        file.write(f'Average Waiting Time: {average_waiting_time}')
        file.write("\n")
        file.write("\n")
        file.close()


if __name__ == "__main__":
    # no_of_processes = int(input("Enter number of processes: "))
    sjf = SJF()
    sjf.processData()