#!/bin/bash

cp cymuk.py release
cp setup.py release
cp requirements.txt release
rsync -r modules release --exclude modules/__pycache__
cp README.md release
cp LICENSE release
cp -r docs release
