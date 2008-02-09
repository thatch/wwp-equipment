#!/bin/bash
python grapher3.py new/*.csv
cd graph
    rm *.png
    for f in mk*.sh; do
        echo "Graphing $f"
        bash $f
    done

