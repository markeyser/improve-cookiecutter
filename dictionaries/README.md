# Data-Science Dictionary

There are many popular data science libraries in Python, which are
commonly used for various purposes including data manipulation,
visualization, machine learning, and more. Here are some of them. All
methods (including private methods), functions and classes in these
popular data science libraries have been included in the dictionary file
`data-science-en.txt`.

> TODO: as you can see, there word Matplotlib is not included in the
> dictionary. So, I guess maybe we need to include also a version with
> the capital letter at the beginning and a version with all capitals
> such as MATPLOTLIB. matplotlib. Be careful, you do not need to add the
> capitalized version. I had to add just the list of the name of the
> libraries it self at the beginning of the file:
> bokeh
> catboost
> gensim
> keras
> lightgbm
> matplotlib
> nltk
> numpy as np
> pandas as pd
> plotly
> scipy
> scrapy
> seaborn as sns
> sklearn
> spacy
> statsmodels
> tensorflow as tf
> torch
> xgboost
>
> Create `data-science-en.txt` with even a much longer list of Python
> libraries. Then create code to create another
> `project-dependencies.txt` that is created automatically from the
> `requirements.txt` file. So, ask in the main README.md file to include
> all packages installed in the project in this file. And then, use
> Makefile to execute a Python script that creates the
> `project-dependencies.txt` dictionary.
> Another idea, include the dictionaries folder inside the .vscode
> folder to avoid confusion. Include also the .csell.json file there.

1. **Pandas**: A powerful library for data manipulation and analysis. It
   provides data structures for efficiently storing large datasets and
   tools for data wrangling and analysis.
2. **NumPy**: A library for numerical computing in Python. It provides a
   high-performance multidimensional array object, and tools for working
   with arrays.
3. **Matplotlib**: A plotting library for creating static, animated, and
   interactive visualizations in Python.
4. **Seaborn**: A statistical data visualization library based on
   Matplotlib. It provides a high-level interface for creating
   attractive graphics.
5. **Scikit-Learn**: A machine learning library in Python. It provides
   simple and efficient tools for predictive data analysis.
6. **TensorFlow**: A library developed by the Google Brain team for
   complex numerical computations and building deep learning models.
7. **Keras**: A high-level neural networks API, written in Python and
   capable of running on top of TensorFlow, CNTK, or Theano.
8. **PyTorch**: A Python package that provides tensor computation (like
   NumPy) with strong GPU acceleration, and deep neural networks built
   on a tape-based autograd system.
9. **Statsmodels**: A Python module that provides classes and functions
   for the estimation of many different statistical models, as well as
   for conducting statistical tests, and statistical data exploration.
10. **SciPy**: A library that provides many efficient and user-friendly
    interfaces for tasks such as numerical integration, interpolation,
    optimization, linear algebra, and more.
11. **NLTK (Natural Language Toolkit)**: A leading platform for building
    Python programs to work with human language data.
12. **Spacy**: A library for advanced Natural Language Processing in
    Python.
13. **Gensim**: A library for unsupervised topic modeling and natural
    language processing, using modern statistical machine learning.
14. **Scrapy**: A fast high-level web crawling & scraping framework for
    Python.
15. **Beautiful Soup**: A library for pulling data out of HTML and XML
    files.
16. **Bokeh**: An interactive visualization library that targets modern
    web browsers for presentation.
17. **Plotly**: A graphing library makes interactive,
    publication-quality graphs.
18. **XGBoost/LightGBM/CatBoost**: Libraries for the gradient boosting
    framework. They are widely used for structured data machine learning
    projects.

These are just a few of the many libraries available, but they're some
of the most commonly used in data science projects.

Bellow the Python code to create the file `data-science-en.txt`. Fell
free to add more packages to the list.

```python
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
with open("dictionaries/data-science-en.txt", "w") as f:
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
```