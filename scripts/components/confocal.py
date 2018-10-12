from bluelake import confocal, excitation_lasers, pause

print(excitation_lasers.red)  # get current value in %
excitation_lasers.red = 40  # set value in %

confocal.start_scan()  # start the active configuration
confocal.start_scan("Preset name")  # start a specific preset

# wait for scan to finish (not required)
pause(1)
while confocal.is_scanning:
    pause(1)

# or abort scan
confocal.abort_scan()
