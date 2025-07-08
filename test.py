from RaspberryPiADS1299 import ADS1299_API
from RaspberryPiADS1299.ADS1299_API import DefaultCallback
from time import sleep
from time import time, sleep

# Custom callback to write EEG data to file
def EEGFileCallback(data):
    """
    Custom callback that writes EEG stream data to eeg_stream.txt file.
    Each data sample (numpy array) is written as a new line in readable format.
    """
    with open("eeg_stream.txt", "a") as f:
        # Convert numpy array to space-separated string
        data_string = " ".join(f"{value:.6f}" for value in data)
        f.write(data_string + "\n")

# init ads api
ads = ADS1299_API()

# init device
ads.openDevice()
# attach custom callback to write data to file
ads.registerClient(EEGFileCallback)
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
