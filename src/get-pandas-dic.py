import bokeh
import catboost
import gensim
import keras
import lightgbm
import matplotlib as mpl
import nltk
import numpy as np
import pandas as pd
import plotly
import scipy
import scrapy
import seaborn as sns
import sklearn
import spacy
import statsmodels
import tensorflow as tf
import torch
import xgboost
from bs4 import BeautifulSoup

libraries = [
    pd,
    np,
    mpl,
    sns,
    sklearn,
    tf,
    keras,
    torch,
    statsmodels,
    scipy,
    nltk,
    spacy,
    gensim,
    scrapy,
    BeautifulSoup,
    bokeh,
    plotly,
    xgboost,
    lightgbm,
    catboost,
    # eli5,
]

# Writing to the txt file
with open("data_science_dictionary.txt", "w") as f:
    for library in libraries:
        # get all functions, classes, etc. in the library module
        all_library_contents = dir(library)
        new_contents = []

        # for each item in the library module
        for item in all_library_contents:
            try:
                # if the item is a class (or a type)
                if isinstance(getattr(library, item), type):
                    # get all methods in the class
                    methods = [
                        method
                        for method in dir(getattr(library, item))
                        if not method.startswith("_")
                    ]
                    new_contents.extend(methods)
            except AttributeError:
                # Skip if attribute doesn't exist
                continue

        all_library_contents.extend(new_contents)

        # Now, let's remove duplicates from the list:
        all_library_contents = list(set(all_library_contents))

        # Remove any private attributes or methods (those starting with a `_`)
        all_library_contents = [
            term for term in all_library_contents if not term.startswith("_")
        ]

        for term in all_library_contents:
            f.write(term + "\n")
