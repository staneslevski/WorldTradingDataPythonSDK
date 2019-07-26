#!/usr/bin/env bash

rm -dR dist && \
rm -dR build && \
python3 setup.py sdist bdist_wheel && \
twine upload dist/*
