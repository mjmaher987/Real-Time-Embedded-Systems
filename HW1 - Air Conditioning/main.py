# Mohammad Javad Maheronnaghsh
# 99105691

global_state = 1
S2_state_cooler = 0
S3_state_heater = 0
crs = 0
heater_degree = 0
cooler_on = 0
heater_on = 0


def scan_input():
    return list(map(int, input("Please write the sequence of temperatures separated by space:\n").split()))


def insert_temperature(temperature):
    global global_state
    global S2_state_cooler
    global S3_state_heater
    global crs
    global heater_degree
    global cooler_on
    global heater_on
    if global_state == 1:
        if temperature < 15:
            global_state = 3
            heater_on = 1
            S3_state_heater = 1
            heater_degree = 1
        elif temperature > 35:
            global_state = 2
            cooler_on = 1
            S2_state_cooler = 1
            crs = 4
        return
    elif global_state == 2:
        if S2_state_cooler == 0:
            print("This is error!")
            return
        elif S2_state_cooler == 1:
            if temperature < 25:
                global_state = 1
                cooler_on = 0
                S2_state_cooler = 0
                crs = 0
            elif temperature > 40:
                S2_state_cooler = 2
                crs = 6
            return
        elif S2_state_cooler == 2:
            if temperature < 35:
                S2_state_cooler = 1
                crs = 4
            elif temperature > 45:
                S2_state_cooler = 3
                crs = 8
            return
        elif S2_state_cooler == 3:
            if temperature < 40:
                S2_state_cooler = 2
                crs = 6
            return

    elif global_state == 3:
        if S3_state_heater == 0:
            print("This is an error!")
            return
        elif S3_state_heater == 1:
            if temperature > 30:
                global_state = 1
                heater_on = 0
                S3_state_heater = 0
                heater_degree = 0
            elif temperature < 5:
                S3_state_heater = 2
                heater_degree = 2
            return
        elif S3_state_heater == 2:
            if temperature > 15:
                S3_state_heater = 1
                heater_degree = 1
            elif temperature < -5:
                S3_state_heater = 3
                heater_degree = 3
            return
        elif S3_state_heater == 3:
            if temperature > 5:
                S3_state_heater = 2
                heater_degree = 2
            elif temperature < -20:
                S3_state_heater = 4
                heater_degree = 4
            return
        elif S3_state_heater == 4:
            if temperature > -10:
                S3_state_heater = 3
                heater_degree = 3
            return


if __name__ == '__main__':

    input_sequence = scan_input()
    while input_sequence:
        insert_temperature(input_sequence.pop(0))
        print(f"state = {global_state} - crs = {crs} - heater_degree = {heater_degree}")

        # recommended test case = 25 10 45 50 45 55 55 50 37 30 23 18 13 3 -7 -23 -23
