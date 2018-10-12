"""FRAP scan sequence -- scan presets are set from the UI, this script just executes them

Note that the presets contain the scan volume and timings, but not the
laser power -- it's set separately from the script.

Instructions:

1. Set the confocal volume and timings for the initial scan and save it as
   a preset called "reference".
2. Set a new confocal volume and timings and save as "bleach".
3. Save a final preset called "image" to observe the sample after bleaching.
4. Set the laser power for the 3 stages in script below.
5. Run the script.
"""
import bluelake
from bluelake import confocal, excitation_lasers, timeline, pause


def wait_for_scan():
    """Wait for the last confocal scan to finish"""
    pause(1)
    while confocal.is_scanning:
        pause(1)


def increment_frap_count():
    """Add or increment a FRAP counter for the timeline markers"""
    if not hasattr(bluelake, "frap_count"):
        bluelake.frap_count = 0
    bluelake.frap_count += 1


increment_frap_count()
timeline.mark_begin(f"FRAP {bluelake.frap_count}")

# Scan 1: Before using this script you must save a scan preset and name it
#         "reference" (or anything else that matches the `start_scan()` below).
excitation_lasers.blue = 15  # % power
# and/or: `excitation_lasers.red = 20`  # % power
confocal.start_scan("reference")
wait_for_scan()

# Scan 2: As above, this starts a scan preset called "bleach". You must save
#         this preset in the UI before starting the script.
excitation_lasers.blue = 90  # % power
confocal.start_scan("bleach")
wait_for_scan()

# Scan 3: The previous two were single-frame scans, but this one is usually
#         multi-frame (again, set this in the UI and save it). It can also
#         be useful to increase the "Image time" in the UI. Effectively,
#         this adds a pause between frames in order to avoid bleaching if
#         the recovery is slow.
excitation_lasers.blue = 15  # % power
confocal.start_scan("image")
wait_for_scan()

timeline.mark_end()
