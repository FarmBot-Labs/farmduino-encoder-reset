#!/usr/bin/env python

'''Farmware to reset encoder tracking on a v1.4 Farmduino.'''

from farmware_tools import device

device.set_pin_io_mode(1, 49)
device.write_pin(49, 0, 0)
device.write_pin(49, 1, 0)
device.set_pin_io_mode(2, 49)
