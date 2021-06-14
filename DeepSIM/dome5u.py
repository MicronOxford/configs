# Function to create record for each device.
from microscope.devices import device
# Import device modules/classes here.
from microscope.cameras import atmcd
#from microscope.cameras import andorsdk3
#from microscope.lasers import cobolt
from microscope.lasers import deepstar
#from microscope.lasers import toptica
from microscope.lasers import sapphire

host = "192.168.1.2"

DEVICES = [
    device(atmcd.AndorAtmcd, host, 7777,
                             {'index':'0'},'9146'),#, 'transform':(True,False,False)},'9146'),
    #device(atmcd.AndorAtmcd, host, 7778,
    #           {'uid':'9145'}),
    device(atmcd.AndorAtmcd, host, 7778,
               {'index':'1'},'9145'),
    #device(andorsdk3.AndorSDK3, host, 7778,
    #           {'uid':'9145'}),
    device(deepstar.DeepstarLaser, host, 7771,
               {'com':'com12'}), # 488
    #device(deepstar.DeepstarLaser, host, 7772,
    #           {'com':'com11'}), # 647
    device(sapphire.SapphireLaser, host, 7773,
               {'com':'com2'}), #561
    #device(cobolt.CoboltLaser, host, 7773,
        #       {'com':'com2'}), # 561
    #device(toptica.TopticaiBeam, host, 7772,
    #           {'port':'com6'}), # 647
]
