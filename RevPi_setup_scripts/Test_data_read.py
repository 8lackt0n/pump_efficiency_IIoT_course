
import Modbus_Functions as mb
import time

#%%
print(mb.read_data(1))
print(mb.read_data(7))

mb.manual_mode()

time.sleep(2)

mb.write_data(1, 200)
mb.write_data(3, 200)

time.sleep(2)

print(mb.read_data(1))
print(mb.read_data(7))

mb.auto_mode()

time.sleep(2)

print(mb.read_data(1))
print(mb.read_data(7))
