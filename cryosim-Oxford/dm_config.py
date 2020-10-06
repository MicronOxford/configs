# Function to create record for each device
from microscope.devices import device

#Import device modules/classes here

from microscope.mirror.alpao import AlpaoDeformableMirror
# Function to create record for each device.
from microscope.devices import device
#from microscope.testsuite.devices import TestDeformableMirror
from microscope.cameras.ximea import XimeaCamera
from microAO.aoDev import AdaptiveOpticsDevice


host = "192.168.0.11"

wavefront_args = (XimeaCamera,'192.168.0.10',7778)
mirror_args = (AlpaoDeformableMirror,host,7781)

DEVICES = [
        device(*mirror_args,conf={'serial_number':'BAX214'}),
        #device(*wavefront_args),
        device(AdaptiveOpticsDevice, host, 7780,
          conf={'ao_element_uri':mirror_args,
               'wavefront_uri':wavefront_args
          })
        #device(XimeaCamera, host,7776)
        ]



