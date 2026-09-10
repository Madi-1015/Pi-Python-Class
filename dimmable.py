from colorzero import Color
from gpiozero import RotaryEncoder, RGBLED
from time import sleep
rotor = RotaryEncoder(16, 20, wrap=True, max_steps=180)

led = RGBLED(red=22, green=23, blue=24)

while True:
    hue = (rotor.steps/180)**2
    led.color = Color(h=hue, s=1, v=1)