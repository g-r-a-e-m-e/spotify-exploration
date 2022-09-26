# pipeline.py is the ETL python file which will extract the raw data from Spotify
# using the Spotify API and pandas.

# The data will be dumped into /data to be read by the [analysis python file].py
# file later.

# Import packages
import pandas as pd
import requests

