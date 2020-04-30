# text-to-speech-ner
A project to perform named entity recognition on speech to text output.

### Installing the environment
Note: You will need the Anaconda Package Manager to be able to run the code in this repo.
Run the following command from the root directory, to create a conda environment for the code (you can replace nerenv with any other environment name, in the first line of `environment.yml`):

``` conda env create -f environment.yml ```

Next, run the following command to activate your newly created environment:

``` conda activate nerenv ```

Now, we want to download 3 models from spacy, so that we can experiment with them(in my experience, the `en_core_web_md` model works best in terms of speed vs accuracy, but feel free to try out all 3). Run the following commands to download them:
- `python -m spacy download en_core_web_sm`
- `python -m spacy download en_core_web_md`
- `python -m spacy download en_core_web_lg`

We also want to download the `nltk tokenizer`, so run the following command to download it:

``` python -m nltk.downloader 'punkt' ```

Finally, we want to download a distributions object for casing the text files appropriately. Download it from [here](https://github.com/nreimers/truecaser/releases/download/v1.0/english_distributions.obj.zip), and unzip it in the root directory. Alternative, if you have wget installed, you can enter the following command:

``` wget https://github.com/nreimers/truecaser/releases/download/v1.0/english_distributions.obj.zip ```

and

``` unzip english_distributions.obj.zip ```
to unzip the file.

### Running the code
You are now ready to run `ner.py` on text files! In order to do so, run the following command:

`python ner.py -f sample.txt -d distributions.obj`

You can replace `sample.txt` with any text file. The output is a list of all entities found in the text file.

`ner.py` also contains an entity set to filter out the entities, which can be modified. Refer to [this webpage](https://spacy.io/api/annotation#named-entities) for more information.

DISCLAIMER: This repository makes use of TrueCaser, an open source project designed with the goal of reassigning case to uncased files. Since speech to text files are usually uncased, this resource is of an immense help. Check it out [here](https://github.com/nreimers/truecaser). Also note that this was written in Python 2.7, so I had to modify it for Python 3.6.

### Hardware
This code was tested on osx-64, as well as linux-64, but should work on any operating system.

### Benchmarks
The spacy models have the following benchmarks (in terms of entities):
| Model | Precision | Recall | F_Score |
|-------|-------|-------|-------|
| SM    | 85.89 | 85.21 | 85.55 |
| MD    | 86.34 | 86.17 | 86.25 |
| LG    | 86.74 | 86.36 | 86.55 |

As for the truecaser, the provided model achieves an accuracy of 98.39% on a small test set of random sentences from Wikipedia.
