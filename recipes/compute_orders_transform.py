# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
revenue_loss = dataiku.Dataset("revenue_loss")
revenue_loss_df = revenue_loss.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

orders_transform_df = revenue_loss_df # For this sample code, simply copy input to output


# Write recipe outputs
orders_transform = dataiku.Dataset("orders_transform")
orders_transform.write_with_schema(orders_transform_df)
