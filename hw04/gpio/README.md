To make the updated version of gpioThru.c work
you need to cd into /sys/class/gpio and make the call "echo # >> export" where #
is replaced with 97 and 98 (you have to make the call twice) then cd into each
directory (gpio97, gpio98) and call "cat direction" if the output from that call
is "in" you need to call "echo out >> direction" to set the gpio ports to outputs
for the leds
