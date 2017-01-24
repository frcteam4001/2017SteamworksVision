

import copy
import math
import time

from networktables import NetworkTable
import logging

logging.basicConfig(level=logging.DEBUG)  # for pynetworktables
NetworkTable.setIPAddress("roboRIO-4001-FRC.local")
NetworkTable.setClientMode()
NetworkTable.initialize()
table = NetworkTable.getTable("SharkCV")

#FOV_DIAGONAL = 68.5  # Microsoft LifeCam HD 3000
#DISTANCE_SIZE = [20, 14]  # 20x14in target


def Streamtest(frame):
    orig = copy.deepcopy(frame)
    '''
    # THRESHOLD
    frame.color_hsv()
    mask = frame.threshold([75, 155, 55], [100, 255, 255])

    # TWEAKS
    mask.dilate(size=6, iterations=2)

    # CONTOUR PROCESSING
    mask.contours_filter(area=(100, -1), width=(20, -1))
    mask.contours_sort('area')
    if len(mask.contours) > 2:
        mask.contours_filter(area=(mask.contours[2].area, -1))

    # DEBUG OUTPUT
    # mask.contoursDraw(orig, start=0, end=0, color=(0,127,255))
    # mask.contoursDraw(orig, start=1, end=2, color=(44,62,229))

    # PUBLISH INFO
    table.putNumber('time', time.time())
    table_frame = table.getSubTable('frame')
    table_frame.putNumber('width', mask.width)
    table_frame.putNumber('height', mask.height)

    # DISTANCE - CALCULATE CAMERA VERTICAL AND HORIZONTAL FOV
    ASPECT_RATIO = float(frame.width) / float(frame.height)
    FOV_VERTICAL = FOV_DIAGONAL / math.sqrt(1 + math.pow(ASPECT_RATIO, 2))
    FOV_HORIZONTAL = FOV_VERTICAL * ASPECT_RATIO

    # PUBLISH ALL CONTOURS
    for idx, cnt in enumerate(mask.contours):
        table_cnt = table.getSubTable('contours/' + str(idx))
        table_cnt.putNumber('area', cnt.area)
        table_cnt.putNumber('width', cnt.width)
        table_cnt.putNumber('height', cnt.height)
        table_cnt.putNumber('centerX', cnt.center_x)
        table_cnt.putNumber('centerY', cnt.center_y)

        # DISTANCE - CALCULATE DISTANCE BASED ON WIDTH AND HEIGHT
        RATIO_HEIGHT = float(cnt.height) / float(frame.height)
        DISTANCE_HEIGHT = (DISTANCE_SIZE[1] / (2 * RATIO_HEIGHT)) / math.tan((FOV_VERTICAL * (math.pi / 180)) / 2)
        table_cnt.putNumber('distanceHeight', DISTANCE_HEIGHT)
        RATIO_WIDTH = float(cnt.width) / float(frame.width)
        DISTANCE_WIDTH = (DISTANCE_SIZE[0] / (2 * RATIO_WIDTH)) / math.tan((FOV_HORIZONTAL * (math.pi / 180)) / 2)
        table_cnt.putNumber('distanceWidth', DISTANCE_WIDTH)
    '''
    return orig