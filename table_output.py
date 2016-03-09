def table_to_header_text(table, names):
    s = ""
    count = 0
    row_names = []
    for row in table:
        name = 'row%s' % count
        values = ', '.join(str(i) for i in row)
        line = 'bool %s[] = { %s };\n' % (name, values)
        s = s + line
        count = count + 1
        row_names.append(name)
    table_dec = "bool **table = new bool*[%d]{\n" % (count, )
    s = s + table_dec
    row_list = ", ".join(row_names)
    list_of_rows = "        %s\n" % (row_list, )
    s = s + list_of_rows
    s = s + "};\n\n"
    quoted_names = ', '.join( '"' + n + '"' for n in names )
    names_dec = "std::vector<std::string> names = { %s };\n" % (quoted_names, )
    s = s + names_dec
    return s
