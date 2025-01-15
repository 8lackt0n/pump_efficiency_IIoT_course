#%% Import packages
import struct
from pymodbus.client import ModbusTcpClient

#%% Connecting to ModBus client
ip   = '192.168.2.100'
port = 502

client = ModbusTcpClient(ip, port=port)
client.connect()

#%% Register structure
# ["Reg. addr.", "Data type", "# of regs"]
input_registers = [[0, "uint16", 1],
                   [1, "uint32", 2],
                   [3, "float32", 2],
                   [5, "float32", 2],
                   [7, "uint32", 2],
                   [9, "float32", 2],
                   [11, "float32", 2]]

holding_registers = [[0, "uint16", 1],
                     [1, "uint32", 2],
                     [3, "uint32", 2]]

#%% Encoding and deconding functions
# Encode 32-bit unsigned int
def encode_32_bit_integer(value):
    byte_value = struct.pack('>I', int(value))
    return struct.unpack('>HH', byte_value)

# Encode 32-bit float
def encode_32_bit_float(value):
    byte_value = struct.pack('>f', float(value))
    return struct.unpack('>HH', byte_value)

# Decode 32-bit unsigned int
def decode_32_bit_integer(registers):
    handle = [struct.pack('>H', p) for p in registers]
    binary_string = b''.join(handle)
    return struct.unpack('!I', binary_string)[0]

# Decode 32-bit float
def decode_32_bit_float(registers):
    handle = [struct.pack('>H', p) for p in registers]
    binary_string = b''.join(handle)
    return struct.unpack('!f', binary_string)[0]

def encode_16_bit_integer(value):
    return struct.unpack('>H', struct.pack('>H', int(value)))

def encode_16_bit_float(value):
    byte_value = struct.pack('>e', float(value))
    return struct.unpack('>H', byte_value)

def decode_16_bit_integer(register):
    return struct.unpack('>H', struct.pack('>H', register[0]))[0]

def decode_16_bit_float(register):
    byte_value = struct.pack('>H', register)
    return struct.unpack('>e', byte_value)[0]

#%% Read data
def read_data(addr, reg_type=None):
    if reg_type == 'holding':
        idx       = list(zip(*holding_registers))[0][:].index(addr)
        data_type = holding_registers[idx][1]
        count     = holding_registers[idx][2]
        data  = client.read_holding_registers(address=addr, count=count).registers

    else:
        idx       = list(zip(*input_registers))[0][:].index(addr)
        data_type = input_registers[idx][1]
        count     = input_registers[idx][2]
        data  = client.read_input_registers(address=addr, count=count).registers
    
    if data_type == 'uint32':
        value = decode_32_bit_integer(data)
    elif data_type == 'float32':
        value = decode_32_bit_float(data)
    elif data_type == 'uint16':
        value = decode_16_bit_integer(data)
        
    elif data_type == 'float16':
        value = decode_16_bit_float(data)
        print("Note, not fully tested, and at half precision, for float16")
    else:
        value = data
        print('Data is not in a supported format, uint32, uint16, float32, float16, no decoder available.')

    return value

#%% Write data
def manual_mode():
    val = encode_16_bit_float(1)
    client.write_registers(address=0, values=val)
    print('PLC is in manual mode')

def write_data(addr, val):
    idx       = list(zip(*holding_registers))[0][:].index(addr)
    data_type = holding_registers[idx][1]
    #count     = holding_registers[idx][2]
    
    if data_type == 'uint32':
        data = encode_32_bit_integer(val)
    elif data_type == 'float32':
        data = encode_32_bit_float(val)
    elif data_type == 'uint16':
        data = encode_16_bit_integer(val)
    elif data_type == 'float16':
        data = encode_16_bit_float(val)
        print("Note, not fully tested, and at half precision, for float16")
    else:
        print('Data is not in a supported format, uint32, uint16, float32, float16, no encoder available.')
    
    client.write_registers(address=addr, values=data)

def auto_mode():
    val = encode_16_bit_float(0)
    client.write_registers(address=0, values=val)
    print('PLC is in autonomous mode')