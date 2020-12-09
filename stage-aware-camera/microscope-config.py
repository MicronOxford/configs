from microscope.device_server import device
from microscope.testsuite.simulated_system import simulated_system_from_image

DEVICES = [
    device(simulated_system_from_image, 'localhost', 8000,
           conf={'filepath': 'mosaicimage.tif'}),
]
