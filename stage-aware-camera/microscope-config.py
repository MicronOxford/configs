from microscope.device_server import device
from microscope.testsuite.simulated_setup import simulated_setup_from_image

DEVICES = [
    device(simulated_setup_from_image, 'localhost', 8000,
           conf={'filepath': 'mosaicimage.tif'}),
]
