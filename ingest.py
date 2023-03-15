import pandas as pd
import os
import sqlite3
import numpy as np
import logging

# Create and configure logger
logging.basicConfig(filename="db_alteration.log", format='%(asctime)s %(message)s')

# Creating an object
logger = logging.getLogger()

# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)


def ingest():
    # Logging start time of ingestion
    logger.info("Weather data ingestion started")

    # Variable for database connection
    db_conn = sqlite3.connect('weather.sqlite')

    try:
        # Creating the variable for directory
        directory = './wx_data'

        # Initializing pandas dataframe
        weather_data = pd.DataFrame()

        # Iterating over all files in the directory
        for filename in os.listdir(directory):

            # Checks if the file have 'txt' extension
            if filename.endswith(".txt"):
                path = os.path.join(directory, filename)

                # Reading the file and creating temporary dataframe
                temp = pd.read_csv(path, sep="\t", header=None,
                                   names=["date", "max_temperature", "min_temperature", "precipitation"])

                # Replacing -9999 with pd.nan
                temp.replace(-9999, np.nan, inplace=True)

                # converting date column to string
                temp['date'] = temp['date'].astype(str)

                # Creating column of station_id by giving the id from the filename itself
                temp["station_id"] = filename[:11]

                # Appending all dates and station data
                weather_data = pd.concat([weather_data, temp])

        weather_stats = weather_data.copy()

        # Creating year column from date
        weather_stats['year'] = weather_stats['date'].str[:4]

        # Computing weather stats
        weather_stats = weather_stats.groupby(["station_id", "year"]).agg(
            {'max_temperature': 'mean', 'min_temperature': 'mean', 'precipitation': 'sum'
             }).reset_index()

        # Renaming the columns to appropriate column names
        weather_stats.rename(
            columns={'max_temperature': 'avg_max_temperature', 'min_temperature': 'avg_min_temperature',
                     'precipitation': 'total_precipitation'}, inplace=True)

        # Altering db tables with the data
        weather_data.to_sql("WeatherData", db_conn, if_exists="replace")
        weather_stats.to_sql("WeatherStats", db_conn, if_exists="replace")

        # Logging end time of ingestion
        logger.info("Weather data ingestion ended")
    except Exception as e:
        logger.error(e, exc_info=True)
    finally:
        # Closing db connection
        db_conn.close()
    return


ingest()
