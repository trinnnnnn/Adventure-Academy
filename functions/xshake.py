import math
import time

def x_shake(width, original_width, shake_amplitude, shake_speed, shake_duration, shake_start_time):
    if shake_start_time is None:
        shake_start_time = time.time()

    elapsed_time = time.time() - shake_start_time
    if elapsed_time <= shake_duration:
        decay_factor = (shake_duration - elapsed_time) / shake_duration

        shake_offset = shake_amplitude * decay_factor * math.sin(elapsed_time * shake_speed)
        width = original_width + shake_offset
    else:
        width = original_width
        shake_start_time = None

    return width, shake_start_time, elapsed_time
