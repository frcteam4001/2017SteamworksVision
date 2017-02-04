import copy
import logging
from networktables import NetworkTable



NetworkTable.setIPAddress("roborio-4001-frc.local")
NetworkTable.setClientMode()
NetworkTable.initialize()

logging.basicConfig(level=logging.DEBUG)

#wait for connection
while not NetworkTable.isConnected():
    pass

logging.info(str(NetworkTable.isConnected()))

table = NetworkTable.getTable("GearZone")



# X values of the left boundary of zones, assuming the robot is at the correct distance
impossibleRight = 233
zone1 = 73
zoneWidth = (impossibleRight - zone1) / 5
zone2 = zone1 + zoneWidth
zone3 = zone2 + zoneWidth
zone4 = zone3 + zoneWidth



def Pipeline(frame):

    #resize for faster processing/should be moved outside
    frame.resize(320, 240)

    #makes a copy of the original image
    orig = copy.deepcopy(frame)

    #applies filters\

    frame.color_hls()

    #mask = frame.threshold([74, 131, 113], [180, 255, 255])
    mask = frame.threshold([76, 60, 60], [180, 255, 255])
    mask.blur(3)
    mask.contours_sort('_area', True)

    #logging.info("# contours --> " + str(len(mask.contours)))

    if len(mask.contours) < 2:
        #if only 1 contour has been found, the robot must be very off
        table.putValue('zone', -1)
        logging.info(-1)

    else:
        #mask.contours_sort("area")
        top_contours = mask.contours[0:2]
        #for i in range(len(top_contours)):#
        #    logging.info(str(top_contours[i].area))


        liftX = (top_contours[0].center_x + top_contours[1].center_x)/2

        if liftX < zone1: #left impossible
            table.putValue('zone', -1)
            logging.info(liftX)
            logging.info(-1)

        elif liftX > impossibleRight:
            table.putValue('zone', -1)
            logging.info(liftX)
            logging.info("hi")

        elif zone1 <= liftX < zone2:
            table.putValue('zone', 1)
            logging.info(liftX)
            logging.info(1)

        elif zone2 <= liftX < zone3:
            table.putValue('zone', 2)
            logging.info(liftX)
            logging.info(2)

        elif zone3 <= liftX < zone4:
            table.putValue('zone', 3)
            logging.info(liftX)
            logging.info(3)

        else:
            table.putValue('zone', 4)
            logging.info(liftX)
            logging.info(4)

    mask.contours_draw(orig)

    return orig