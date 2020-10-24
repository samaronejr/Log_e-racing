import can
import os
from constants import *
import time
import loglib

############################################### Log Config ###########################################################
bus_c = loglib.bus_c()
createtargetmessage_c = loglib.createtargetmessage_c()
receive_c = loglib.receive_c()
receive_thread_c = loglib.receive_thread_c()
run_c = loglib.run_c()
main_c = loglib.main_c()
######################################################################################################################

if "CAR_SIMULATION" in RUN_FLAGS:
    can_channel = "vcan0"
else:
    can_channel = "can0"
    os.system("sudo ip link set up can0 type can bitrate 500000")
        
bus_filters = [{"can_id": CAN_MOTOR_RPM_ID, "can_mask": 0xfff, "extended": False},
                {"can_id": CAN_STEERING_ID, "can_mask": 0xfff, "extended": False}]
bus = can.interface.Bus(can_channel, bustype='socketcan', receive_own_messages=True)
bus.set_filters(bus_filters)
bus_c.info("bus:{}".format(bus))
motor_rpm = 0
car_speed = 0
steering_sensor = 0



def createTargetMessage(angle):
        steering = angle
        pedal = 1000
        brake = 1000
        mission_finished  = 0
        ebs = 0

        # Format message values
        #steering += STEERING_OFFSET
        steering = steering
        createtargetmessage_c.info("|0| steering:{}".format(steering))
        if steering > 90:
            steering = 90
        if steering < -90:
            steering = -90
        createtargetmessage_c.info("|1| steering:{}".format(steering))
        steering +=128
        steering = int(steering)
        createtargetmessage_c.info("|2| steering:{}".format(steering))

        steer_hex = steering.to_bytes(1, "little")
        createtargetmessage_c.info("|3| steer_hex:{}".format(steer_hex))
        msg_data = [0, 0,
                    0, 0, 
                    0, 0,
                    0,steer_hex[0]]
        return can.Message(arbitration_id=CAN_DRIVERLESS_ID, data=msg_data, extended_id=False)


def receive():
    global motor_rpm, steering_sensor, car_speed, bus
    pass
    print_info = ""
    msg = bus.recv(0.5)
    receive_c.info("|0| msg:{}".format(msg))
    if msg is None:
        print("ERROR: Not receiving CAN messages")
    elif msg.arbitration_id == CAN_MOTOR_RPM_ID:
        motor_rpm = int.from_bytes(msg.data[4:], "big")
        car_speed = motor_rpm * RPM_TO_MS
    receive_c.info("|1| motor_rpm:{}| car_speed:{}".format(motor_rpm,car_speed))
    # NEED FIX
    elif msg.arbitration_id == CAN_STEERING_ID:
        steer_data = int.from_bytes(msg.data[:2], "big")
        steering_sensor = steer_data * (360/ 65536)
        steering_sensor -= STEERING_OFFSET
        if steering_sensor >= 360-STEER_MAX+STEERING_OFFSET:
            steering_sensor = steering_sensor -360
    receive_c.info("|2| steer_data:{}| steering_sensor:{}".formatsteer_data,steering_sensor))
    return motor_rpm,steering_sensor, print_info

def receive_thread():
    global motor_rpm, steering_sensor, car_speed
    while True:
        receive()

def run(angle):
    global motor_rpm, steering_sensor, car_speed
    can_msg = createTargetMessage(angle)
    bus.send(can_msg)
    run_c.info("can_msg:{}\nbus:{}".format(can_msg,bus))


if __name__ == "__main__":
    angle = int(input("steer"))
    main_c.info("angle:{}".format(angle))
    run(angle)
