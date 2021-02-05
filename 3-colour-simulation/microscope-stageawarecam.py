from microscope.device_server import device
from microscope.simulators.stage_aware_camera import simulated_setup_from_image
import microscope.testsuite.devices as testdevices

DEVICES = [
    device(simulated_setup_from_image, 'localhost', 8000,
           conf={'filepath': 'merged-zaber-rgb.tif'}),
    device(testdevices.DummyDSP, 'localhost', 8006),
        device(testdevices.TestLaser, '127.0.0.1', 8003),
]
