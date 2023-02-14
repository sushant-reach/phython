def solve(A):
    count = 0
    substr = 0
    for i in A:
        if i == "1":
            count += 1
        else:
            count -= 1

        if count == 0:
            substr += 1

    if count == 0:
        return substr
    else:
        return 1


A = "00110000010000101111001000111011011001101101110100000110111110101001100111100001111100001000000111101111101001100110000010001100010100100111011011111110100000011100001000100001111000010110101000011001101101111001110010100100110000011110110101010001100000111011000110011111110000010010111100111111111000100111101011101011111011111101101110011000001010100000111101100010011010111111001111011011100001011000110111010001110111110101101110110100011110100110010110101001110101010000010001100100101010010011110011001100001010100010111001110110011101000000001101011000101011000101101100001011110100010100011011101110101011000011111101000010101111010100001000000000001011101010111010000001111010000001111011111010000000111000001001011001100010111010011001101110000111110011001000100011111010010001010001100001110110100010100000001110110110110111010110101011010010110100010000101010101111101101001111010010010000011111110100011000001111101111100011010100110010100110101011110101100010100000010101111001100001010110011100010111010111011001010000011100101001110000101111000110100100111101001111001011000100111010111110000011101000010100000111111010101110010010110111011000001110101000001101110011111001000000111000110100000110101011100110111000010001010101010101100011101000110011110000110010000111011101000000110000010111101011100100001101000001010101101111000111100001011100011110001011111001111011110110010100010000100101001111001010111101000100000000111101001101011110000110011010110011111101011010101000101101101110000011100110001011011100110100001100000000110001001111000100101000010111011111111001110110111011100100011110010110110001111100110100001100001001011101001101010100100001111101010110000111000000100110000011001101110000101101101001110011001010000000111010000001100110000001000100110000101000011111100110111001011001000111110100110101000010111101101011100111110011011000010010111101001001010001110000101111101011001011101011101100100110010100001111010101001110101110011001000110110001011111111111"
print(solve(A))