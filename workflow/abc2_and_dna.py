"""Catch beads and then fish for DNA"""
from bluelake import Trap, stage, fluidics, pause, timeline, reset_force

trap1 = Trap("1", "XY")
trap2 = Trap("2", "XY")
match_score1 = timeline["Tracking Match Score"]["Bead 1"]
match_score2 = timeline["Tracking Match Score"]["Bead 2"]

def catch_2_beads():
    "Just like `abc2.py`"
    target_traps = [trap1, trap2]
    match_scores = [match_score1, match_score2]

    for trap in target_traps:
        trap.clear()  # to get rid of any existing beads

    stage.move_to("beads")  # must match the label in the UI
    fluidics.open(1, 2, 3, 6)  # list of valves to open matching the UI

    match_threshold = 80  # % minimal match score
    while any(m.latest_value < match_threshold for m in match_scores):
        if any(0 < m.latest_value < match_threshold for m in match_scores):
            for trap in target_traps:
                trap.clear()  # bad beads
            pause(1)

    stage.move_to("buffer")
    fluidics.close(1, 2, 3, 6)


def goto_distance(target):
    """Move trap 1 until it reaches the `target` distance from trap 2"""
    distance = timeline["Distance"]["Distance 1"]
    dx = distance.latest_value - target

    while abs(dx) > 0.2:  # um
        if dx <= 0:
            trap1.move_by(dx=+0.1)
        else:
            trap1.move_by(dx=-0.1)
        dx = distance.latest_value - target


def fish_for_dna(min_distance_um, max_distance_um, force_threshold_pN):
    """Oscillate between min and max distance while the force is under the threshold value"""
    stage.move_to("DNA")
    goto_distance(min_distance_um)
    fluidics.open(1, 2, 3, 6)
    pause(1)

    reset_force()
    goto_distance(max_distance_um)
    while trap2.current_force < force_threshold_pN:
        goto_distance(min_distance_um)
        reset_force()
        goto_distance(max_distance_um)

    fluidics.close(1, 2, 3, 6)
    stage.move_to("buffer")
    goto_distance(min_distance_um)
    reset_force()


catch_2_beads()
fish_for_dna(min_distance_um=10, max_distance_um=15, force_threshold_pN=10)
