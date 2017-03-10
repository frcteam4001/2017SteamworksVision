# 2017SteamworksVision

* Vision code to run on a Raspberry Pi 3.
* Utilizes SharkCV courtesy of Team 226 Hammerheads
* Outputs contours to the roboRIO using Networktables
* Images streamed using mjpg-streamer

## Running the vision program (Pipeline.py)
To run on the Pi, open terminal and run the commands
```
cd PycharmProjects/2017SteamworksVision
sudo python SharkCV/SharkCV.py Pipeline.py -vw 320 -vh 240 -wb 10 -oj 
```

## Viewing the MJPEG Stream
To check the image stream, go to 0.0.0.0:5800 in the local browser (on the Pi) or check [device IP]:5800 on a remote browser that is on the same network. 
To get the device ID, open a terminal and enter `hostname -I`

## Editing the Code
Use IDLE to modify the code by entering
```
cd PycharmProjects/2017SteamworksVision
sudo idle Pipeline.py
```

## Running the program on start up
To have the code start running on start up, you need to edit the rc.local file in the /etc directory.
```
sudo idle /etc/rc.local
```

Add the following lines before the `exit 0` line
```
cd PycharmProjects/2017SteamworksVision/
nohup sudo python SharkCV/SharkCV.py Pipeline.py -vw 320 -vh 240 -wb 10 -oj &
```

## Checking the log
When the program runs on autostart, int dumps log output to the nohup.out file in `PycharmProjects/2017SteamworksVision/`.  You can view the file by entering the following in the terminal
```
cd PycharmProjects/2017SteamworksVision/
sudo nano nohup.out
```






