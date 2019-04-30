import pandas as pd
import os
import matplotlib.pyplot as plt
from task2 import Analyser


class Visualiser:
    """
    This class is responsible for creating visualisations for the SLI or TD transcripts and compare them
    using appropriate charts.
    """

    def __init__(self, data):
        """Constructor for the class. Initialises the data frame using the method 'create_data_frame' as shown.
        A data frame is capable of storing and displaying the data in a tabular format. Please note that this
        constructor does not take any argument, because the caller will not have the data at the time of
        creation of the object and hence the method, create_data_frame() has not been introduced.

        Parameters
        -----------

        Returns
        -----------
        None
        """

        # The instance variable is assigned using this method.
        self.data = data

    def compute_averages(self):
        """This method computes the mean of all 6 statistics and return them as 2 dictionaries.

        Parameters
        -----------

        Returns
        -----------
        mean_stats_sli: dictionary containing the mean of 6 statistics for SLI group.
        mean_stats_td : dictionary containing the mean of 6 statistics for TD group.
        """

        # Initialise the two empty dictionaries to store the means.
        mean_stats_sli, mean_stats_td = {}, {}

        for col in self.data.columns:
            # The way data frame is created, the first 10 rows belong to SLI and the bottom 10 for TD.
            # And hence the below 2 statements work for each of the column looped over.
            mean_stats_sli[col] = self.data[col].head(10).mean()
            mean_stats_td[col] = self.data[col].tail(10).mean()

        return mean_stats_sli, mean_stats_td

    def visualise_statistics(self):
        """This method compares all the 6 statistics for both the groups against each other and generates the
        appropriate graphs as visualisation.

        Parameters
        -----------

        Returns
        -----------
        None
        """

        # Run the loop on all the columns and calculate the mean
        for col in self.data.columns:
            # Find the mean to plot the graph
            mean_sli = self.data[col].head(10).mean()
            mean_td = self.data[col].tail(10).mean()

            # Create bar chart using the below method.
            plt.bar(['SLI', 'TD'], [mean_sli, mean_td])

            # Set the title to the figure.
            plt.title("Comparing " + col + " of SLI and TD")

            # Set the y label
            plt.ylabel(col)

            # Save the figure
            plt.savefig("SLI_TD_"+col)
            plt.gcf().clear()
            # plt.show()
        return


def create_data_frame():
    """This method creates the data frame required for further processing.
    This method is called from within the constructor (__init__) of this class.

    Parameters
    -----------

    Returns
    -----------
    data_df: Data Frame containing the statistics of all the child transcripts.
    """

    # Create an empty data frame with the columns as set below.
    data_df = pd.DataFrame(columns=['length', 'size', 'num_repetition', 'num_retracing',
                                    'num_grammatical_error', 'num_pauses'])

    # Populate the data frame with the statistics of all the files present in cleaned directories.
    for dir_path in ["SLI_cleaned", "TD_cleaned"]:
        data_dict = {}
        for file in os.listdir(dir_path):
            file = os.path.join(dir_path, file)
            key = os.path.basename(file).strip(".txt")
            data_list = []

            # Create an object of Analyser class and use that to analyse the scripts.
            analyser_obj = Analyser()
            analyser_obj.analyse_script(file)

            # Append the statistics to a list and then add that element to the dictionary.
            data_list.append(analyser_obj.data['length'])
            data_list.append(analyser_obj.data['size'])
            data_list.append(analyser_obj.data['num_repeat'])
            data_list.append(analyser_obj.data['num_retrace'])
            data_list.append(analyser_obj.data['num_gram_error'])
            data_list.append(analyser_obj.data['num_pauses'])

            # Make the key of the dictionary as the name of the file.
            data_dict[key] = data_list

        # Create the data frame from the dictionary.
        df = pd.DataFrame.from_dict(data_dict, 'index', columns=['length', 'size', 'num_repetition',
                                                                 'num_retracing', 'num_grammatical_error',
                                                                 'num_pauses'])

        # Now, append the data frame created to the main data frame which would be used for plotting.
        data_df = data_df.append(df)

    # Tabular display of the statistics of all the child transcripts.
    print(data_df)

    return data_df


if (__name__ == "__main__"):

    # Create a data frame from the cleaned file to pass to the constructor of Visualiser class.
    df_data = create_data_frame()

    # Create an object of the class
    visualiser_obj = Visualiser(df_data)

    # The below method returns the mean of both SLI and TD scripts
    mean_stats_sli, mean_stats_td = visualiser_obj.compute_averages()
    print("The mean statistics for SLI scripts are as follows:", mean_stats_sli)
    print("The mean statistics for TD scripts are as follows:", mean_stats_td)

    # The below method is responsible for plotting the comparisons of SLI and TD scripts
    # of the 6 statistics.
    visualiser_obj.visualise_statistics()

