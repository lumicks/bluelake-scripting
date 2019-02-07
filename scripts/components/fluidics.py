from bluelake import fluidics, pause

# Open specific valves
fluidics.open(1, 2, 3, 6)
# or
fluidics.open(1, 2)

# And close valves
fluidics.close(1, 2)

# Read the current pressure value
print(fluidics.pressure())

# Pressure control does the same thing as the UI (not really ideal)
fluidics.increase_pressure()
fluidics.decrease_pressure()

while fluidics.pressure < 1:  # bar
    fluidics.increase_pressure()
    pause(1)  # seconds to pause -- important because pressure changes are slow
