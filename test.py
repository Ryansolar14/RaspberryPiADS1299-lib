from RaspberryPiADS1299 import ADS1299_API
from RaspberryPiADS1299 import DefaultCallback
from time import sleep
from time import time, sleep

# init ads api
ads = ADS1299_API()

# init device
ads.openDevice()
# attach default callback
ads.registerClient(DefaultCallback)
# configure ads
ads.configure(sampling_rate=1000)

print ("ADS1299 API EEG stream starting")

# begin test streaming
# ads.startTestStream()

# begin EEG streaming
ads.startEegStream()

# wait
sleep(10)

print ("ADS1299 API test stream stopping")

# stop device
ads.stopStream()
# clean up
ads.closeDevice()

sleep(1)
print ("Test Over")
