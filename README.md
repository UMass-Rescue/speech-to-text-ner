# text-to-speech-ner
A project to perform named entity recognition on speech to text output.

### Installing the environment
Note: You will need the Anaconda Package Manager to be able to run the code in this repo.
Run the following command from the root directory, to create a conda environment for the code (you can replace nerenv with any other environment name):

``` conda create --name nerenv --file spec-file.txt ```

Next, run the following command to activate your newly created environment:

``` conda activate nerenv ```

Now, we want to download 3 models from spacy, so that we can experiment with them(in my experience, the `en_core_web_md` model works best in terms of speed vs accuracy, but feel free to try out all 3). Run the following commands to download them:
- `python -m spacy download en_core_web_sm`
- `python -m spacy download en_core_web_md`
- `python -m spacy download en_core_web_lg`

You are now ready to run `ner.py` on text files! In order to do so, run the following command:

`python ner.py -f sample.txt -d distributions.obj`

You can replace `sample.txt` with any text file. The output is a list of all entities found in the text file.

DISCLAIMER: This repository makes use of TrueCaser, an open source project designed with the goal of reassigning case to uncased files. Since speech to text files are usually uncased, this resource is of an immense help. Check it out [here](https://github.com/nreimers/truecaser). Also note that this was written in Python 2.7, so I had to modify it for Python 3.6.
