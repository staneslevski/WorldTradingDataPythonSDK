#!/usr/bin/env bash

rm dist/* build/* && \
python3 setup.py sdist bdist_wheel && \
twine upload dist/*
