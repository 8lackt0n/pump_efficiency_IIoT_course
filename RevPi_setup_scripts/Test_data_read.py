
import Modbus_Functions as mb
import time

#%%
print(mb.read_data(0, "input"))
print(mb.read_data(0, "holding"))

print(mb.read_data(1, "input"))
print(mb.read_data(7, "input"))


mb.manual_mode()
time.sleep(2)

mb.write_data(1, 200)
print(mb.read_data(1, "holding"))
mb.write_data(3, 200)
print(mb.read_data(3, "holding"))

time.sleep(2)
print(mb.read_data(0, "input"))
print(mb.read_data(0, "holding"))

print(mb.read_data(1, "input"))
print(mb.read_data(7, "input"))

time.sleep(2)
print(mb.read_data(0, "holding"))

mb.auto_mode()

time.sleep(2)
print(mb.read_data(0, "input"))
print(mb.read_data(0, "holding"))

print(mb.read_data(1, "input"))
print(mb.read_data(7, "input"))
