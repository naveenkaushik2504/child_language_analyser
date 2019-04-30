import os


class Analyser:
    """
    This class is responsible for generating the required statistics for any given cleaned transcript.
    """

    def __init__(self):
        """Constructor for the class. Initialises a dictionary with the basic statistics needed.

        Parameters
        -----------

        Returns
        -----------
        None
        """

        self.data = {'length': 0, 'size': 0, 'num_repeat': 0, 'num_retrace': 0, 'num_gram_error': 0, 'num_pauses': 0}

    def __str__(self):
        """Overriding the __str__ method to print the object in the desired format.

        Parameters
        -----------

        Returns
        -----------
        obj_desc: Formatted string to be displayed.
        """

        obj_desc = ""
        obj_desc += "\n The length of the Transcript is " + str(self.data['length'])
        obj_desc += "\n The size of the Transcript is " + str(self.data['size'])
        obj_desc += "\n The number of repetitions in the Transcript are " + str(self.data['num_repeat'])
        obj_desc += "\n The number of retracing in the Transcript are " + str(self.data['num_retrace'])
        obj_desc += "\n The number of grammatical errors in the Transcript are " + str(self.data['num_gram_error'])
        obj_desc += "\n The number of pauses made in the Transcript are " + str(self.data['num_pauses'])
        return obj_desc

    def analyse_script(self, cleaned_file):
        """This method accepts the cleaned transcript file and generates the desired statistics and stores in the
        instance variable 'data'.

        Parameters
        -----------
        cleaned_file: Cleaned transcript file

        Returns
        -----------
        None
        """

        file_contents = []
        # Open the file passed as argument
        with open(cleaned_file) as in_file:
            # Variable flag is just to handle the special case of [* m:+ed]
            flag = 0
            for line in in_file:
                for item in line.split():
                    if(flag == 1):
                        if(item == "m:+ed]"):
                            file_contents.append("[* " + item)
                        else:
                            file_contents.append(item)
                        flag = 0
                        continue
                    if(item == "[*"):
                        flag = 1
                    else:
                        file_contents.append(item)

        # Set the values in the instance variable 'data'
        self.data['length'] = file_contents.count(".") + file_contents.count("?") + file_contents.count("!")

        # Vocabulary is considered as the words in the file excluding all the special chat symbols.
        size_list = [x for x in file_contents if x.isalpha()]
        self.data['size'] = len(set(size_list))
        self.data['num_repeat'] = file_contents.count("[/]")
        self.data['num_retrace'] = file_contents.count("[//]")
        self.data['num_gram_error'] = file_contents.count("[* m:+ed]")
        self.data['num_pauses'] = file_contents.count("(.)")


# Below main function is the starting point of execution.
if (__name__ == "__main__"):
    # Create an object of the class
    analyser_obj = Analyser()

    # The below loop would run and print the stats for all the cleaned files present.
    # The function 'analyse_script' can also be used as a utility function to get the stats independently.
    for dir_path in ["SLI_cleaned", "TD_cleaned"]:
        for file in os.listdir(dir_path):
            file = os.path.join(dir_path, file)
            analyser_obj.analyse_script(file)
            print("---------------------------------------------------------------")
            print("Following statistics are for the file ", file)
            print(analyser_obj)
            print("---------------------------------------------------------------")
