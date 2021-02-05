from math import sin, cos, pi, atan
import numpy as np
import matplotlib.pyplot as plt



# Hyperparameters (all lengths in meters)
L = 1  # Length of arena
H = 1  # Width of arena

B_x = 0     # Earth's magnetic field, replace later
B_y = 1


# Paperbot
d_paper = 0.05    # wheel diameter
w_paper = 0.09    # width of robot


# Segway
d_seg = 0.502
w_seg = 0.53




# run a full simulation
def simulate(input_list, init_state, delta_t, d, w):
    state_list = []
    sensor_list = []
    
    state = init_state
    for inputs in input_list:
        state_list.append(state)
        state, sensor = simulate_step(state, inputs, delta_t, d, w)
        sensor_list.append(sensor)
    
    return state_list, sensor_list


# simulate one time step
def simulate_step(state_k, input_k, delta_t, d, w):
    '''
    Inputs:
    state_t: tuple of x, y, and theta at time k, in that order
    input_t: tuple of left wheel velocity and right wheel velocity, in that order

    Outputs:
    next_state: x, y, and theta at time k+1
    readings: sensor readings for l1, l2, big_omega, b1, and b2
    '''


    x_k = state_k[0]
    y_k = state_k[1]
    theta_k = state_k[2]

    omegaL_k = input_k[0]
    omegaR_k = input_k[1]



    # state update
    x_next = x_k + (-((d*delta_t/4)*sin(theta_k))*omegaR_k) + (((d*delta_t/4)*sin(theta_k))*omegaL_k)    #no noise component yet
    y_next = y_k + (-((d*delta_t/4)*cos(theta_k))*omegaR_k) + (((d*delta_t/4)*cos(theta_k))*omegaL_k)    #no noise component yet
    theta_next = theta_k + ((d*delta_t/(2*w))*omegaR_k) + ((d*delta_t/(2*w))*omegaL_k)                  #no noise component yet

    # bound x between 0 and L
    if x_next < 0.0:
        x_next = 0.0
    elif x_next > L:
        x_next = L

    # bound y between 0 and H
    if y_next < 0:
        y_next = 0.0
    elif y_next > H:
        y_next = H

    # normalize theta between 0 and 2*pi
    if theta_next < 0.0:
        theta_next += 2*pi
    elif theta_next > 2*pi:
        theta_next -= 2*pi



    # Take Readings
    l1_k = H - y_k
    l2_k = L - x_k

    big_omega_k = (d/(2*w))*(omegaR_k+omegaL_k)
    if big_omega_k < 0.0:
        big_omega_k += 2*pi
    elif big_omega_k > 2*pi:
        big_omega_k -= 2*pi

    b1_k = B_x*cos(theta_k) - B_y*sin(theta_k)
    b2_k = B_x*sin(theta_k) + B_y*cos(theta_k)

    next_state = (x_next, y_next, theta_next)
    sensor_readings = (l1_k, l2_k, big_omega_k, b1_k, b2_k)

    return next_state, sensor_readings



def plot_path(state_list, title):
    x = []
    y = []

    for states in state_list:
        x.append(states[0])
        y.append(states[1])

    f = plt.figure(1)
    plt.xlim((0,L))
    plt.ylim((0,H))
    f.set_figheight(5)
    f.set_figwidth(5)
    plt.plot(x,y)
    plt.title(title)
    plt.show()

    
def paperbot():
    #PAPERBOTS

    # Matthew
    init_state = (0.0, 0.0, 45.0)
    right_wheel = read_data('wheel_data/matthew_right.txt')
    left_wheel = read_data('wheel_data/matthew_left.txt')



    input_list = []
    for i in np.arange(len(left_wheel)):
        left_rad = left_wheel[i] * np.pi / 180
        right_rad = right_wheel[i] * np.pi / -180
        input_list.append((left_rad, right_rad))

    delta_t = 0.01   #length of time step

    state_list, sensor_list = simulate(input_list, init_state, delta_t, d_paper, w_paper)
    plot_path(state_list, "Matthew Paperbot")

    x_coord = []
    y_coord = []

    for i in np.arange(len(state_list)):
        x_coord.append(state_list[i][0] - init_state[0])
        y_coord.append(state_list[i][1] - init_state[1])

    #print(x_coord)
    #print()
    #print(y_coord)




    # Ryan
    init_state = (0.0, 0.0, 45.0)
    right_wheel = read_data('wheel_data/ryan_right.txt')
    left_wheel = read_data('wheel_data/ryan_left.txt')


    input_list = []
    for i in np.arange(len(left_wheel)):
        left_rad = left_wheel[i] * np.pi / 180
        right_rad = right_wheel[i] * np.pi / -180
        input_list.append((left_rad, right_rad))

    delta_t = 0.01   #length of time step

    state_list, sensor_list = simulate(input_list, init_state, delta_t, d_paper, w_paper)
    plot_path(state_list, "Ryan Paperbot")
    
    x_coord = []
    y_coord = []

    for i in np.arange(len(state_list)):
        x_coord.append(state_list[i][0])
        y_coord.append(state_list[i][1])

    print(x_coord)
    print()
    print(y_coord)


    '''
 
    # Remy
    init_state = (0.0, 0.0, 45.0)
    right_wheel = read_data('wheel_data/remy_right.txt')
    left_wheel = read_data('wheel_data/remy_left.txt')


    input_list = []
    for i in np.arange(len(left_wheel)):
        left_rad = left_wheel[i] * np.pi / 180
        right_rad = right_wheel[i] * np.pi / -180
        input_list.append((left_rad, right_rad))

    delta_t = 0.01   #length of time step

    state_list, sensor_list = simulate(input_list, init_state, delta_t, d_paper, w_paper)
    plot_path(state_list, "Remy Paperbot")
    
    x_coord = []
    y_coord = []

    for i in np.arange(len(state_list)):
        x_coord.append(state_list[i][0])
        y_coord.append(state_list[i][1])

    #print(x_coord)
    #print()
    #print(y_coord)

    '''





    # Gwen
    init_state = (0.2, 0.3, 45.0)
    right_wheel = read_data('wheel_data/gwen_right.txt')
    left_wheel = read_data('wheel_data/gwen_left.txt')


    input_list = []
    for i in np.arange(len(left_wheel)):
        left_rad = left_wheel[i] * np.pi / 180
        right_rad = right_wheel[i] * np.pi / -180
        input_list.append((left_rad, right_rad))

    delta_t = 0.01   #length of time step

    state_list, sensor_list = simulate(input_list, init_state, delta_t, d_paper, w_paper)
    plot_path(state_list, "Gwen Paperbot")
    
    x_coord = []
    y_coord = []

    for i in np.arange(len(state_list)):
        x_coord.append(state_list[i][0] - init_state[0])
        y_coord.append(state_list[i][1] - init_state[1])

    #print(x_coord)
    #print()
    #print(y_coord)





def segway():
    # SEGWAY

    # Matthew
    init_state = (0.0, 0.0, 45.0)
    right_wheel = read_data('matthew_right.txt')
    left_wheel = read_data('matthew_left.txt')



    input_list = []
    for i in np.arange(len(left_wheel)):
        left_rad = left_wheel[i] * np.pi / 180
        right_rad = right_wheel[i] * np.pi / 180
        input_list.append((left_rad, right_rad))

    delta_t = 0.01   #length of time step

    state_list, sensor_list = simulate(input_list, init_state, delta_t, d_seg, w_seg)
    plot_path(state_list, "Matthew Segway")

    x_coord = []
    y_coord = []

    for i in np.arange(len(state_list)):
        x_coord.append(state_list[i][0] - init_state[0])
        y_coord.append(state_list[i][1] - init_state[1])

    print(x_coord)
    print()
    print(y_coord)




    # Ryan
    init_state = (0.0, 0.0, 45.0)
    right_wheel = read_data('ryan_seg_right.txt')
    left_wheel = read_data('ryan_seg_left.txt')


    input_list = []
    for i in np.arange(len(left_wheel)):
        left_rad = left_wheel[i] * np.pi / 180
        right_rad = right_wheel[i] * np.pi / -180
        input_list.append((left_rad, right_rad))

    delta_t = 0.01   #length of time step

    state_list, sensor_list = simulate(input_list, init_state, delta_t, d_seg, w_seg)
    plot_path(state_list, "Ryan Segway")
    
    x_coord = []
    y_coord = []

    for i in np.arange(len(state_list)):
        x_coord.append(state_list[i][0])
        y_coord.append(state_list[i][1])

    print(x_coord)
    print()
    print(y_coord)



    '''

    # Remy
    init_state = (0.0, 0.0, 45.0)
    right_wheel = read_data('remy_right.txt')
    left_wheel = read_data('remy_left.txt')


    input_list = []
    for i in np.arange(len(left_wheel)):
        left_rad = left_wheel[i] * np.pi / 180
        right_rad = right_wheel[i] * np.pi / -180
        input_list.append((left_rad, right_rad))

    delta_t = 0.01   #length of time step

    state_list, sensor_list = simulate(input_list, init_state, delta_t, d_seg, w_seg)
    plot_path(state_list, "Remy Segway")
    
    x_coord = []
    y_coord = []

    for i in np.arange(len(state_list)):
        x_coord.append(state_list[i][0])
        y_coord.append(state_list[i][1])

    print(x_coord)
    print()
    print(y_coord)





    # Gwen
    init_state = (2, 3, 45.0)
    right_wheel = read_data('gwen_right.txt')
    left_wheel = read_data('gwen_left.txt')


    input_list = []
    for i in np.arange(len(left_wheel)):
        left_rad = left_wheel[i] * np.pi / 180
        right_rad = right_wheel[i] * np.pi / -180
        input_list.append((left_rad, right_rad))

    delta_t = 0.01   #length of time step

    state_list, sensor_list = simulate(input_list, init_state, delta_t, d_seg, w_seg)
    plot_path(state_list, "Gwen Segway")
    
    x_coord = []
    y_coord = []

    for i in np.arange(len(state_list)):
        x_coord.append(state_list[i][0] - init_state[0])
        y_coord.append(state_list[i][1] - init_state[1])

    print(x_coord)
    print()
    print(y_coord)
    '''



def read_data(datafile):
    f = open(datafile, 'r')
    data_str = f.readlines()
    data = []
    for i in np.arange(len(data_str)):
        data_str[i] = data_str[i].replace('\n', '')
        data.append(float(data_str[i]))

    
    return data


def write_data(filename, data):
    f = open(filename, 'w')
    data_str = []
    for i in np.arange(len(data)):
        data_str.append(str(data[i]) + '\n')
    f.writelines(data_str)
    
    


if __name__ == "__main__":
    paperbot()