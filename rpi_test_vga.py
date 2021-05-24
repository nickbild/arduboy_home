import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)

a0_7 = 26
a1_8 = 32
a2_9 = 36
a3_10 = 38
a4_11 = 40
a5_12 = 3
a6_13 = 5
a14 = 7

r1 = 11

high_memory_latch = 8
interrupt = 19


GPIO.setup(a0_7, GPIO.OUT)
GPIO.setup(a1_8, GPIO.OUT)
GPIO.setup(a2_9, GPIO.OUT)
GPIO.setup(a3_10, GPIO.OUT)
GPIO.setup(a4_11, GPIO.OUT)
GPIO.setup(a5_12, GPIO.OUT)
GPIO.setup(a6_13, GPIO.OUT)
GPIO.setup(a14, GPIO.OUT)

GPIO.setup(r1, GPIO.OUT)

GPIO.setup(interrupt, GPIO.OUT)
GPIO.setup(high_memory_latch, GPIO.OUT)


GPIO.output(interrupt, 0)
GPIO.output(high_memory_latch, 0)


# Draw box representing Arduboy screen area.
for x in range(36, 165):
    for y in range(43, 108):
        i = (y * 200) + x

        v = '{0:015b}'.format(i)

        GPIO.output(a0_7, int(v[7]))
        GPIO.output(a1_8, int(v[6]))
        GPIO.output(a2_9, int(v[5]))
        GPIO.output(a3_10, int(v[4]))
        GPIO.output(a4_11, int(v[3]))
        GPIO.output(a5_12, int(v[2]))
        GPIO.output(a6_13, int(v[1]))
        GPIO.output(a14, int(v[0]))

        GPIO.output(high_memory_latch, 1)
        GPIO.output(high_memory_latch, 0)

        GPIO.output(a0_7, int(v[14]))
        GPIO.output(a1_8, int(v[13]))
        GPIO.output(a2_9, int(v[12]))
        GPIO.output(a3_10, int(v[11]))
        GPIO.output(a4_11, int(v[10]))
        GPIO.output(a5_12, int(v[9]))
        GPIO.output(a6_13, int(v[8]))

        GPIO.output(r1, 1)

        GPIO.output(interrupt, 1)
        GPIO.output(interrupt, 0)


# Transform Arduboy x,y coordinates to VGA x,y coordinates.
def drawPoint(x, y):
    x += 36
    y += 43
    i = (y * 200) + x

    v = '{0:015b}'.format(i)

    GPIO.output(a0_7, int(v[7]))
    GPIO.output(a1_8, int(v[6]))
    GPIO.output(a2_9, int(v[5]))
    GPIO.output(a3_10, int(v[4]))
    GPIO.output(a4_11, int(v[3]))
    GPIO.output(a5_12, int(v[2]))
    GPIO.output(a6_13, int(v[1]))
    GPIO.output(a14, int(v[0]))

    GPIO.output(high_memory_latch, 1)
    GPIO.output(high_memory_latch, 0)

    GPIO.output(a0_7, int(v[14]))
    GPIO.output(a1_8, int(v[13]))
    GPIO.output(a2_9, int(v[12]))
    GPIO.output(a3_10, int(v[11]))
    GPIO.output(a4_11, int(v[10]))
    GPIO.output(a5_12, int(v[9]))
    GPIO.output(a6_13, int(v[8]))

    GPIO.output(r1, 0)

    GPIO.output(interrupt, 1)
    GPIO.output(interrupt, 0)

    return


drawPoint(0, 0)
