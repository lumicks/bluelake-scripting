"""Automated bead catching of 1 bead"""
from bluelake import stage, fluidics, pause, trap1, timeline

match_score = timeline["Tracking Match Score"]["Bead 1"]

trap1.clear()  # to get rid of any existing bead
stage.move_to("beads")  # must match the label in the UI
fluidics.open(1, 2, 3, 6)  # list of valves to open matching the UI

match_threshold = 80  # % minimal match score
while match_score.latest_value < match_threshold:
    # We only want to clear the trap if there's a bead there, so > 0% match
    if 0 < match_score.latest_value < match_threshold:
        print("Rejected bead with match score:", match_score.latest_value)
        trap1.clear()  # bad bead, BAD bead
    pause(0.5)  # seconds

stage.move_to("buffer")
fluidics.close(1, 2, 3, 6)
