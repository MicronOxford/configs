from microscope.devices import device
from microscope.mirror.alpao import AlpaoDeformableMirror
from microscope.cameras.ximea import XimeaCamera
from microAO.aoDev import AdaptiveOpticsDevice

mirror_args = [AlpaoDeformableMirror, '192.168.1.20', 8007]
wavefront_args = [XimeaCamera, '192.168.1.20', 8008]
slm_arg = ['pyroSLM', '192.168.1.19', 8000]

DEVICES = [
  device(*mirror_args,
         {'serial_number': 'BIL103'}),
  device(*wavefront_args),
  device(AdaptiveOpticsDevice, '192.168.1.20', 8009,
         {'wavefront_uri': wavefront_args,
         'ao_element_uri': mirror_args,
          'slm_uri': slm_arg})
]
