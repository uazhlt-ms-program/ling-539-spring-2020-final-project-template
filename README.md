_TODO: Explain the layout of your final project, any notes, etc._ 
My final project takes a semi-supervised approach, using pretrained embeddings, to classify a dataset of newspaper articles into 6 topics/categories. To select the categories uses LDA and insight knowledge of the researcher.

# Presentation

- _TODO: include URL here_

_NOTE: A PDF of your presentation slides named `presentation-slides.pdf` should be added under the `presentation-slides` directory._

_Your presentation video may be uploaded to [Google Drive](https://drive.google.com/) (**New** &rarr; **File upload**), [YouTube](https://studio.youtube.com/), [Vimeo](https://vimeo.com/upload), [DropBox](https://www.dropbox.com) (**Upload files**), or [Box](https://arizona.account.box.com) (**Upload** &rarr; **File**).  The video does not need to be public (i.e., discoverable via a web search), so long as your instructor can view it via the URL above._ 

_The expected length of the video is 3-10 minutes._

# Data

_TODO: Provide 1) a description of your data and 2) a link/instructions for access._

My dataset consists in about 3000 newspaper articles that mention the event of violence known as “Piazza Fontana” bombing, which took place on December 12, 1969 in Milan, Italy. 
I collected the articles by scraping the online archive of one of the main Italian newspaper, “La Repubblica”  for the time period from 1984 to 2019.
These data ("rep_main&art_clean_pzfontana_manualcheck_1984_2019.csv") are accessible at this link: 

The pretraned embeddings dataset is avaiable at this link (select italian, 100d) https://wikipedia2vec.github.io/wikipedia2vec/pretrained/
Note that these data needs to be decompressed before use. These vectors have been trained on Italian Wikipedia with the skip-gram model (window=5, iteration=10, negative=15)
The data are offered in binary and text format (I used the text format) and as 100d and 300d vectors (I used the 100d)


# Code

_TODO: Provide commands and descriptions for running your code. Feel free to add subsections as needed._

The code is organized in 4 steps, each with a set of functions. Each function has docstrings to explain what the function does and the parameters it takes.
STEP 1: LOAD THE DATASET AND PREPROCESS IT
STEP 2: UNZIP, LOAD, AND PREPROCESS THE PRETRAINED EMBEDDINGS DATASET
STEP 3: MATCH THE PRETRAINED EMBEDDINGS WITH MY DATA AND TRANSFORM MY DATA INTO VECTORS
STEP 4: CLASSIFY DOCUMENTS INTO CATEGORIES USING COSINE SIMILARITY 

## Installation

_TODO: Provide the commands for installing all necessary dependencies._

``` 
# executed from within the `code` directory:
docker build -f Dockerfile -t "ling-539/final-project:latest" .
```

## Tests

_TODO: You are encouraged (but not required) to write tests to ensure your code can be run.  If you write tests, provide instructions for running them here.  Otherwise, remove this subsection._

```
docker run -it python tests.py
```
