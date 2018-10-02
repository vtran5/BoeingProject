#Electrical Kill
#Voltage for all legs to zero

import smbus
import time
import numpy as np

# Get I2C bus
bus = smbus.SMBus(1)

time.sleep(0.5)
data = [0x00, 0x00]
bus.write_i2c_block_data(0x56, 0x2F, data)
