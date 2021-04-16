"""
Project for Week 4 of "Python Data Representations".
Find differences in file contents.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

IDENTICAL = -1


def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs.

      Returns IDENTICAL if the two lines are the same.
    """
    _i_ = -1
    short_length = min(len(line1), len(line2))
    if len(line1) == len(line2):
        for _i_ in range(len(line1)):
            if line1[_i_] != line2[_i_]:
                return _i_
        return IDENTICAL
    else:
        for _i_ in range(short_length):
            if line1[_i_] != line2[_i_]:
                return _i_
        return _i_ + 1


def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index at which to indicate difference
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """
    if "\n" in line1 or "\n" in line2:
        return ""
    elif "\r" in line1 or "\r" in line2:
        return ""
    elif idx < 0 or idx > min(len(line1), len(line2)):
        return ""
    return (line1 + "\n" + '=' * (idx) + "^" + "\n" + line2 + "\n")


def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.

      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
    _i_ = -1
    short_length = min(len(lines1), len(lines2))
    if len(lines1) == len(lines2):
        for _i_ in range(len(lines2)):
            diff = singleline_diff(lines1[_i_], lines2[_i_])
            if diff != -1:
                return _i_, diff
        return IDENTICAL, IDENTICAL
    else:
        for _i_ in range(short_length):
            diff = singleline_diff(lines1[_i_], lines2[_i_])
            if diff != -1:
                return _i_, diff
        return _i_ + 1, 0


def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    file = open(filename, 'rt')
    return file.read().splitlines()


def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    list1 = get_file_lines(filename1)
    list2 = get_file_lines(filename2)
    diff = multiline_diff(list1, list2)
    line_no = "Line " + str(diff[0]) + ":\n"
    if diff[0] != -1 and diff[1] != -1:
        _a_ = list1[diff[0]]
        _b_ = list2[diff[0]]
        return line_no + singleline_diff_format(_a_, _b_, diff[1])
    return "No differences\n"
