from bluelake import Trap

trap1 = Trap("1", "XY")
trap2 = Trap("2", "XY")

trap1.clear()
trap2.clear()

# or optionally:
trap1.clear(delay_ms=100)  # how long the shutter is closed
