from bluelake import stage

stage.move_to("beads")  # the waypoint name must match the name in the UI
stage.move_to("DNA", speed=10)  # optional speed in 0-100%
