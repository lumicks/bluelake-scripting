"""Force clamp on trap 1 XY"""
from bluelake import force_clamp_start, force_clamp_stop, stage, fluidics, pause, trap1, timeline

# Select which force channel to clamp on
force_1x = timeline["Force HF"]["Force 1x"]
# Start clamping with the specified trap
force_clamp_start("Trap 1",force_1x.name, 5)
pause(1)
force_clamp_stop()