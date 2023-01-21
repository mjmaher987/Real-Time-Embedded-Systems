
from __future__ import unicode_literals






import math


class Event_EDF:
    def __init__(self, arrival=None, duration=None, deadline=None):
        self.arrival = int(arrival)
        self.duration = int(duration)
        self.deadline = int(deadline)


class Event_RMS:
    def __init__(self, period=None, execution_time=None):
        self.period = int(period)
        self.execution_time = int(execution_time)


def scan_events_console(type):
    print('Enter events in console\nWhen it is finished, enter \'finish\' in separate line')
    all_events = []
    while True:
        event_string = input()
        if event_string == 'finish':
            break
        event_array = event_string.split()
        if type == 1:
            created_event = Event_EDF(event_array[0], event_array[1], event_array[2])
            all_events.append(created_event)
        else:
            created_event = Event_RMS(event_array[0], event_array[1])
            all_events.append(created_event)
    return all_events


def read_events_file(type):
    print('Save events in events.txt file and then enter 1')

    while True:
        chosen = input()
        if chosen == '1':
            break

        print('Please Enter valid input')
    with open('events.txt', mode='r') as file:
        lines = file.readlines()
        all_events = []
        for event in lines:
            event_string = event.replace('\n', '')
            event_array = event_string.split()
            if type == 1:
                created_event = Event_EDF(event_array[0], event_array[1], event_array[2])
                all_events.append(created_event)
            else:
                created_event = Event_RMS(event_array[0], event_array[1])
                all_events.append(created_event)
        return all_events


def scan_events():
    type_schedule = scan_type()
    print("Choose how to insert events:\nEnter 1 if you want to insert in console."
          "\nEnter 2 if you want to insert data using file")

    while True:
        chosen = input()
        if chosen == '1':
            return scan_events_console(type_schedule), type_schedule
        elif chosen == '2':
            return read_events_file(type_schedule), type_schedule
        print('Please Enter valid input')


def scan_type():
    print('Enter 1 for EDF, 2 for RMS')
    while True:
        type_schedule = input()
        if type_schedule == '1':
            return 1
        elif type_schedule == '2':
            return 2
        print('Please Enter valid input')


def EDF(events):
    number_events = len(events)
    answer = []
    deadlines = [(events[arg].deadline, arg) for arg in range(number_events)]
    remained_times = [(events[arg].duration, arg) for arg in range(number_events)]
    arrivals = [(events[arg].arrival, arg) for arg in range(number_events)]
    max_deadline = max(deadlines)[0]

    in_progress = -1
    done = []

    starttime = 0
    for time in range(0, max_deadline + 1):
        # print(remained_times)
        signaled = []
        for arrival_tuple in arrivals:
            start_time = arrival_tuple[0]
            index = arrival_tuple[1]
            if start_time <= time:
                signaled.append(deadlines[index])

        signaled.sort()
        delete = []
        for x in signaled:
            if x[0] <= time or x[1] in done:
                delete.append(x)
        for x in delete:
            signaled.remove(x)
        if len(signaled) > 0:
            # print("***************")
            to_start = signaled[0][1]
            if in_progress != to_start:
                if in_progress != -1:
                    # print("number " + str(in_progress) + " continued")
                    remained_times[in_progress] = remained_times[in_progress][0] - 1, in_progress
                    answer.append((starttime, time, in_progress + 1))
                    if remained_times[in_progress][0] == 0:
                        done.append(in_progress)
                        # print("number " + str(in_progress) + " finished")

                # print("number " + str(to_start) + " started")
                starttime = time
                in_progress = to_start
            else:
                # print("number " + str(to_start) + " continued")
                remained_times[to_start] = (remained_times[to_start][0] - 1, to_start)
                if remained_times[to_start][0] == 0:
                    in_progress = -1
                    done.append(to_start)
                    # print("number " + str(to_start) + " finished")
                    answer.append((starttime, time, to_start + 1))

                    delete = []
                    for x in signaled:
                        if x[0] < time or x[1] in done:
                            delete.append(x)
                    for x in delete:
                        signaled.remove(x)
                    if len(signaled) > 0:
                        # print("number " + str(signaled[0][1]) + " started")
                        starttime = time
                        in_progress = signaled[0][1]
                else:
                    in_progress = to_start

            # print("time = " + str(time))
        else:
            if in_progress != -1:
                remained_times[in_progress] = (remained_times[in_progress][0] - 1, in_progress)
                answer.append((starttime, time, in_progress + 1))
            in_progress = -1
    # print(remained_times)
    return answer, number_events, max_deadline


def LCM(periods):
    values = [x[0] for x in periods]
    answer = 1
    for x in values:
        answer = math.lcm(answer, x)
    return answer


def RMS(events):
    number_events = len(events)
    answer = []
    periods = [(events[arg].period, arg) for arg in range(number_events)]
    execution_times = [(events[arg].execution_time, arg) for arg in range(number_events)]

    main_arr = [(index, 0, math.inf, execution_times[index][0]) for index in range(number_events)]

    periods.sort(reverse=False)
    print(periods)
    # print(periods)
    lcm = LCM(periods)
    print(lcm)
    # print(main_arr)
    for time in range(0, lcm + 1):
        # print('**\ntime is ' + str(time))
        for period in periods:
            if time % period[0] == 0:
                # print('task ' + str(period[1]) + ' released')
                index_released = period[1]
                main_arr[index_released] = (
                    index_released, time, time + periods[index_released][0], execution_times[index_released][0])
        for period in periods:
            index_ = period[1]
            info = main_arr[index_]
            start = info[1]
            end = info[2]
            exec = info[3]
            if exec > 0:
                answer.append((time, time + 1, index_ + 1))
                # print("Execute task " + str(index_) + " from " + str(time) + " to " + str(time + 1))
                main_arr[index_] = (index_, start, end, exec - 1)
                break
        else:
            print("Nothing to do at = " + str(time))
            # if main_arr[]
        # print(main_arr)

    return answer, number_events, lcm + 1


def schedule_events(events, type_schedule):
    if type_schedule == 1:
        return EDF(events)
    else:
        return RMS(events)


def visualize_events(schedule, n, m):
    import matplotlib.pyplot as plt

    plt.xticks([x1 for x1 in range(0, m + 1)])
    plt.yticks([x2 for x2 in range(1, n + 1)])
    for x in schedule:
        plt.plot([x[0], x[1]], [x[2], x[2]], 'k-', linewidth=5)
    plt.show()


if __name__ == '__main__':
    events, type = scan_events()
    schedule, n, m = schedule_events(events, type)
    print(schedule)
    visualize_events(schedule, n, m)

# Test Case 1 for EDF:
# 0 10 33
# 4 3 28
# 5 10 29
# finish

# Test Case 2 for EDF:
# 30 7 40
# 4 6 11
# 2 10 15
# finish

# example input for RMS
# 6 2
# 4 1
# finish

# example input for RMS
# 8 3
# 5 3
# finish
