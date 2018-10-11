"""Fish for DNA"""
from bluelake import Trap, stage, fluidics

trap = Trap("1", "XY")

while trap.current_force < 15:  # [pN]
    trap.move_by(dx=-1.0)  # [um]
    trap.move_by(dx=+1.0)  # [um]

print("caught molecule")
stage.move_to("buffer")
fluidics.stop_flow()
