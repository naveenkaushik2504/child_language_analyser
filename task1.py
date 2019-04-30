import os


def process_1a(line):
    """Logic to process the Task 1a. It removes all the words inside '[' or ']'
    except for the characters [//], [/], [*] and [* m:+ed]

    Parameters
    -----------
    line: The line that needs to be pre processed for task 1a.

    Returns
    -----------
    result_1a: This is the line created after the processing done for the task 1a.
    """

    result_1a = ""
    # Iterate until the line becomes empty.
    while(len(line) != 0):
        popped_char = ""
        # If the character is starting with '[' then we need to look for its end and remove the words within it.
        if(line[0] == '['):
            small_str = ""
            while(popped_char != ']'):
                popped_char = line.pop(0)
                small_str += popped_char
            # If the word is any of the below one, then keep it, otherwise its discarded.
            if(small_str == "[//]" or small_str == "[/]" or small_str == "[* m:+ed]"):
                result_1a += small_str
        else:
            result_1a += line.pop(0)
    return result_1a


def process_1b(line):
    """Logic to process the Task 1b. It removes the characters '<' or '>' around the words.

    Parameters
    -----------
    line: The line that needs to be pre processed for task 1b.

    Returns
    -----------
    result_1b: This is the line created after the processing done for the task 1b.
    """

    result_1b = ""
    # Iterate until the line becomes empty.
    while (len(line) != 0):
        # If the character is starting with '<' then we need to look for its end and retain the words within it.
        if (line[0] == '<'):
            small_str = ""
            popped_char = line.pop(0)
            popped_char = line.pop(0)
            while (popped_char != '>'):
                small_str += popped_char
                popped_char = line.pop(0)
            result_1b += small_str
        else:
            result_1b += line.pop(0)
    return result_1b


def process_1c(line):
    """Logic to process the Task 1c. It removes the words that have prefixes '&' or '+'.

    Parameters
    -----------
    line: The line that needs to be pre processed for task 1c.

    Returns
    -----------
    result_1c: This is the line created after the processing done for the task 1c.
    """

    # Here we just split the entire line and return the line with the words which do not start with '&' or '+'.
    result_1c = ' '.join(word for word in line.split(' ') if not word.startswith('&') and not word.startswith('+'))

    return result_1c


def process_1d(line):
    """Logic to process the Task 1d. It removes the characters '(' or ')' around the words,
    but retains the words and the symbol '(.)'

    Parameters
    -----------
    line: The line that needs to be pre processed for task 1d.

    Returns
    -----------
    result_1d: This is the line created after the processing done for the task 1d.
    """

    result_1d = ""
    # Iterate until the line becomes empty.
    while(len(line) != 0):
        popped_char = ""
        # If the character is starting with '(' then we need to look for its end and retain the words within it.
        # We also need to retain the spacial word '(.)'
        if(line[0] == '('):
            small_str = ""
            while(popped_char != ')'):
                popped_char = line.pop(0)
                small_str += popped_char
            if(small_str == "(.)"):
                result_1d += small_str
            else:
                result_1d += small_str.lstrip('(').rstrip(')')
        else:
            result_1d += line.pop(0)
    return result_1d


def pre_process_line(line):
    """This code passes the line to 4 functions which complete the tasks for each of the requirement given.
    The output of one is fed to the next one and so on.

    Parameters
    -----------
    line: This is the line that needs to be pre processed from the original transcript.

    Returns
    -----------
    result: Returns the processed line.
    """

    # Here we call the 4 functions one by one and pass the output of one to the next one.

    result = process_1a(list(line))
    result = process_1b(list(result))
    result = process_1c(result)
    result = process_1d(list(result))
    return result


def process_data(input_dir, output_dir):
    """This code emits out each of the *CHI line of the transcripts and sends those lines for pre processing.

    Parameters
    -----------
    input_dir: This is the input directory to read the child transcripts (SLI, TD)
    output_dir: This is the Output directory of the cleaned transcripts (SLI_cleaned, TD_cleaned)

    Returns
    -----------
    None
    """

    # The following path used is based on the dataset that was given.
    for file in os.listdir(os.path.join("data", input_dir)):
        # Each file path is considered to be absolute path relative the the directory of the code.
        file = os.path.join("data", input_dir, file)
        if file.endswith(".txt"):
            print("Processing file ", file)
            with open(file) as in_file:
                # flag variable is used to detect the end of required *CHI line.
                flag = 0
                with open(os.path.join(output_dir, os.path.basename(file)), 'w') as out_file:
                    chi_line = ""
                    for line in in_file:
                        # Whenever the line starts with "*CHI:" we consider that until we get "%mor" or "*EXA:" which
                        # indicates the start of the next line.
                        if(line.startswith(("*CHI:"))):
                            flag = 1
                            chi_line += line.lstrip("*CHI:\t")
                            continue
                        if(flag == 1):
                            if (not (line.startswith(("%mor:")) or line.startswith(("*EXA:"))) ):
                                chi_line += line.lstrip("*CHI:")
                            else:
                                # Once we find the line of our use, we pre process it as per the requirements.
                                out_file.write(pre_process_line(chi_line))
                                chi_line = ""
                                flag = 0


# We first process the SLI scripts.
print("Processing for SLI transcripts will be done first. ")
process_data("SLI", "SLI_cleaned")
print("Processing of SLI completed.")

# Next we move to the TD transcripts and clean them.
print("Processing for TD transcripts will be done now. ")
process_data("TD", "TD_cleaned")
print("Processing of TD completed.")

print("All the child transcripts have been processed and stored in directories SLI_cleaned and TD_cleaned")

