"""Fish for DNA"""
from bluelake import trap1, stage, fluidics

while trap1.current_force < 15:  # [pN]
    trap1.move_by(dx=-1.0)  # [um]
    trap1.move_by(dx=+1.0)  # [um]

print("caught molecule")
stage.move_to("buffer")
fluidics.stop_flow()
