FrmPayloadFoo = "10110011111001101101111010010010"
FrmPayloadBar = "10110111111010001100001110010010"
FooBinary = "01000110011011110110111100100001"
BarBinary = "01000010011000010111001000100001"


def main():
    xor_foo_bar = simple_xor(FrmPayloadFoo, FrmPayloadBar)
    print(xor_foo_bar)

    decrypt_foo = simple_xor(xor_foo_bar, BarBinary)
    print(decrypt_foo)

    n = int(decrypt_foo, 2)
    x = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
    print(x)


def simple_xor(message_one, message_two):
    return ''.join('0' if a == b else '1' for a, b in zip(message_one, message_two))


if __name__ == '__main__':
    main()
