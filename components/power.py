from bluelake import power

# Reading values
print("Trapping laser", power.trapping_laser)  # get power in %
print("Overall {:.2f} %".format(power.overall_trapping_power))
print(power.trap1_split)
print(power.qtrap_split)
print(power.bright_field_led)

# Setting values
power.bright_field_led = 7  # value in %
