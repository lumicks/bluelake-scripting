"""Smooth high-frequency trap oscillation

See docs at https://help.lumicks.com/bluelake-api/api.html#bluelake.Trap.start_oscillation
"""
from bluelake import trap1, pause

# Start a 10 Hz oscillation, with amplitude 1 um
trap1.start_oscillation(axis="x", frequency=10, amplitude=1)

# Let it run for 5 seconds, then stop
pause(5.0)
trap1.stop()
