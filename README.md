# Raspberry Pi ADS1299 Driver

<p align="center">
  <img alt="banner" src="/images/banner.jpg/" width="600">
</p>
<p align="center" href="">
  A High Level Driver for ADS1299 Control with Raspberry Pi
</p>

## Hardware Configuration

The Raspberry Pi 3 is used as a reference

|Signal  |  RPi Pin  |  ADS Pin|
|--------|:---------:|----------:|
|MOSI    |     19    |    DIN|
|MISO    |     21    |    DOUT|
|SCLK    |     23    |    SCLK|
|CS      |     24    |    CS|
|START   |     15    |    START|
|RESET   |     16    |    nRESET|
|PWRDN   |     18    |    nPWRDN|
|DRDY    |     22    |    DRDY|

### Hardware Setup for EEG

Connect sensing electrode to P (+) and ref to SRB1. With default config, the API doesn't enable the bias, that should help if you want to test with only a few electrodes.

## How to use it

It is easy as :

```python
from RaspberryPiADS1299 import ADS1299_API
from time import time, sleep

# init ads api
ads = ADS1299_API()

# init device
ads.openDevice()
# attach default callback
ads.registerClient(DefaultCallback)
# configure ads
ads.configure(sampling_rate=1000)

print("ADS1299 API test stream starting")

# begin test streaming
ads.startTestStream()

# begin EEG streaming
# ads.startEegStream()

# wait
sleep(10)

print("ADS1299 API test stream stopping")

# stop device
ads.stopStream()
# clean up
ads.closeDevice()

sleep(1)
print("Test Over")

```
# Installation Instructions for RaspberryPiADS1299 Library

These steps will guide you through installing the RaspberryPiADS1299 library from source on your Raspberry Pi. This includes setting up a Python virtual environment to avoid system-level package conflicts.

---

## 1. Prerequisites

Ensure your system is up to date and required tools are installed:

```bash
sudo apt-get update
sudo apt-get install python3-venv python3-pip git
```

---

## 2. Clone the Repository

Clone the library from GitHub:

```bash
git clone https://github.com/Ryansolar14/RaspberryPiADS1299-lib.git
cd RaspberryPiADS1299
```

---

## 3. Create and Activate a Python Virtual Environment

Create a virtual environment (recommended):

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 4. Install the Library

Install the library from source:

```bash
pip install .
```

---

## 5. Install Additional Dependencies

Install any other dependencies that your project or scripts require (e.g., numpy, RPi.GPIO):

```bash
pip install numpy RPi.GPIO
```

---

## 6. Verify Installation

You can verify the installation by running a sample script (see the README or your own test script):

```bash
python your_script.py
```

---

## 7. Deactivate the Virtual Environment (when done)

When you are finished, deactivate the virtual environment:

```bash
deactivate
```

---

## Notes

- **Hardware:** Make sure your ADS1299 hardware is properly connected to your Raspberry Pi as described in the library documentation.
- **Python Version:** This library requires Python 3. If you see errors about print statements, edit the source to use Python 3 print syntax (i.e., `print("text")`).
- **Permissions:** You may need to adjust SPI permissions:  
  ```bash
  sudo chmod 666 /dev/spidev0.0
  sudo reboot
  ```

---

## Credits

### Author
Fred Simard

### Maintainer
AJ Keller (@aj-ptw)

### Modified By:
Ryan Busch (@ryansolar14)
