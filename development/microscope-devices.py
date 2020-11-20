#!/usr/bin/env python

import microscope
import microscope.testsuite.devices as testdevices
from microscope.device_server import device


def make_xy_stage(**kwargs):
    del kwargs
    stage = testdevices.TestStage(
        limits={
            "X": microscope.AxisLimits(0, 25000),
            "Y": microscope.AxisLimits(0, 12000),
        }
    )
    return {"xy-stage": stage}


def make_outer_z_stage(**kwargs):
    del kwargs
    stage = testdevices.TestStage(
        limits={"Z": microscope.AxisLimits(0, 25000)}
    )
    return {"outer-z-stage": stage}


DEVICES = [
    device(testdevices.TestCamera, "127.0.0.1", 8000,),
    device(testdevices.TestCamera, "127.0.0.1", 8001),
    device(testdevices.TestLightSource, "127.0.0.1", 8002),
    device(testdevices.TestLightSource, "127.0.0.1", 8003),
    device(testdevices.TestFilterWheel, "127.0.0.1", 8004, {"positions": 6}),
    device(testdevices.TestFilterWheel, "127.0.0.1", 8005, {"positions": 12}),
    device(testdevices.DummyDSP, "127.0.0.1", 8006),
    device(testdevices.DummySLM, "127.0.0.1", 8007),
    device(make_xy_stage, "127.0.0.1", 8008),
    device(make_outer_z_stage, "127.0.0.1", 8009),
]
