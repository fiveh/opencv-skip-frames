import cv2
import logging


class VideoCam():
    def __init__(self, url=0):
        self.url = url
        self.cap = cv2.VideoCapture(self.url)
        self.get_frame()
        self.get_frame_read()
        logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)

    def check_camera(self, cap):
        logging.info('Camera {} status: {}'.format(self.url, cap.isOpened()))

    def show_frame(self, frame, name_fr='NAME'):
        cv2.imshow(name_fr, frame)
        # cv2.imshow(name_fr, cv2.resize(frame, (0, 0), fx=0.4, fy=0.4))
        cv2.waitKey(1)


    def get_frame(self):
        return self.cap.retrieve()

    def get_frame_read(self):
        return self.cap.read()

    def close_cam(self):
        self.cap.release()
        cv2.destroyAllWindows()

    def restart_capture(self, cap):
        cap.release()
        self.cap = cv2.VideoCapture(self.url)