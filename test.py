#!/usr/bin/env python3
"""
Test script for RaspberryPiADS1299-lib

This script demonstrates how to collect Channel 1 data from an ADS1299 EEG amplifier
for 1 second at 1000 Hz sampling rate and stream the output to the terminal.

Features:
- Collects only Channel 1 data (configures ADS1299 for single channel)
- Samples at 1000 Hz for exactly 1 second (~1000 samples)
- Prints each sample value as it's collected (streaming output)
- No disk writes - output goes directly to stdout
- Works with real ADS1299 hardware when available
- Falls back to realistic simulated data when hardware not present
- Self-contained and executable as: python3 test.py

Requirements:
- RaspberryPiADS1299-lib installed and importable
- numpy, spidev, lgpio (installed via pip3 install -r requirements.txt)
- For real hardware: ADS1299 connected to Raspberry Pi SPI interface

Author: Generated for RaspberryPiADS1299-lib demonstration
"""

from RaspberryPiADS1299.ADS1299_API import ADS1299_API
from time import time, sleep
import sys

# Global variable to track sample count
sample_count = 0
start_time = None

def channel1_callback(data_array):
    """
    Custom callback function that prints only Channel 1 data
    Args:
        data_array: numpy array containing data from all configured channels
    """
    global sample_count, start_time
    
    if start_time is None:
        start_time = time()
    
    # Print only the first channel (Channel 1) value
    print(data_array[0])
    
    sample_count += 1

def main():
    """
    Main function to set up ADS1299 and collect Channel 1 data
    """
    global sample_count, start_time
    
    print("RaspberryPiADS1299 Channel 1 Test - Collecting data for 1 second at 1000 Hz")
    print("Sample values will be printed one per line...")
    print("-" * 60)
    
    # Initialize the ADS1299 API
    ads = ADS1299_API()
    
    # Try to detect if this is likely real hardware vs development environment
    hardware_available = False
    
    try:
        # Test if SPI device exists
        import os
        if os.path.exists('/dev/spidev0.0'):
            hardware_available = True
    except:
        pass
    
    try:
        # Open device (will fail if hardware not available)
        ads.openDevice()
        
        # Register our custom callback for Channel 1 data
        ads.registerClient(channel1_callback)
        
        # Configure for 1 channel at 1000 Hz sampling rate
        ads.configure(nb_channels=1, sampling_rate=1000)
        
        print("Real ADS1299 hardware detected. Starting data collection...")
        
        # Start EEG streaming
        ads.startEegStream()
        
        # Reset timing variables
        start_time = None
        sample_count = 0
        
        # Collect data for 1 second
        # We'll check every 0.1 seconds if we've collected enough data
        while True:
            sleep(0.1)
            if start_time and (time() - start_time) >= 1.0:
                break
        
        print("-" * 60)
        print(f"Data collection complete. Collected {sample_count} samples in approximately 1 second.")
        
    except (FileNotFoundError, OSError, Exception) as e:
        # Handle case where hardware is not available - use manual stubbed mode
        if hardware_available:
            print(f"Hardware detected but failed to initialize: {e}")
            print("Please check connections and permissions.")
            sys.exit(1)
        
        print("Hardware not detected, using stubbed mode for demonstration...")
        print("(This simulates the ADS1299 data stream)")
        
        # Manual stubbed data generation
        import numpy as np
        
        print("Starting stubbed data collection...")
        
        # Reset timing variables
        start_time = None
        sample_count = 0
        
        # Generate data for exactly 1 second at 1000 Hz
        target_samples = 1000
        sample_interval = 1.0 / 1000.0  # 1ms per sample
        
        start_time = time()
        
        for i in range(target_samples):
            # Generate random data like the ADS1299 would (in microvolts)
            # Using a more realistic EEG-like signal range
            fake_data = np.array([np.random.normal(0, 50)])  # Mean=0, StdDev=50 microvolts
            
            # Call our callback
            channel1_callback(fake_data)
            
            # Sleep to maintain 1000 Hz timing
            # Account for processing time
            elapsed = time() - start_time
            expected_time = (i + 1) * sample_interval
            sleep_time = expected_time - elapsed
            if sleep_time > 0:
                sleep(sleep_time)
        
        print("-" * 60)
        print(f"Stubbed data collection complete. Generated {sample_count} samples in approximately 1 second.")
        
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
        sys.exit(1)
        
    finally:
        # Clean up
        try:
            if hasattr(ads, 'stream_active'):
                ads.stopStream()
            if hasattr(ads, 'closeDevice'):
                ads.closeDevice()
        except:
            pass  # Ignore cleanup errors
    
    print("Test completed successfully.")

if __name__ == "__main__":
    main()