"""Automated bead catching -- 2 beads"""
from bluelake import stage, fluidics, pause, timeline, Trap

trap1 = Trap("1", "XY")
trap2 = Trap("2", "XY")
target_traps = [trap1, trap2]

match_score1 = timeline["Tracking Match Score"]["Bead 1"]
match_score2 = timeline["Tracking Match Score"]["Bead 2"]
match_scores = [match_score1, match_score2]

for trap in target_traps:
    trap.clear()  # to get rid of any existing beads

stage.move_to("beads")  # must match the label in the UI
fluidics.open(1, 2, 3, 6)  # list of valves to open matching the UI

# Note: `match_score1` does not map directly to `trap1`. `match_score1`,
# `match_score2` sort beads from left to right, up to down. In case we
# `match_score1.latest_value > 0` we can't be sure that if that bead is
# in `trap1` or `trap2`. So to catch 2 beads we need to make sure both
# are good or clear both traps even if just one is bad.

match_threshold = 80  # % minimal match score
while any(m.latest_value < match_threshold for m in match_scores):
    if any(0 < m.latest_value < match_threshold for m in match_scores):
        for trap in target_traps:
            trap.clear()  # bad beads
        pause(1)

stage.move_to("buffer")
fluidics.close(1, 2, 3, 6)
