from utils import parse_indent, is_empty, is_comment, is_dir, is_multiple_of_indent

''' 
    Validates schema and returns indent size if valid, otherwise raises ValueError.

    Once an indent size N is determined, each indentation level must be:

        1) less than N by a multiple of N,  e.g. 8 -> 4 or 8 -> 0
        2) 0, or 
        3) preceded by a directory and greater than N by exactly N.
'''

class Validator():

    def __init__(schema_lines):
        self.indent = None
        self._schema_lines = schema_lines

    #
    # Initialize indent and line number of first indent.
    #
    def find_first_indent(self):
        ''' returns tuple(indent_value, index in schema lines) '''

        indent, start_index = 0, 0 

        for index, line in enumerate(self._schema_lines):
            if parse_indent(line) > 0:
                indent = parse_indent(line)
                break

        return indent, start_index

    def validate(self):

        #
        # Parse according to the validation rules, starting at the line after the first indent.
        #

        is_valid = True

        first_indent, start_index = self.find_first_indent()
        prev_indent = indent
        prev_line = self._schema_lines[start_index]
        lines = self._schema_lines[start_index + 1:]

        for index, line in enumerate(lines):

            if is_empty(line) or is_comment(line):
                prev_line = line
                continue

            this_indent = parse_indent(line) 
            difference = this_indent - prev_indent

            if (difference == 0) or\
               (difference == indent and is_dir(prev_line)) or\
               (difference < 0 and is_multiple_of_indent(this_indent, indent)):
                prev_indent = this_indent
                continue
            else:
                line_number = 1 + index + start_index
                print 'Parsing error on line {}:\n\n{}: {}'.format(line_number, line_number, line)
                is_valid = False

            prev_line = line

        return is_valid
