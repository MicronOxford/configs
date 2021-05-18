#!/usr/bin/env python

import microscope
from microscope.device_server import device

from microscope.simulators import (
    SimulatedCamera,
    SimulatedFilterWheel,
    SimulatedLightSource,
    SimulatedStage,
)
from microscope.testsuite.devices import DummyDSP, DummySLM


def make_xy_stage(**kwargs):
    del kwargs
    stage = SimulatedStage(
        limits={
            "X": microscope.AxisLimits(0, 25000),
            "Y": microscope.AxisLimits(0, 12000),
        }
    )
    return {"xy-stage": stage}


def make_outer_z_stage(**kwargs):
    del kwargs
    stage = SimulatedStage(
        limits={"Z": microscope.AxisLimits(0, 25000)}
    )
    return {"outer-z-stage": stage}


DEVICES = [
    device(SimulatedCamera, "127.0.0.1", 8000,),
    device(SimulatedCamera, "127.0.0.1", 8001),
    device(SimulatedLightSource, "127.0.0.1", 8002),
    device(SimulatedLightSource, "127.0.0.1", 8003),
    device(SimulatedFilterWheel, "127.0.0.1", 8004,
           {"positions": 6}),
    device(SimulatedFilterWheel, "127.0.0.1", 8005,
           {"positions": 12}),
    device(DummyDSP, "127.0.0.1", 8006),
    device(DummySLM, "127.0.0.1", 8007),
    device(make_xy_stage, "127.0.0.1", 8008),
    device(make_outer_z_stage, "127.0.0.1", 8009),
]
