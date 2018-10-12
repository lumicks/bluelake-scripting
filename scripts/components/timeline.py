from bluelake import timeline
import time

# Grab a reference to any channel. The first [] is the group name
# and the second [] is the channel name. These match exactly the
# channel tree visible in the graphical UI of Bluelake.
force_channel = timeline["Force HF"]["Force 1x"]
match_score = timeline["Tracking Match Score"]["Bead 1"]

# The latest ("current") value of the data on that channel
force_value = force_channel.latest_value

# The current time, according to the timeline
t0 = timeline.current_time

# Do something
time.sleep(0.01) # seconds

t1 = timeline.current_time

# Fetch the data for that timespan
force_data = force_channel[t0:t1].data
timestamps = force_channel[t0:t1].timestamps
print(force_data)

# Add a marker to the timeline GUI
timeline.mark_begin()
time.sleep(1) # seconds
timeline.mark_end()
