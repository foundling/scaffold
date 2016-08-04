import utils

def validate_schema(schema_lines):

    ''' Validates schema and returns indent size if valid, otherwise raises ValueError.

        Once an indent size N is determined, each indentation level must be:

            1) less than N by a multiple of N,  e.g. 8 -> 4 or 8 -> 0
            2) 0, or 
            3) preceded by a directory and greater than N by exactly N.
    '''

    #
    # Initialize indent and line number of first indent.
    #

    indent = 0 
    start_index = 0
    for index, line in enumerate(schema_lines):
        if utils.parse_indent(line) > 0:
            indent = utils.parse_indent(line)
            start_index = index
            break

    #
    # Parse first line after indent according to the validation rules.
    #

    last_indent = indent
    prev_line = schema_lines[start_index]
    for index, line in enumerate( schema_lines[start_index + 1:] ):

        if utils.is_empty(line) or utils.is_comment(line):
            prev_line = line
            continue

        this_indent = utils.parse_indent(line) 
        difference = this_indent - last_indent

        if (difference == 0) or (difference == indent and utils.is_dir(prev_line)) or (difference < 0 and utils.is_multiple_of_indent(this_indent, indent)):
            last_indent = this_indent
            continue
        else:
            line_number = 1 + index + start_index
            raise ValueError('Parsing error on line {}:\n\n{}: {}'.format(line_number, line_number, line))

        prev_line = line

    return indent


