import copy
import logging
from networktables import NetworkTable


NetworkTable.setIPAddress("127.0.0.1")
NetworkTable.setClientMode()
NetworkTable.initialize()
logging.basicConfig(level=logging.DEBUG)

#wait for connection
while not NetworkTable.isConnected:
    pass

table = NetworkTable.getTable("GearTable")


# X values of the left boundary of zones, assuming the robot is at the correct distance
impossibleLeft = 0
impossibleRight = 0
zone1 = 0
zone2 = 0
zone3 = 0
zone4 = 0



def Pipeline(frame):

    #resize for faster processing/should be moved outside
    frame.resize(320, 240)

    #makes a copy of the original image
    orig = copy.deepcopy(frame)

    #applies filters
    frame.color_hls()
    mask = frame.threshold([70, 100, 50], [100, 190, 155])
    mask.blur(3)

    #if only 1 contour has been found, the robot must be very off
    if len(mask.contours) == 1:
        table.putValue('zone', -1)
    elif len(mask.contours) == 2:
        liftX = mask.contours[0].center_x + mask.contours[1].center_x


        if liftX < impossibleLeft * 1.05:
            table.putValue('zone', -1)
        elif liftX * 1.05 > impossibleRight:
            table.putValue('zone', -1)
        elif zone1 <= liftX < zone2:
            table.putValue('zone', 1)
        elif zone2 <= liftX < zone3:
            table.putValue('zone', 2)
        elif zone3 <= liftX < zone4:
            table.putValue('zone', 3)
        else:
            table.putValue('zone', 4)

    mask.contours_draw(orig)

    return orig