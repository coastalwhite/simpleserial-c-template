import numpy as np
import chipwhisperer as cw

# Setup our capture and target boards.
########################################
scope = cw.scope()
scope.default_setup()
target = cw.target(scope, cw.targets.SimpleSerial2, flush_on_err=False)
########################################

# Reprogram the target
########################################
import os
from chipwhisperer.capture.api.programmers import STM32FProgrammer

# Initiate a new STM32F Program
# STM32 being the ARM microcontroller that we are using
# https://en.wikipedia.org/wiki/STM32#STM32_F3
program = STM32FProgrammer

# Get the path to the current folder
# Adjust accordingly
aes_firmware_dir = os.path.dirname(os.path.realpath(__file__))
aes_hex_path = os.path.join(aes_firmware_dir, r"simpleserial-target-CWLITEARM.hex")

# Apply the program to the actual target
# This allows us to run the hex code on the microcontroller
cw.program_target(scope, program, aes_hex_path)
########################################

# Capture a trace of our binary
########################################
# Define some dummy data
data = bytearray([0x42] * 16)

# Arm the capture board
scope.arm()

# Flush the UART buffer
target.flush()

# Send a new command to trigger our code.
# Here we use scmd = 128
target.send_cmd('p', 0x80, data)

# Do our wave trace capture
# and fetch that wave trace
ret = scope.capture()
trace = scope.get_last_trace()
########################################

# Return the data.
########################################
# Print the returned data
returned_data = target.read_cmd('r')
print(returned_data)
ack = target.read_cmd('e')

import matplotlib.pyplot as plt

# Plot the trace
plt.plot(trace)
plt.show()
########################################