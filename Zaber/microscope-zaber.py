#!/usr/bin/env python

from microscope.devices import device
import microscope.cameras.ximea as ximea
import microscope.controllers.zaber as zaber
import microscope.controllers.coolled as coolled

from microscope.simulators import (
    SimulatedCamera,
    SimulatedFilterWheel,
    SimulatedLightSource,
)
from microscope.testsuite.devices import DummyDSP
from microscope.devices import AxisLimits


DEVICES = [
    device(ximea.XimeaCamera, '127.0.0.1', 8000),
    device(DummyDSP, '127.0.0.1', 8006),
    device(SimulatedCamera, '127.0.0.1', 8001),
    device(SimulatedFilterWheel, '127.0.0.1', 8004,
          conf={'positions': 5}),
    device(SimulatedLightSource, '127.0.0.1',8003),
    device(zaber.ZaberDaisyChain, '127.0.0.1',8010,
           conf={'port':'/dev/tty.usbserial-AK06IX8F',
                 'address2type': {
                     2: zaber.ZaberDeviceType.STAGE,
                     5: zaber.ZaberDeviceType.STAGE,
                     4: zaber.ZaberDeviceType.FILTER_WHEEL,
            #         3: zaber.ZaberDeviceType.LED,
                 }}),
    device(coolled.CoolLED, '127.0.0.1',8011,
           conf={'port': '/dev/tty.usbmodem00003'})
    # 1: joystick, 2: XY 3: LEDs 4: filter wheel 5: Focus,
]
