import sys
import re

if len(sys.argv) == 3:
    input_f, output_f = sys.argv[1], sys.argv[2]
    collapsed = False
elif len(sys.argv) == 4:
    input_f, output_f = sys.argv[2], sys.argv[3]
    collapsed = sys.argv[1] == '--collapsed'

output_lines = []
column_names = []
collapsed_line = []

f = open(input_f, "r")
col1 = None
for line in f:
    if not line:
        col1 = None
        continue
    find_col1 = re.match(r'^\[(?P<col1>.+)\]$', line)
    if find_col1:
        col1 = find_col1.group('col1')
        if collapsed and collapsed_line:
            output_lines.append("{}\n".format(
                ",".join(collapsed_line)
            ))
        collapsed_line = [col1]
        continue
    if col1 and line:
        find_line = re.match(r'^(?P<col2>\w+)\s*=\s*(?P<col3>\w+)$', line)
        if find_line:
            column_name = find_line.group('col2')
            if collapsed:
                if column_name not in column_names:
                    column_names.append(column_name)
                collapsed_line.append(find_line.group('col3'))
            else:
                output_lines.append("{},{},{}\n".format(
                    col1,
                    column_name,
                    find_line.group('col3')
                ))
f.close()
if collapsed:
    # catch that dangling collapsed line since theyre only being appended
    # during the new col1 find.
    output_lines.append("{}\n".format(
        ",".join(collapsed_line)
    ))
    # insert the header line
    output_lines.insert(0, "{},{}\n".format(
        "header",
        ",".join(column_names)
    ))

f = open(output_f, "w")
for line in output_lines:
    f.write(line)
f.close()
