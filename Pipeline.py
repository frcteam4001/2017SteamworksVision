import copy

def process(frame):
    frame.resize(320, 240)
    orig = copy.deepcopy(frame)

    frame.color_hls()
    mask = frame.threshold([83, 69, 165], [100, 203, 207])
    mask.blur(2)

    mask.contours_filter(area=(400, -1))
    for idx, cnt in enumerate(mask.contours):
        print('area: ' + cnt.area)
        print('width', cnt.width)
        print('height', cnt.height)
        print('center_x', cnt.center_x)
        print('center_y', cnt.center_y)
    return orig