def int32_to_ip(n):
    return '.'.join(str((n >> (8 * i)) & 0xFF) for i in reversed(range(4)))

print(int32_to_ip(2154959208))