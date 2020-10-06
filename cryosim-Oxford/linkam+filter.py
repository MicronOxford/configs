from microscope.devices import device
# Import device modules/classes here.
from microscope.stages import linkam
from microscope.filterwheels import thorlabs
from microscope.cameras import atmcd
from microscope.cameras import ximea
from microscope.lasers import deepstar




host = "192.168.0.10"

DEVICES = [
        device(linkam.LinkamCMS, host, 8001,uid=''),
        device(thorlabs.ThorlabsFW102C, host, 7780, # ND wheel
               {'com':'com8', 'timeout':.2}),
        #device(atmcd.AndorAtmcd, host,7777, uid='7197'), #AndorCamera
        device(ximea.XimeaCamera, host, 7778), #ximea camera for interferometer
        device(deepstar.DeepstarLaser, host, 7771, # 488
               {'com' : 'com9'}),
        device(deepstar.DeepstarLaser, host, 7770, # 405
               {'com' : 'com5'}),
  

 
        
]
