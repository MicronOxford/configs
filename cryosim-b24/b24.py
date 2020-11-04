"""Config file for devicebase.

Import device classes, then define entries in DEVICES as:
    devices(CLASS, HOST, PORT, other_args)
"""
## Function to create record for each device.
from microscope.devices import device
## Import device modules/classes here.
from microscope.lasers.deepstar import DeepstarLaser
from microscope.lasers.sapphire import SapphireLaser

from microscope.lasers.cobolt import CoboltLaser
from microscope.filterwheels.thorlabs import ThorlabsFW102C

DEVICES = [
        device(DeepstarLaser, 'dsp.b24', 8001, conf=dict(com='com7', baud=9600, timeout=1)), #405nm
        device(DeepstarLaser, 'dsp.b24', 8002, conf=dict(com='com10', baud=9600, timeout=1)), #488nm
        device(CoboltLaser, 'dsp.b24', 8003, conf=dict(com='com1', baud=115200, timeout=1)), #561nm
        device(DeepstarLaser, 'dsp.b24', 8004, conf=dict(com='com8', baud=9600, timeout=1)), #647nm
		device(ThorlabsFW102C, 'dsp.b24', 8005, conf=dict(com='com5', baud=115200, timeout=1)), #transmitted
		device(ThorlabsFW102C, 'dsp.b24', 8006, conf=dict(com='com3', baud=115200, timeout=1)), #reflected
]
