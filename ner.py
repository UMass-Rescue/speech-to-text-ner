import spacy
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--file", type=str,
	help="path to speech file")

args = vars(ap.parse_args())

text_file = args['file']

# model = spacy.load("en_core_web_sm")
# model = spacy.load("en_core_web_md")
model = spacy.load("en_core_web_lg")

with open(text_file, 'r') as f:
    doc = f.read()

annotations = model(doc)

print(annotations.ents)