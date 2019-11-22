filepath = 'output_from1.txt'

memory = []
register = [0, 0, 0, 0, 0, 0, 0, 0]

file = open(filepath, 'r')
counter = 0
for line in file:
    memory.append(int(line))
    print(memory[counter])
    counter += 1

_inst = 0
for i in range(len(memory)):
    if (bin(memory[i])[0] == '-'):
        code = (bin(memory[i])[3:]).zfill(32)
    else:
        code = bin(memory[i])[2:].zfill(32)

    opCode = code[7] + code[8] + code[9]
    # print(opCode)
    print(opCode + "\n")
    print(opCode + "\n")
    if opCode == "000" or "001":
        print("R-type")
        if opCode == "000":
            print("add")
            rs1 = code[10] + code[11] + code[12]
            rs2 = code[13] + code[14] + code[15]
            rd = code[29] + code[30] + code[31]
            register[int(rd, 2)] = register[int(rs1, 2)] +
            register[int(rs2, 2)]

        if opCode == "001":
            rs1 = code[10] + code[11] + code[12]
            rs2 = code[13] + code[14] + code[15]
            rd = code[29] + code[30] + code[31]
            register[int(rd, 2)] = register[int(
                rs1, 2)] & register[int(rs2, 2)]
            register[int(rd, 2)] = ~register[int(rd, 2)]
            print("nand")
    if opCode == "010" or "011" or "100":
        print("I-type")
        if opCode == "010":
            print("lw")
        if opCode == "011":
            print("sw")
        if opCode == "100":
            print("beq")
    if opCode == "101":
        rs1 = code[10] + code[11] + code[12]
        rs2 = code[13] code[14] + code[15]
        register[int(rs2, 2)] = i + 1
        i = rs1
        print("J-type")
        print("jalr")
    if opCode == "111" or "110":
        print("O-type")
        if opCode == "111":
            i += 1
            break
            print("halt")
        if opCode == "110":
            print("noop")
