#!/bin/bash

if [[ $# -ge 1 ]]; then
    python3 stats.py $1
fi
