import plasma
from plasma import plasma_stick
from random import uniform, randint
from array import array
import time

# This code creates an orange flickering effect on a LED strip
# connected to a Pimoroni Plasma Stick microcontroller.
#
# It first performs a fade-in animation where all LEDs gradually
# increase in brightness, then enters an infinite loop where it
# randomly selects LEDs and slightly varies their hue to create a
# flame-like flickering effect.
#
# The colours are kept within an orange spectrum using HSV colour values.

# Number of LEDs in the strip
NUM_LEDS = 50
# Base hue value (in HSV colour space, normalized to 0-1 range)
HUE = 25 / 360
# Amount of hue variation allowed (in HSV colour space, normalized to 0-1 range)
HUE_SPREAD = 30 / 360

# Initialize the LED strip
led_strip = plasma.WS2812(
    NUM_LEDS, 0, 0, plasma_stick.DAT, color_order=plasma.COLOR_ORDER_RGB
)
led_strip.start()

# Calculate the minimum hue value for the flicker effect
min_hue = HUE - (HUE_SPREAD / 2)

# Initial fade-in animation
# Gradually increases brightness of all LEDs from 0% to 100%
for v in range(100):
    for i in range(NUM_LEDS):
        led_strip.set_hsv(i, HUE, 1, v / 100)
    time.sleep(1 / 50)  # 50 FPS animation

# Main loop - creates a flickering effect
# Randomly selects LEDs and varies their hue slightly for a fire-like effect
while True:
    # Parameters:
    # - Random LED position
    # - Random hue between min_hue and 30/360
    # - Full saturation (1)
    # - Full brightness (1)
    led_strip.set_hsv(randint(0, NUM_LEDS), uniform(min_hue, 30 / 360), 1, 1)
    time.sleep(1 / 10)  # Small delay between updates
