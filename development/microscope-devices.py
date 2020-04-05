#!/usr/bin/env python

from microscope.devices import device
import microscope.testsuite.devices as testdevices

DEVICES = [
    device(testdevices.TestCamera, '127.0.0.1', 8000,),
    device(testdevices.TestCamera, '127.0.0.1', 8001),
    device(testdevices.TestLaser, '127.0.0.1', 8002),
    device(testdevices.TestLaser, '127.0.0.1', 8003),
    device(testdevices.TestFilterWheel, '127.0.0.1', 8004),
    device(testdevices.TestFilterWheel, '127.0.0.1', 8005),
    device(testdevices.DummyDSP, '127.0.0.1', 8006),
    device(testdevices.DummySLM, '127.0.0.1', 8007),
]
