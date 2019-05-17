"""Force clamp on trap 1 XY"""
from bluelake import force_clamp_start, force_clamp_stop, stage, fluidics, pause, trap1, timeline

force_clamp_start("Trap 1",: "Force 1", 5)
pause(1)
force_clamp_stop()
