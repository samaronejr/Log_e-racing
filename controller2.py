from time import time
import numpy as np
from constants import *
from math import atan2, degrees, hypot, inf
from utils import rotate
import loglib

############################################### Log Config ###########################################################
size2=loglib.size2()
a_m_p2=loglib.a_m_p2()
b_y_r2=loglib.b_y_r2()
yel_blue2=loglib.yel_blue2()
lots_of_cones2=loglib.lots_of_cones2()
angle_to_point2=loglib.angle_to_point2()
dist2=loglib.dist2()
closest_point2=loglib.closest_point2()
sort_cones2=loglib.sort_cones2()
gonna_hit2=loglib.gonna_hit2()
get_middle2=loglib.get_middle2()
one_cone2=loglib.one_cone2()
get_fake_mid2=loglib.get_fake_mid2()
one_side2=loglib.one_side2()
######################################################################################################################
######## General functions ########
def angle_to_point(point):
    angle_to_point2.info('point:{}'.format(point))
    return degrees(atan2(point[1],point[0]))

# Return distance between 2 points
def dist(p1, p2):
    dist2.info('p1:{}| p2:{}'.format(p1,p2))
    return hypot(p1[0]-p2[0], p1[1]-p2[1])

def closest_point(node, nodes):
    nodes = np.asarray(nodes)
    dist_2 = np.sum((nodes - node)**2, axis=1)
    closest_point2.info('nodes:{}| dist_2:{}'.format(nodes,dist_2))
    return np.argmax(dist_2)

def sort_cones(cones):
    dists = np.sqrt(np.sum(np.square(cones), axis=1))
    sorted_indexes = dists.argsort()
    sort_cones2.info('cones:{}| dists:{}| sorted_indexes:{}'.format(cones,dists,sorted_indexes))
    return cones[sorted_indexes[::]] # sort cones based on dist 

def gonna_hit(cone):
    x,y = cone
    gonna_hit2.info('cone:{}| x:{}| y:{}'.format(cone,x,y))
    if x < FRONT_DISTANCE:
        return (abs(y) < HALF_CAR_WIDTH)
    else:
        return False

def get_middle(blue, yellow):
    # TODO Check if one cone has 2 correspondences
    #sorted_blue = sort_cones(blue)
    #sorted_yellow = sort_cones(yellow)
    middle = []
    for b in blue:
        min_dist = inf
        yellow_selected = None
        get_middle2.info('|0| min_dist:{}| d:{}| blue:{}| b:{}| yellow:{}| y:{}'.format(min_dist,d,blue,b,yellow,y))
        for y in yellow:
            d = dist(b, y)
            if MIN_TRACK_WIDTH <= d <= MAX_TRACK_WIDTH:
                if d < min_dist:
                    min_dist = d
                    yellow_selected = y
            get_middle2.info('|1| min_dist:{}| d:{}| blue:{}| b:{}| yellow:{}| yellow_selected:{}| y:{}'.format(min_dist,d,blue,b,yellow,yellow_selected,y))
        if yellow_selected is not None:
            middle.append(np.average([b, yellow_selected], axis=0))
        get_middle2.info('|2| middle:{}| min_dist:{}| d:{}| blue:{}| b:{}| yellow:{}| yellow_selected:{}| y:{}'.format(middle,min_dist,d,blue,b,yellow,yellow_selected,y))
    return middle

def one_cone(blue, yellow):
    if len(blue)>0:
        angle = STEER_MIN
    elif len(yellow)>0:
        angle = STEER_MAX
    one_cone2.info('blue:{}| yellow:{}| angle:{}'.format(blue,yellow,angle))
    return angle


def get_fake_mid(cones, color):
    mid = []
    cones = sort_cones(cones)
    angle = 0
    size = len(cones)
    for i in range(size):
        #a = angle_to_point([cones[i+1][0]-cones[i][0], cones[i+1][0]-cones[i][1]])
        a = angle_to_point(cones[i])
        print("angle:", a)
        angle = angle+a
        get_fake_mid2.info('|0| angle:{}| size:{}| a:{}| cones[i]:{}'.format(angle,size,a,cones[i]))
    angle = angle/size
    print("final angle:", angle)
    get_fake_mid2.info('|1| final angle:{}| size:{}| cones:{}'.format(angle,size,cones))
    for i in range(size-1):
        m = (cones[i]+cones[i+1])/2
        if color == "blue":
            of = [0, -HALF_TRACK_WIDTH]
        else:
            of = [0, HALF_TRACK_WIDTH]
        of = rotate(of, math.radians(angle))
        print("offset", of)
        mid.append(m+of)
        get_fake_mid2.info('|2| of:{}| mid:{}| m:{}'.format(of,mid,m))

    return mid

def one_side(blue, yellow):
    if len(blue)>0:
        angle = STEER_MIN
        mid = get_fake_mid(blue, "blue")
    elif len(yellow)>0:
        angle = STEER_MAX
        mid = get_fake_mid(yellow, "yellow")
    one_side2.info('angle:{}| mid:{}| blue:{}| yellow:{}'.format(angle,mid,blue,yellow))
    print("mid:", mid)
    return angle, mid

def lots_of_cones(blue, yellow):
    print_info = ""
    mid = get_middle(blue, yellow)
    angle = DEFAULT_ANGLE
    i = closest_point([0,0], mid)
    closest = mid[i]
    look_ahead = dist([0,0], closest)
    mid.insert(0, mid.pop(i))
    angle = angle_to_point(closest)
    lots_of_cones2.info('|0| blue:{}| yellow:{}| i:{}| mid:{}| angle:{}| closest:{}| look_ahead:{}'.format(blue,yellow,i,mid,angle,closest,look_ahead))
    for b in blue:
        if gonna_hit(b):
            angle = STEER_MIN
            print_info += "GOING TO HIT BLUE CONE, IGNORING MIDDLE PATH \n"
            break
    for y in yellow:
        if gonna_hit(y):
            angle = STEER_MAX
            print_info += "GOING TO HIT YELLOW CONE, IGNORING MIDDLE PATH \n"
            break
    lots_of_cones2.info('|1|angle:{}| print_info{}'.format(angle,print_info))
    return angle, mid, print_info

''' 
Parameters:
    blue - np.array( [ [x1,y1], [x2,y2], ... ] )
    yellow - np.array( [ [x1,y1], [x2,y2], ... ] )
'''

last_steer = 0
def run(blue, yellow):
    time_start = time()
    blue_size = blue.shape[0]
    yellow_size = yellow.shape[0]
    total_size = blue_size + yellow_size
    size2.info('blue_size:{}| yellow_size:{}| total_size:{}| blue:{}| yellow:{}|'.format(blue_size,yellow_size,total_size,blue,yellow))
    print_info = f"Controller:\n    Input:\n        Blue size: {blue_size:>5}\n        Yellow size: {yellow_size:>3}\n    "

    if total_size == 0: # no cones
        print_info += "Control Mode: no cones \n"
        angle = last_steer
        mid  = []
        a_m_p2.info('|no cones|angle:{}| mid:{}| print_info:{}'.format(angle,mid,print_info))

    elif total_size == 1: # one cone only
        print_info += "Control Mode: one cone only \n"
        angle, mid = one_cone(blue, yellow)
        last_steer = angle
        mid  = []
        a_m_p2.info('|no cones| angle/last_stear:{}| mid:{}| print_info:{}'.format(angle,mid,print_info))

    elif blue_size == 0 or yellow_size == 0: # cones on only one side
        print_info += "Control Mode: one side only \n"
        angle, mid = one_side(blue, yellow)
        last_steer = angle
        a_m_p2.info('|cones on only one side| angle/last_stear:{}| mid:{}| print_info:{}'.format(angle,mid,print_info))

    else: # one or more cones on both sides
        print_info += "Control Mode: lots of cones \n"
        angle, mid, print_i = lots_of_cones(blue, yellow)
        print_info += print_i
        last_steer = angle
        a_m_p2.info('|one or more cones on both sides| angle/last_stear:{}| mid:{}| print_info:{}'.format(angle,mid,print_info))


    return angle, mid, print_info



if __name__ == "__main__":
    def test(blue, yellow, expected, test_name):
        result = run(blue,yellow)
        b_y_r2.info('test_name:{}| expected:{}| blue:{}| yellow:{}| result:{}'.format(test_name,expected,blue,yellow,result))
        print(f"{test_name} : \nresult: {result} Expected {expected}")
        print("Succeed test" if result == expected else "\n\nFailed test\n\n")
        print()

    ### No cone test
    expected = 0.0
    yel = np.array( [] )
    blue = np.array( [] )
    yel_blue2.info('|no cone|yel:{}| blue:{}'.format(yel,blue))
    test(blue, yel, expected=0.0, test_name="no cone")


    ### One code tests
    # blue
    yel = np.array( [] )
    blue = np.array( [ [1,1] ] )
    yel_blue2.info('|one cone : blue|yel:{}| blue:{}'.format(yel,blue))
    test(blue, yel, expected=MAX_ANGLE, test_name="one cone : blue")

    # yellow
    yel = np.array( [ [1,1] ] )
    blue = np.array( [] )
    yel_blue2.info('|one cone : yellow|yel:{}| blue:{}'.format(yel,blue))
    test(blue, yel, expected=-MAX_ANGLE, test_name="one cone : yellow")


    ### One side tests
    # blue
    yel = np.array( [] )
    blue = np.array( [ [2,1], [1,1] ] )
    yel_blue2.info('|one side : blue|yel:{}| blue:{}'.format(yel,blue))
    test(blue, yel, expected=MAX_ANGLE, test_name="one side : blue")

    # yellow
    yel = np.array( [ [2,1], [1,1] ] )
    blue = np.array( [] )
    yel_blue2.info('|one side : yellow|yel:{}| blue:{}'.format(yel,blue))
    test(blue, yel, expected=-MAX_ANGLE, test_name="one side : yellow")


    ### Only one cone on one side tests
    # blue
    yel = np.array( [[-1, 1]] )
    blue = np.array( [ [2,1], [1,1] ] )
    yel_blue2.info('|only one cone on one side : blue|yel:{}| blue:{}'.format(yel,blue))
    test(blue, yel, expected=0.0, test_name="only one cone on one side : blue")

    # yellow
    yel = np.array( [ [2,1], [1,1] ] )
    blue = np.array( [[-1, 1]] )
    yel_blue2.info('|only one cone on one side : yellow|yel:{}| blue:{}'.format(yel,blue))
    test(blue, yel, expected=-0.0, test_name="only one cone on one side : yellow")


    ### Only one cone on one side tests
    # blue
    yel = np.array( [[-1, 1]] )
    blue = np.array( [ [2,1], [1,1] ] )
    yel_blue2.info('|only one cone on one side : blue|yel:{}| blue:{}'.format(yel,blue))
    test(blue, yel, expected=0.0, test_name="only one cone on one side : blue")

    # yellow
    yel = np.array( [ [2,1], [1,1] ] )
    blue = np.array( [[-1, 1]] )
    yel_blue2.info('|only one cone on one side : yellow|yel:{}| blue:{}'.format(yel,blue))
    test(blue, yel, expected=-0.0, test_name="only one cone on one side : yellow")


    ### One cone on each side tests
    # blue
    yel = np.array( [[-1, 1]] )
    blue = np.array( [ [1,1] ] )
    yel_blue2.info('|one cone on each side : blue|yel:{}| blue:{}'.format(yel,blue))
    test(blue, yel, expected=0.0, test_name="one cone on each side : blue")

    # yellow
    yel = np.array( [ [1,1] ] )
    blue = np.array( [ [-1, 1] ] )
    yel_blue2.info('|one cone on each side : yellow|yel:{}| blue:{}'.format(yel,blue))
    test(blue, yel, expected=-0.0, test_name="one cone on each side : yellow")


    ### Lots of cones tests
    # blue
    yel = np.array( [ [2,1], [1,1] ] )
    blue = np.array( [ [-2,1], [-1,1] ] )
    yel_blue2.info('|lots of cones : blue|yel:{}| blue:{}'.format(yel,blue))
    test(blue, yel, expected=0.0, test_name="lots of cones : blue")

    # yellow
    yel = np.array( [ [2,1], [1,1] ] )
    blue = np.array( [ [-2,1], [-1,1] ] )
    yel_blue2.info('|lots of cones : yellow|yel:{}| blue:{}'.format(yel,blue))
    test(blue, yel, expected=-0.0, test_name="lots of cones : yellow")
