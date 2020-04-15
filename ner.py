import spacy
import argparse
from truecaser import *
from truecaser.Truecaser import getTrueCase
import os
import _pickle as cPickle
import nltk
import string
import argparse
import fileinput

# only care about these entity types
ENT_SET = ('PERSON', 'NORP', 'FAC', 'ORG', 'GPE', 'LOC', 'PRODUCT', 'EVENT', 'LANGUAGE', 'DATE', 'TIME')  # refer to https://spacy.io/api/annotation#named-entities

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--file", type=str,
	help="path to speech file", required=True)
ap.add_argument('-d', '--distribution_object', help='language distribution file', required=True)

args = vars(ap.parse_args())

text_file = args['file']
dist_obj = args['distribution_object']

with open(dist_obj, 'rb') as f:
    uniDist = cPickle.load(f)
    backwardBiDist = cPickle.load(f)
    forwardBiDist = cPickle.load(f)
    trigramDist = cPickle.load(f)
    wordCasingLookup = cPickle.load(f)

with open('output.txt', 'w') as f:
    for sentence in fileinput.input(text_file):
        tokensCorrect = nltk.word_tokenize(sentence)
        tokens = [token.lower() for token in tokensCorrect]
        tokensTrueCase = getTrueCase(tokens, 'title', wordCasingLookup, uniDist, backwardBiDist, forwardBiDist, trigramDist)
        f.write(" ".join(tokensTrueCase))

# you can experiment with models here

# model = spacy.load("en_core_web_sm")
model = spacy.load("en_core_web_md")
# model = spacy.load("en_core_web_lg")

with open('output.txt', 'r') as f:
    doc = f.read()

annotations = model(doc)
entities = [ent for ent in annotations.ents if ent.label_ in ENT_SET ]  # filter entities

print(entities)