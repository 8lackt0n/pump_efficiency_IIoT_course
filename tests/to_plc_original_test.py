import struct
import pymodbus
from pymodbus.client import ModbusTcpClient

print("started!")

def encode_32_int(value):
    byte_value = struct.pack('>I', int(value))
    return struct.unpack('>HH', byte_value)

def encode_32_float(value):
    byte_value = struct.pack('>f', float(value))
    return struct.unpack('>HH', byte_value)

def decode_32_int(registers):
    handle = [struct.pack('>H', p) for p in registers]
    binary_string = b''.join(handle)
    return struct.unpack('!I', binary_string)[0]

def decode_32_float(registers):
    handle = [struct.pack('>H', p) for p in registers]
    binary_string = b''.join(handle)
    return struct.unpack('!f', binary_string)[0]

def encode_float_or_int(value, i):
    if i == 0:
        val = encode_32_int(value)
        return val
    else:
        val = encode_32_float(value)
        return val
    

def decode_float_or_int(reg, i):
    if i == 0:
        val = decode_32_int(reg)
        return val
    else:
        val = decode_32_float(reg)
        return val


plc_ip = '192.168.2.100'
plc_port = 502

client = ModbusTcpClient(plc_ip, port=plc_port)
client.connect()

print("Connected!")

#print("External control")
#rr = client.read_input_registers(address=0, count=1).registers
#print(decode_32_int(rr))

input_reg =      [1,3,5,7,9,11]
input_reg_type = [0,1,1,0,1,1] #0 = int, 1 = float

hold_reg =      [0,1,3]
hold_reg_num =  [1,2,2]
hold_reg_type = [0,0,0]

for i in range(len(input_reg)):
    rr = client.read_input_registers(address=input_reg[i], count=2).registers
    print(decode_float_or_int(rr,input_reg_type[i]))


client.write_register(0,1)


print("Write to Pump 1")
val = encode_32_int(700)
client.write_registers(address=1, values=val)

print("Write to Pump 2")
val = encode_32_int(700)
client.write_registers(address=3, values=val)

print("Holding")
for i in range(len(hold_reg)):
    rr = client.ead_holding_registers(address=hold_reg[i], count=2).registers
    print(decode_float_or_int(rr,hold_reg_type[i]))

print("Input again")

for i in range(len(input_reg)):
    rr = client.read_input_registers(address=input_reg[i], count=2).registers
    print(decode_float_or_int(rr,input_reg_type[i]))

client.close()

