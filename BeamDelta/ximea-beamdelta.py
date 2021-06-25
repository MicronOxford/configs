#!/usr/bin/env python

from microscope.devices import device
import microscope.cameras.ximea as ximea
DEVICES = [
    device(ximea.XimeaCamera, '127.0.0.1', 8000, conf={'serial_number': '00982350'})
           ,
    device(ximea.XimeaCamera, '127.0.0.1', 8001, conf={'serial_number': '38880050'}),
]
