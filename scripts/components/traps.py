from bluelake import trap1, trap2, trap12xy, trap12z, nanostage, pause, reset_force

# absolute movement
trap1.move_to(x=4, y=1)  # [um] matches the position in the UI
trap1.move_to(x=10)  # [um] no change on Y
trap1.move_to(x=10, speed=10)  # [um/s] defaults to 1 um/s if not specified

# relative movement
trap1.move_by(dx=1, dy=2)  # [um] note `dx` instead of `x` above
trap1.move_by(dx=1, dy=2, speed=0)  # [um/s] 0 means maximum speed

trap12z.move_to(z=-2)  # [um] # only Z for trap 1+2 Z

nanostage.move_to(x=1, y=20, z=15, speed=3)  # [um] full XYZ movement


def pingpong(distance_delta_um, period_ms, speed):
    """This will pingpong infinitely and must be stopped using the `Stop` button in the UI"""
    while True:
        trap1.move_by(dx=+distance_delta_um, speed=speed)
        pause(period_ms / 1000 / 2)  # pause time is given in seconds, convert from milliseconds
        print("ping")
        # reset_force() # optionally reset the force
        trap1.move_by(dx=-distance_delta_um, speed=speed)
        pause(period_ms / 1000 / 2)
        print("pong")
        # reset_force() # optionally reset the force


pingpong(distance_delta_um=0.01, period_ms=50, speed=10)
