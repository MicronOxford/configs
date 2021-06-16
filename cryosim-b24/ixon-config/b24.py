"""Config file for devicebase.

Import device classes, then define entries in DEVICES as:
    devices(CLASS, HOST, PORT, other_args)
"""
## Function to create record for each device.
from microscope.devices import device
## Import device modules/classes here.
from microscope.lasers.deepstar import DeepstarLaser
from microscope.lasers.cobolt import CoboltLaser
DEVICES = [
        device(DeepstarLaser, 'dsp.b24', 8001, com='com6', baud=9600, timeout=1), #405nm
        device(DeepstarLaser, 'dsp.b24', 8002, com='com3', baud=9600, timeout=1), #488nm
        device(CoboltLaser, 'dsp.b24', 8003, com='com4', baud=115200, timeout=1), #561nm
        device(DeepstarLaser, 'dsp.b24', 8004, com='com5', baud=9600, timeout=1), #647nm
]
