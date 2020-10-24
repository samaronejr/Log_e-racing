import logging
from logging import Logger
######################################################################################################################
##                                                  Controller2                                                     ##
######################################################################################################################
class size2(Logger):
    def __init__(self,log_file=None,log_format="%(asctime)s\n%(message)s"):
        self.formatter = logging.Formatter(log_format)
        self.log_file = log_file
        Logger.__init__(self,'controller2_run_size.log')
        self.addHandler(self.get_file_handler())
        logging.basicConfig(filename='controller2_run_size.log', level=logging.INFO)
    def get_file_handler(self):
        file_handler = logging.FileHandler('controller2_run_size.log')
        file_handler.setFormatter(self.formatter)
        return file_handler
######################################################################################################################
class a_m_p2(Logger):
    def __init__(self,log_file=None,log_format="%(asctime)s\n%(message)s"):
        self.formatter = logging.Formatter(log_format)
        self.log_file = log_file
        Logger.__init__(self,"controller2_run_angle_mid_print.log")
        self.addHandler(self.get_file_handler())
        logging.basicConfig(filename='controller2_run_angle_mid_print.log', level=logging.INFO)
    def get_file_handler(self):
        file_handler = logging.FileHandler("controller2_run_angle_mid_print.log")
        file_handler.setFormatter(self.formatter)
        return file_handler
######################################################################################################################
class b_y_r2(Logger):
    def __init__(self,log_file=None,log_format="%(asctime)s\n%(message)s"):
        self.formatter = logging.Formatter(log_format)
        self.log_file = log_file
        Logger.__init__(self,"controller2_main_blue_yellow_result.log")
        self.addHandler(self.get_file_handler())
        logging.basicConfig(filename='controller2_main_blue_yellow_result.log', level=logging.INFO)

    def get_file_handler(self):
        file_handler = logging.FileHandler("controller2_main_blue_yellow_result.log")
        file_handler.setFormatter(self.formatter)
        return file_handler
######################################################################################################################
class yel_blue2(Logger):
    def __init__(self,log_file=None,log_format="%(asctime)s\n%(message)s"):
        self.formatter = logging.Formatter(log_format)
        self.log_file = log_file
        Logger.__init__(self,"controller2_main_yel_blue.log")
        self.addHandler(self.get_file_handler())
        logging.basicConfig(filename='controller2_main_yel_blue.log', level=logging.INFO)
    def get_file_handler(self):
        file_handler = logging.FileHandler("controller2_main_yel_blue.log")
        file_handler.setFormatter(self.formatter)
        return file_handler
######################################################################################################################
class lots_of_cones2(Logger):
    def __init__(self,log_file=None,log_format="%(asctime)s\n%(message)s"):
        self.formatter = logging.Formatter(log_format)
        self.log_file = log_file
        Logger.__init__(self,"controller2_lots_of_cones.log")
        self.addHandler(self.get_file_handler())
        logging.basicConfig(filename='controller2_lots_of_cones.log', level=logging.INFO)
    def get_file_handler(self):
        file_handler = logging.FileHandler("controller2_lots_of_cones.log")
        file_handler.setFormatter(self.formatter)
        return file_handler
######################################################################################################################
class angle_to_point2(Logger):
    def __init__(self,log_file=None,log_format="%(asctime)s\n%(message)s"):
        self.formatter = logging.Formatter(log_format)
        self.log_file = log_file
        Logger.__init__(self,"controller2_angle_to_point.log")
        self.addHandler(self.get_file_handler())
        logging.basicConfig(filename='controller2_angle_to_point.log', level=logging.INFO)
    def get_file_handler(self):
        file_handler = logging.FileHandler("controller2_angle_to_point.log")
        file_handler.setFormatter(self.formatter)
        return file_handler
######################################################################################################################
class dist2(Logger):
    def __init__(self,log_file=None,log_format="%(asctime)s\n%(message)s"):
        self.formatter = logging.Formatter(log_format)
        self.log_file = log_file
        Logger.__init__(self,"controller2_dist.log")
        self.addHandler(self.get_file_handler())
        logging.basicConfig(filename='controller2_dist.log', level=logging.INFO)
    def get_file_handler(self):
        file_handler = logging.FileHandler("controller2_dist.log")
        file_handler.setFormatter(self.formatter)
        return file_handler
######################################################################################################################
class closest_point2(Logger):
    def __init__(self,log_file=None,log_format="%(asctime)s\n%(message)s"):
        self.formatter = logging.Formatter(log_format)
        self.log_file = log_file
        Logger.__init__(self,"controller2_closest_point.log")
        self.addHandler(self.get_file_handler())
        logging.basicConfig(filename='controller2_closest_point.log', level=logging.INFO)
    def get_file_handler(self):
        file_handler = logging.FileHandler("controller2_closest_point.log")
        file_handler.setFormatter(self.formatter)
        return file_handler
######################################################################################################################
class sort_cones2(Logger):
    def __init__(self,log_file=None,log_format="%(asctime)s\n%(message)s"):
        self.formatter = logging.Formatter(log_format)
        self.log_file = log_file
        Logger.__init__(self,"controller2_sort_cones.log")
        self.addHandler(self.get_file_handler())
        logging.basicConfig(filename='controller2_sort_cones.log', level=logging.INFO)
    def get_file_handler(self):
        file_handler = logging.FileHandler("controller2_sort_cones.log")
        file_handler.setFormatter(self.formatter)
        return file_handler
######################################################################################################################
class gonna_hit2(Logger):
    def __init__(self,log_file=None,log_format="%(asctime)s\n%(message)s"):
        self.formatter = logging.Formatter(log_format)
        self.log_file = log_file
        Logger.__init__(self,"controller2_gonna_hit.log")
        self.addHandler(self.get_file_handler())
        logging.basicConfig(filename='controller2_gonna_hit.log', level=logging.INFO)
    def get_file_handler(self):
        file_handler = logging.FileHandler("controller2_gonna_hit.log")
        file_handler.setFormatter(self.formatter)
        return file_handler
######################################################################################################################
class get_middle2(Logger):
    def __init__(self,log_file=None,log_format="%(asctime)s\n%(message)s"):
        self.formatter = logging.Formatter(log_format)
        self.log_file = log_file
        Logger.__init__(self,"controller2_get_middle.log")
        self.addHandler(self.get_file_handler())
        logging.basicConfig(filename='controller2_get_middle.log', level=logging.INFO)
    def get_file_handler(self):
        file_handler = logging.FileHandler("controller2_get_middle.log")
        file_handler.setFormatter(self.formatter)
        return file_handler
######################################################################################################################
class one_cone2(Logger):
    def __init__(self,log_file=None,log_format="%(asctime)s\n%(message)s"):
        self.formatter = logging.Formatter(log_format)
        self.log_file = log_file
        Logger.__init__(self,"controller2_one_cone.log")
        self.addHandler(self.get_file_handler())
        logging.basicConfig(filename='controller2_one_cone.log', level=logging.INFO)
    def get_file_handler(self):
        file_handler = logging.FileHandler("controller2_one_cone.log")
        file_handler.setFormatter(self.formatter)
        return file_handler
######################################################################################################################
class get_fake_mid2(Logger):
    def __init__(self,log_file=None,log_format="%(asctime)s\n%(message)s"):
        self.formatter = logging.Formatter(log_format)
        self.log_file = log_file
        Logger.__init__(self,"controller2_get_fake_mid.log")
        self.addHandler(self.get_file_handler())
        logging.basicConfig(filename='controller2_get_fake_mid.log', level=logging.INFO)
    def get_file_handler(self):
        file_handler = logging.FileHandler("controller2_get_fake_mid.log")
        file_handler.setFormatter(self.formatter)
        return file_handler
######################################################################################################################
class one_side2(Logger):
    def __init__(self,log_file=None,log_format="%(asctime)s\n%(message)s"):
        self.formatter = logging.Formatter(log_format)
        self.log_file = log_file
        Logger.__init__(self,"controller2_one_side.log")
        self.addHandler(self.get_file_handler())
        logging.basicConfig(filename='controller2_one_side.log', level=logging.INFO)
    def get_file_handler(self):
        file_handler = logging.FileHandler("controller2_one_side.log")
        file_handler.setFormatter(self.formatter)
        return file_handler

######################################################################################################################
##                                                 Controller                                                       ##
######################################################################################################################
class size(Logger):
    def __init__(self,log_file=None,log_format="%(asctime)s\n%(message)s"):
        self.formatter = logging.Formatter(log_format)
        self.log_file = log_file
        Logger.__init__(self,"controller_run_size.log")
        self.addHandler(self.get_file_handler())
        logging.basicConfig(filename='controller_run_size.log', level=logging.INFO)
    def get_file_handler(self):
        file_handler = logging.FileHandler("controller_run_size.log")
        file_handler.setFormatter(self.formatter)
        return file_handler
######################################################################################################################
class a_m_p(Logger):
    def __init__(self,log_file=None,log_format="%(asctime)s\n%(message)s"):
        self.formatter = logging.Formatter(log_format)
        self.log_file = log_file
        Logger.__init__(self,"controller_run_angle_mid_print.log")
        self.addHandler(self.get_file_handler())
        logging.basicConfig(filename='controller_run_angle_mid_print.log', level=logging.INFO)
    def get_file_handler(self):
        file_handler = logging.FileHandler("controller_run_angle_mid_print.log")
        file_handler.setFormatter(self.formatter)
        return file_handler
######################################################################################################################
class b_y_r(Logger):
    def __init__(self,log_file=None,log_format="%(asctime)s\n%(message)s"):
        self.formatter = logging.Formatter(log_format)
        self.log_file = log_file
        Logger.__init__(self,"controller_main_blue_yellow_result.log")
        self.addHandler(self.get_file_handler())
        logging.basicConfig(filename='controller_main_blue_yellow_result.log', level=logging.INFO)
    def get_file_handler(self):
        file_handler = logging.FileHandler("controller_main_blue_yellow_result.log")
        file_handler.setFormatter(self.formatter)
        return file_handler
######################################################################################################################
class yel_blue(Logger):
    def __init__(self,log_file=None,log_format="%(asctime)s\n%(message)s"):
        self.formatter = logging.Formatter(log_format)
        self.log_file = log_file
        Logger.__init__(self,"controller_main_yel_blue.log")
        self.addHandler(self.get_file_handler())
        logging.basicConfig(filename='controller_main_yel_blue.log', level=logging.INFO)
    def get_file_handler(self):
        file_handler = logging.FileHandler("controller_main_yel_blue.log")
        file_handler.setFormatter(self.formatter)
        return file_handler
######################################################################################################################
class closest_point1(Logger):
    def __init__(self,log_file=None,log_format="%(asctime)s\n%(message)s"):
        self.formatter = logging.Formatter(log_format)
        self.log_file = log_file
        Logger.__init__(self,"controller_closest_point.log")
        self.addHandler(self.get_file_handler())
        logging.basicConfig(filename='controller_closest_point.log', level=logging.INFO)
    def get_file_handler(self):
        file_handler = logging.FileHandler("controller_closest_point.log")
        file_handler.setFormatter(self.formatter)
        return file_handler
######################################################################################################################
class lots_of_cones1(Logger):
    def __init__(self,log_file=None,log_format="%(asctime)s\n%(message)s"):
        self.formatter = logging.Formatter(log_format)
        self.log_file = log_file
        Logger.__init__(self,"controller_lots_of_cones.log")
        self.addHandler(self.get_file_handler())
        logging.basicConfig(filename='controller_lots_of_cones.log', level=logging.INFO)
    def get_file_handler(self):
        file_handler = logging.FileHandler("controller_lots_of_cones.log")
        file_handler.setFormatter(self.formatter)
        return file_handler
######################################################################################################################
class angle_to_point1(Logger):
    def __init__(self,log_file=None,log_format="%(asctime)s\n%(message)s"):
        self.formatter = logging.Formatter(log_format)
        self.log_file = log_file
        Logger.__init__(self,"controller_angle_to_point.log")
        self.addHandler(self.get_file_handler())
        logging.basicConfig(filename='controller_angle_to_point.log', level=logging.INFO)
    def get_file_handler(self):
        file_handler = logging.FileHandler("controller_angle_to_point.log")
        file_handler.setFormatter(self.formatter)
        return file_handler
######################################################################################################################
class sort_cones1(Logger):
    def __init__(self,log_file=None,log_format="%(asctime)s\n%(message)s"):
        self.formatter = logging.Formatter(log_format)
        self.log_file = log_file
        Logger.__init__(self,"controller_sort_cones.log")
        self.addHandler(self.get_file_handler())
        logging.basicConfig(filename='controller_sort_cones.log', level=logging.INFO)
    def get_file_handler(self):
        file_handler = logging.FileHandler("controller_sort_cones.log")
        file_handler.setFormatter(self.formatter)
        return file_handler
######################################################################################################################
class normalize_angle1(Logger):
    def __init__(self,log_file=None,log_format="%(asctime)s\n%(message)s"):
        self.formatter = logging.Formatter(log_format)
        self.log_file = log_file
        Logger.__init__(self,"controller_normalize_angle.log")
        self.addHandler(self.get_file_handler())
        logging.basicConfig(filename='controller_normalize_angle.log', level=logging.INFO)
    def get_file_handler(self):
        file_handler = logging.FileHandler("controller_normalize_angle.log")
        file_handler.setFormatter(self.formatter)
        return file_handler
######################################################################################################################
class gonna_hit1(Logger):
    def __init__(self,log_file=None,log_format="%(asctime)s\n%(message)s"):
        self.formatter = logging.Formatter(log_format)
        self.log_file = log_file
        Logger.__init__(self,"controller_gonna_hit.log")
        self.addHandler(self.get_file_handler())
        logging.basicConfig(filename='controller_gonna_hit.log', level=logging.INFO)
    def get_file_handler(self):
        file_handler = logging.FileHandler("controller_gonna_hit.log")
        file_handler.setFormatter(self.formatter)
        return file_handler
######################################################################################################################
class one_cone1(Logger):
    def __init__(self,log_file=None,log_format="%(asctime)s\n%(message)s"):
        self.formatter = logging.Formatter(log_format)
        self.log_file = log_file
        Logger.__init__(self,"controller_one_cone.log")
        self.addHandler(self.get_file_handler())
        logging.basicConfig(filename='controller_one_cone.log', level=logging.INFO)
    def get_file_handler(self):
        file_handler = logging.FileHandler("controller_one_cone.log")
        file_handler.setFormatter(self.formatter)
        return file_handler
######################################################################################################################
class one_side1(Logger):
    def __init__(self,log_file=None,log_format="%(asctime)s\n%(message)s"):
        self.formatter = logging.Formatter(log_format)
        self.log_file = log_file
        Logger.__init__(self,"controller_one_side.log")
        self.addHandler(self.get_file_handler())
        logging.basicConfig(filename='controller_one_side.log', level=logging.INFO)
    def get_file_handler(self):
        file_handler = logging.FileHandler("controller_one_side.log")
        file_handler.setFormatter(self.formatter)
        return file_handler
######################################################################################################################
class one_on_one_side1(Logger):
    def __init__(self,log_file=None,log_format="%(asctime)s\n%(message)s"):
        self.formatter = logging.Formatter(log_format)
        self.log_file = log_file
        Logger.__init__(self,"controller_one_on_one_side.log")
        self.addHandler(self.get_file_handler())
        logging.basicConfig(filename='controller_one_on_one_side.log', level=logging.INFO)
    def get_file_handler(self):
        file_handler = logging.FileHandler("controller_one_on_one_side.log")
        file_handler.setFormatter(self.formatter)
        return file_handler
######################################################################################################################
class one_on_each_side1(Logger):
    def __init__(self,log_file=None,log_format="%(asctime)s\n%(message)s"):
        self.formatter = logging.Formatter(log_format)
        self.log_file = log_file
        Logger.__init__(self,"controller_one_on_each_side.log")
        self.addHandler(self.get_file_handler())
        logging.basicConfig(filename='controller_one_on_each_side.log', level=logging.INFO)
    def get_file_handler(self):
        file_handler = logging.FileHandler("controller_one_on_each_side.log")
        file_handler.setFormatter(self.formatter)
        return file_handler

######################################################################################################################
##                                                     Main                                                         ##
######################################################################################################################
class velocidade_m(Logger):
    def __init__(self,log_file=None,log_format="%(asctime)s\n%(message)s"):
        self.formatter = logging.Formatter(log_format)
        self.log_file = log_file
        Logger.__init__(self,"main_velocidade.log")
        self.addHandler(self.get_file_handler())
        logging.basicConfig(filename="main_velocidade.log", level=logging.INFO)
    def get_file_handler(self):
        file_handler = logging.FileHandler("main_velocidade.log")
        file_handler.setFormatter(self.formatter)
        return file_handler
######################################################################################################################
class car_pos_m(Logger):
    def __init__(self,log_file=None,log_format="%(asctime)s\n%(message)s"):
        self.formatter = logging.Formatter(log_format)
        self.log_file = log_file
        Logger.__init__(self,"main_car_pos.log")
        self.addHandler(self.get_file_handler())
        logging.basicConfig(filename="main_car_pos.log", level=logging.INFO)
    def get_file_handler(self):
        file_handler = logging.FileHandler("main_car_pos.log")
        file_handler.setFormatter(self.formatter)
        return file_handler
######################################################################################################################
class cones_m(Logger):
    def __init__(self,log_file=None,log_format="%(asctime)s\n%(message)s"):
        self.formatter = logging.Formatter(log_format)
        self.log_file = log_file
        Logger.__init__(self,"main_cones.log")
        self.addHandler(self.get_file_handler())
        logging.basicConfig(filename="main_cones.log", level=logging.INFO)
    def get_file_handler(self):
        file_handler = logging.FileHandler("main_cones.log")
        file_handler.setFormatter(self.formatter)
        return file_handler
######################################################################################################################
class img_m(Logger):
    def __init__(self,log_file=None,log_format="%(asctime)s\n%(message)s"):
        self.formatter = logging.Formatter(log_format)
        self.log_file = log_file
        Logger.__init__(self,"main_img.log")
        self.addHandler(self.get_file_handler())
        logging.basicConfig(filename="main_img.log", level=logging.INFO)
    def get_file_handler(self):
        file_handler = logging.FileHandler("main_img.log")
        file_handler.setFormatter(self.formatter)
        return file_handler
######################################################################################################################
class print_img_m(Logger):
    def __init__(self,log_file=None,log_format="%(asctime)s\n%(message)s"):
        self.formatter = logging.Formatter(log_format)
        self.log_file = log_file
        Logger.__init__(self,"main_print_img.log")
        self.addHandler(self.get_file_handler())
        logging.basicConfig(filename="main_print_img.log", level=logging.INFO)
    def get_file_handler(self):
        file_handler = logging.FileHandler("main_print_img.log")
        file_handler.setFormatter(self.formatter)
        return file_handler
######################################################################################################################
class tripleprints(Logger):
    def __init__(self,log_file=None,log_format="%(asctime)s\n%(message)s"):
        self.formatter = logging.Formatter(log_format)
        self.log_file = log_file
        Logger.__init__(self,"main_tripleprints.log")
        self.addHandler(self.get_file_handler())
        logging.basicConfig(filename="main_tripleprints.log", level=logging.INFO)
    def get_file_handler(self):
        file_handler = logging.FileHandler("main_tripleprints.log")
        file_handler.setFormatter(self.formatter)
        return file_handler
 
######################################################################################################################
##                                                    Video                                                         ##
######################################################################################################################
class get_frame_v(Logger):
    def __init__(self,log_file=None,log_format="%(asctime)s\n%(message)s"):
        self.formatter = logging.Formatter(log_format)
        self.log_file = log_file
        Logger.__init__(self,"video_get_frame.log")
        self.addHandler(self.get_file_handler())
        logging.basicConfig(filename="video_get_frame.log", level=logging.INFO)
    def get_file_handler(self):
        file_handler = logging.FileHandler("video_get_frame.log")
        file_handler.setFormatter(self.formatter)
        return file_handler
######################################################################################################################
class detect_v(Logger):
    def __init__(self,log_file=None,log_format="%(asctime)s\n%(message)s"):
        self.formatter = logging.Formatter(log_format)
        self.log_file = log_file
        Logger.__init__(self,"video_detect.log")
        self.addHandler(self.get_file_handler())
        logging.basicConfig(filename="video_detect.log", level=logging.INFO)
    def get_file_handler(self):
        file_handler = logging.FileHandler("video_detect.log")
        file_handler.setFormatter(self.formatter)
        return file_handler
######################################################################################################################
class get_mono_pos_v(Logger):
    def __init__(self,log_file=None,log_format="%(asctime)s\n%(message)s"):
        self.formatter = logging.Formatter(log_format)
        self.log_file = log_file
        Logger.__init__(self,"video_get_mono_pos.log")
        self.addHandler(self.get_file_handler())
        logging.basicConfig(filename="video_get_mono_pos.log", level=logging.INFO)
    def get_file_handler(self):
        file_handler = logging.FileHandler("video_get_mono_pos.log")
        file_handler.setFormatter(self.formatter)
        return file_handler
######################################################################################################################
class get_stereo_pos_v(Logger):
    def __init__(self,log_file=None,log_format="%(asctime)s\n%(message)s"):
        self.formatter = logging.Formatter(log_format)
        self.log_file = log_file
        Logger.__init__(self,"video_get_stereo_pos.log")
        self.addHandler(self.get_file_handler())
        logging.basicConfig(filename="video_get_stereo_pos.log", level=logging.INFO)
    def get_file_handler(self):
        file_handler = logging.FileHandler("video_get_stereo_pos.log")
        file_handler.setFormatter(self.formatter)
        return file_handler
######################################################################################################################
class get_pos_v(Logger):
    def __init__(self,log_file=None,log_format="%(asctime)s\n%(message)s"):
        self.formatter = logging.Formatter(log_format)
        self.log_file = log_file
        Logger.__init__(self,"video_get_pos.log")
        self.addHandler(self.get_file_handler())
        logging.basicConfig(filename="video_get_pos.log", level=logging.INFO)
    def get_file_handler(self):
        file_handler = logging.FileHandler("video_get_pos.log")
        file_handler.setFormatter(self.formatter)
        return file_handler
######################################################################################################################
class run_v(Logger):
    def __init__(self,log_file=None,log_format="%(asctime)s\n%(message)s"):
        self.formatter = logging.Formatter(log_format)
        self.log_file = log_file
        Logger.__init__(self,"video_run.log")
        self.addHandler(self.get_file_handler())
        logging.basicConfig(filename="video_run.log", level=logging.INFO)
    def get_file_handler(self):
        file_handler = logging.FileHandler("video_run.log")
        file_handler.setFormatter(self.formatter)
        return file_handler
######################################################################################################################
class main_v(Logger):
    def __init__(self,log_file=None,log_format="%(asctime)s\n%(message)s"):
        self.formatter = logging.Formatter(log_format)
        self.log_file = log_file
        Logger.__init__(self,"video_main.log")
        self.addHandler(self.get_file_handler())
        logging.basicConfig(filename="video_main.log", level=logging.INFO)
    def get_file_handler(self):
        file_handler = logging.FileHandler("video_main.log")
        file_handler.setFormatter(self.formatter)
        return file_handler
######################################################################################################################
class zedsdk_v(Logger):
    def __init__(self,log_file=None,log_format="%(asctime)s\n%(message)s"):
        self.formatter = logging.Formatter(log_format)
        self.log_file = log_file
        Logger.__init__(self,"video_zedsdk.log")
        self.addHandler(self.get_file_handler())
        logging.basicConfig(filename="video_zedsdk.log", level=logging.INFO)
    def get_file_handler(self):
        file_handler = logging.FileHandler("video_zedsdk.log")
        file_handler.setFormatter(self.formatter)
        return file_handler
######################################################################################################################
class opencv_v(Logger):
    def __init__(self,log_file=None,log_format="%(asctime)s\n%(message)s"):
        self.formatter = logging.Formatter(log_format)
        self.log_file = log_file
        Logger.__init__(self,"video_opencv.log")
        self.addHandler(self.get_file_handler())
        logging.basicConfig(filename="video_opencv.log", level=logging.INFO)
    def get_file_handler(self):
        file_handler = logging.FileHandler("video_opencv.log")
        file_handler.setFormatter(self.formatter)
        return file_handler
######################################################################################################################
class yolo_v(Logger):
    def __init__(self,log_file=None,log_format="%(asctime)s\n%(message)s"):
        self.formatter = logging.Formatter(log_format)
        self.log_file = log_file
        Logger.__init__(self,"video_yolo.log")
        self.addHandler(self.get_file_handler())
        logging.basicConfig(filename="video_yolo.log", level=logging.INFO)
    def get_file_handler(self):
        file_handler = logging.FileHandler("video_yolo.log")
        file_handler.setFormatter(self.formatter)
        return file_handler

######################################################################################################################
##                                               Can_Interface                                                      ##
######################################################################################################################
class bus_c(Logger):
    def __init__(self,log_file=None,log_format="%(asctime)s\n%(message)s"):
        self.formatter = logging.Formatter(log_format)
        self.log_file = log_file
        Logger.__init__(self,"can_interface_bus.log")
        self.addHandler(self.get_file_handler())
        logging.basicConfig(filename='can_interface_bus.log', level=logging.INFO)
    def get_file_handler(self):
        file_handler = logging.FileHandler("can_interface_bus.log")
        file_handler.setFormatter(self.formatter)
        return file_handler
######################################################################################################################
class createtargetmessage_c(Logger):
    def __init__(self,log_file=None,log_format="%(asctime)s\n%(message)s"):
        self.formatter = logging.Formatter(log_format)
        self.log_file = log_file
        Logger.__init__(self,"can_interface_createtargetmessage.log")
        self.addHandler(self.get_file_handler())
        logging.basicConfig(filename='can_interface_createtargetmessage.log', level=logging.INFO)
    def get_file_handler(self):
        file_handler = logging.FileHandler("can_interface_createtargetmessage.log")
        file_handler.setFormatter(self.formatter)
        return file_handler
######################################################################################################################
class receive_c(Logger):
    def __init__(self,log_file=None,log_format="%(asctime)s\n%(message)s"):
        self.formatter = logging.Formatter(log_format)
        self.log_file = log_file
        Logger.__init__(self,"can_interface_receive.log")
        self.addHandler(self.get_file_handler())
        logging.basicConfig(filename='can_interface_receive.log', level=logging.INFO)
    def get_file_handler(self):
        file_handler = logging.FileHandler("can_interface_receive.log")
        file_handler.setFormatter(self.formatter)
        return file_handler
######################################################################################################################
class run_c(Logger):
    def __init__(self,log_file=None,log_format="%(asctime)s\n%(message)s"):
        self.formatter = logging.Formatter(log_format)
        self.log_file = log_file
        Logger.__init__(self,"can_interface_run.log")
        self.addHandler(self.get_file_handler())
        logging.basicConfig(filename='can_interface_run.log', level=logging.INFO)
    def get_file_handler(self):
        file_handler = logging.FileHandler("can_interface_run.log")
        file_handler.setFormatter(self.formatter)
        return file_handler
######################################################################################################################
class main_c(Logger):
    def __init__(self,log_file=None,log_format="%(asctime)s\n%(message)s"):
        self.formatter = logging.Formatter(log_format)
        self.log_file = log_file
        Logger.__init__(self,"can_interface_main.log")
        self.addHandler(self.get_file_handler())
        logging.basicConfig(filename='can_interface_main.log', level=logging.INFO)
    def get_file_handler(self):
        file_handler = logging.FileHandler("can_interface_main.log")
        file_handler.setFormatter(self.formatter)
        return file_handler
######################################################################################################################