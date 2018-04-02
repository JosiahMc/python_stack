for row in range(0, 13):
    str_row = []
    str_format = "{0:{width}} {1:{width}} {2:{width}} {3:{width}} {4:{width}} {5:{width}} {6:{width}} {7:{width}} {8:{width}} {9:{width}} {10:{width}} {11:{width}} {12:{width}}"
    if row == 0:
        str_row.append("x ")
        pass
    for col in range(0, 13):
        if (row == 0 and col > 0):
            str_row.append(str(col))

        elif (row > 0 and col == 0):
            str_row.append(str(row))
        elif (row > 0 and col > 0):
            str_row.append(str(row * col))
    print str_format.format(*str_row, width=3)
