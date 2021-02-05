This directory contains files to configure microsocpe/cockpit as a
3-camera 3 colour fluorescence system to best demonstrait the zaber
large mosaic image previously collected.

There is also a slightly altered
microscope/simulation/stage_aware_camera.py

If you copy this into the relevant directory, then run the microscpe
device server with

device-server microscpe-stageawarecam.py

finally start cockpit with

cockpit --depot-file simulated-system.depot

This starts a simulation with 3 cameras and 3 filter wheels, allowing
imaging in the 3 colours.

