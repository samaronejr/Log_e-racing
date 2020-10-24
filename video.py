from time import time
import numpy as np
import cv2
import math
from pydarknet import Detector, Image
from constants import *
import loglib

############################################### Log Config ###########################################################
get_frame_v= loglib.get_frame_v()
detect_v = loglib.detect_v()
get_mono_pos_v = loglib.get_mono_pos_v()
get_stereo_pos_v = loglib.get_stereo_pos_v()
get_pos_v = loglib.get_pos_v()
run_v = loglib.run_v()
main_v = loglib.main_v()
zedsdk_v = loglib.zedsdk_v()
opencv_v = loglib.opencv_v()
yolo_v = loglib.yolo_v()
######################################################################################################################

if CAPTURE_MODE == "ZED_SDK":
    import pyzed.sl as sl
    zed = sl.Camera()
    init_params = sl.InitParameters()
    init_params.camera_resolution = sl.RESOLUTION.HD720
    init_params.depth_mode = sl.DEPTH_MODE.PERFORMANCE
    init_params.coordinate_units = sl.UNIT.METER
    err = zed.open(init_params)
    if err != sl.ERROR_CODE.SUCCESS:
        print("ERROR OPENING ZED CAMERA WITH SDK")
        exit(1)
    image = sl.Mat()
    depth_map = sl.Mat()
    point_cloud = sl.Mat()
    runtime_parameters = sl.RuntimeParameters()
    zedsdk_v.info('zed:{}|\ninit_params:{}|\nerr:{}|\nimage:{}|\ndepth_map:{}|\npoint_cloud:{}|\nruntime_parameters:{}'.format(zed,init_params,err,image,depth_map,point_cloud,runtime_parameters))
elif CAPTURE_MODE == "OPENCV":
    cam = cv2.VideoCapture(CAMERA_INDEX)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, OPENCV_CAMERA_WIDTH)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, OPENCV_CAMERA_HEIGHT)
    zedsdk_v.info('cam:{}'.format(cam))

if DETECTION_MODE == "YOLO":
    net = Detector(bytes(YOLO_PATH_CONFIG[YOLO_VERSION], encoding="utf-8"), bytes(YOLO_PATH_WEIGHTS[YOLO_VERSION], encoding="utf-8"), 0, bytes(YOLO_PATH_DATA[YOLO_VERSION],encoding="utf-8"))
    yolo_v.info("net:{}".format(net))




def get_frame():
    if CAPTURE_MODE == "ZED_SDK":
        if zed.grab(runtime_parameters) == sl.ERROR_CODE.SUCCESS:
            # A new image is available if grab() returns SUCCESS
            zed.retrieve_image(image, sl.VIEW.LEFT)
            get_frame_v.info('|0| zed:{}'.format(zed))
        return cv2.cvtColor(image.get_data(), cv2.COLOR_RGBA2RGB)
    else:
        _, frame = cam.read()
        if FLIP_IMG:
            frame = cv2.flip(frame, 0)
            frame = cv2.flip(frame, 1)
        get_frame_v.info('|1| frame:{}'.format(frame))
        return frame[:,:OPENCV_FRAME_WIDTH_CUT,:] # cut half left of image

def detect(frame):
    img_darknet = Image(frame)
    results = net.detect(img_darknet, thresh=DETECTION_THRESHOLD)
    detect_v.info("img_darknet:{}|\nresults:{}".format(img_darknet,results))
    return [[x,y,w,h,cat,score] for cat, score, (x, y, w, h) in results]

def get_mono_pos(rects):
    cones_blue = [[],[]]
    cones_yellow = [[],[]]
    print_info = ""
    for rect in rects:
        y = (CONE_HEIGHT * FOCAL) / (rect[3]*PIXEL_SIZE)
        u = (rect[0]-U_OFFSET)
        x = u*PIXEL_SIZE*y/FOCAL
        v = (rect[1]-V_OFFSET)
        z = v*PIXEL_SIZE*y/FOCAL
        print_info += f"Cone height:{rect[3]} px \n"
        print_info += f"Cone x:{x/10} cm, y:{y/10} cm \n"
        get_mono_pos_v.info("|0| y:{}| u:{}| x:{}| v:{}| z:{}\nprint_info:{}".format(y,u,x,v,z,print_info))
        x /= 1000
        x += X_OFFSET
        y /= 1000
        z /= 1000

        ratio = rect[2]/rect[3]
        get_mono_pos_v.info("|1| y:{}| u:{}| x:{}| v:{}| z:{}| ratio:{}".format(y,u,x,v,z,ratio))
        if MIN_RATIO <= ratio <= MAX_RATIO:
            if MIN_DISTANCE <= y <= MAX_DISTANCE:
                if not math.isinf(x) or not math.isinf(y) or not math.isnan(x) or not math.isnan(y):
                    if rect[4] == b'blue_cone':
                        cones_blue[0].append([x,y])
                        cones_blue[1].append(rect)
                    elif rect[4] == b'yellow_cone':
                        cones_yellow[0].append([x,y])
                        cones_yellow[1].append(rect)
            else:
                ignored_by_y_dist += 1
        else:
            ignored_by_ratio += 1
    get_mono_pos_v.info("|2| ignored_by_y_dist:{}| ignored_by_ratio:{}".format(ignored_by_y_dist,ignored_by_ratio))
    get_mono_pos_v.info("|3| cones_blue:{}|\ncones_yellow:{}|\nprint_info:{}".format(cones_blue,cones_yellow,print_info))
    print_info += f"Input:\n    Cones Detected:{len(rects):>3}\n"
    print_info += f"    Cones Returned:\n        Blue:{len(cones_blue):>5}\n        Yellow:{len(cones_yellow):>3}\n"
    print_info += f"    Ignored cones:\n        Ratio:{ignored_by_ratio:>4}\n        Y Dist:{ignored_by_y_dist:>3}\n"

    return cones_blue, cones_yellow, print_info

def get_stereo_pos(rects):
    cones_blue = [[],[]]
    cones_yellow = [[],[]]
    print_info = ""
    for rect in rects:
        zed.retrieve_measure(point_cloud, sl.MEASURE.XYZRGBA)
        #zed.retrieve_measure(depth_map, sl.MEASURE.DEPTH) # Retrieve depth
        err, point3D = point_cloud.get_value(rect[0],rect[1])
        get_stereo_pos_v.info("|0| err:{}|\npoint3D:{}|\nzed:{}".format(err, point3D,zed))
        if err == sl.ERROR_CODE.SUCCESS:
            x = point3D[0]
            z = point3D[1]
            y = point3D[2]
            get_stereo_pos_v.info("|1| x:{}|\ny:{}|\nz:{}".format(x, y,z))
            if not math.isinf(x) and not math.isinf(y) and not math.isnan(x) and not math.isnan(y):
                if rect[4] == b'blue_cone' or rect[4] == b'BLUE_CONE':
                    cones_blue[0].append([y,-x + X_OFFSET ])
                    cones_blue[1].append(rect)
                elif rect[4] == b'yellow_cone' or rect[4] == b'YELLOW_CONE':
                    cones_yellow[0].append([y,-x + X_OFFSET])
                    cones_yellow[1].append(rect)
    get_mono_pos_v.info("|2| cones_blue:{}|\ncones_yellow:{}".format(cones_blue,cones_yellow))
    return cones_blue, cones_yellow, print_info

def get_pos(rects):
    if MESURMENT_MODE == "MONO":
        cones_blue, cones_yellow, print_info = get_mono_pos(rects)
    elif MESURMENT_MODE == "STEREO":
        cones_blue, cones_yellow, print_info = get_stereo_pos(rects)

    get_pos_v.info("cones_blue:{}\ncones_yellow:{}\nprint_info:{}".format(cones_blue, cones_yellow, print_info))
    return cones_blue, cones_yellow, print_info


def run():
    frame_time_start = time()
    frame = get_frame()
    frame_time = (time() - frame_time_start) * 1000

    detect_time_start = time()
    rects = detect(frame)
    detect_time = (time() - detect_time_start) * 1000
    run_v.info("|0| frame_time_start:{}| frame_time:{}| detect_time_start:{}| rects:{}| detect_time:{}\nframe:{}".format(frame_time_start,frame_time,detect_time_start,rects,detect_time,frame))
    img = frame.copy()

    frame_time_start = time()
    cones_blue, cones_yellow, print_info = get_pos(rects)
    get_pos_time = (time() - frame_time_start) * 1000
    run_v.info("|1| frame_time_start:{}| get_pos_time:{}| cones_blue:{}| cones_yellow:{}| print_info:{}\nimg:{}".format(frame_time_start,get_pos_time,cones_blue,cones_yellow,print_info,img))
    if SHOW_IMG:
        if len(cones_blue[0]):
            for i in range(len(cones_blue[0])):
                x,y = cones_blue[0][i]
                u,v,w,h,cat,_ = cones_blue[1][i]
                cv2.rectangle(img, (int(u - w / 2), int(v - h / 2)), (int(u + w / 2), int(v + h / 2)), (255, 0, 0), thickness=2)
                cv2.putText(img, str(f"x:{x:.2f} m"),(int(u),int(v)),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,0))
                cv2.putText(img, str(f"y:{y:.2f} m"),(int(u),int(v+30)),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,0))

        if len(cones_yellow[0]):
            for i in range(len(cones_yellow[0])):
                x,y = cones_yellow[0][i]
                u,v,w,h,cat,_ = cones_yellow[1][i]
                cv2.rectangle(img, (int(u - w / 2), int(v - h / 2)), (int(u + w / 2), int(v + h / 2)), (0, 255, 255), thickness=2)
                cv2.putText(img, str(f"x:{x:.2f} m"),(int(u),int(v)),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,0))
                cv2.putText(img, str(f"y:{y:.2f} m"),(int(u),int(v+30)),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,0))


    print_info += f"    Times:\n        Frame:{frame_time:>7.0f} ms\n        Detect:{detect_time:>6.0f} ms\n        get_pos:{get_pos_time:>5.0f} ms\n\n"
    run_v.info("|2| x:{}| y:{}| u:{}| v:{}| w:{}| h:{}| cat:{}| _:{}\nprint_info:{}".format(x,y,u,v,w,h,cat,_,print_info))
    return np.array(cones_blue[0]), np.array(cones_yellow[0]), print_info, img


if __name__ == "__main__":
    print("Starting test")

    blue, yellow , print_info, img = run()
    main_v.info("blue:{}| yellow:{}\nprint_info:{}\nimg:{}".format(blue,yellow,print_info,img))
    print(f"blue cones: {blue}\nyellow cones: {yellow}\n")
