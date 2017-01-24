# 2017SteamworksVision

* Vision code to run on a Raspberry Pi 3.
* Utilizes SharkCV courtesy of Team 226 Hammerheads
* Outputs contours to the roboRIO using Networktables
* Images streamed using mjpg-streamer

To run on the Pi, open terminal and run the commands
```
cd PycharmProjects/2017SteamworksVision
python SharkCV/SharkCV.py -vw 320 -vh 240 -wb 0 -wh 127.5 -oj [module.py]
```

To check the image stream, go to 0.0.0.0:5800 on a local browser (on the Pi) or check [device IP]:5800 on a remote browser
