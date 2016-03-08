def table_to_header_file(table, names):
    s = ""
    count = 0
    for row in table:
        name = 'row%s' % count
        values = ', '.join(str(i) for i in row)
        line = 'bool %s[] = { %s };\n' % (name, values)
        s = s + line
        count = count + 1
    return s
