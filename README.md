# kw41-thread-demo
This project provide the demo codes and configuration for KW41 Thread.

## Install hsdk library
        - copy hsdk_ubuntu/build/*.so to /user/lib/
        - change all name to *.so.1

## Install other libraries
	- apt-get install libudev-dev libpcap-dev
	- apt-get install python-twisted or easy_install twisted

## Configure
        - ./make_tun.sh
	- ./Thread_KW_Tun /dev/ttyACM0 fslthr0 0 25 115200 &

## Run this codes
        - ./run_thread.sh on or ./run_thread.sh off
	- python /root/rgb_led.py fd01::3ead:7d3e:16eb:b4d1:1d7 on or 
	- python /root/rgb_led.py fd01::3ead:7d3e:16eb:b4d1:1d7 off

