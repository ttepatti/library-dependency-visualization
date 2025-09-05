#!/bin/bash
# dumps shared libraries for every binary in a folder to CSV
# csv format:
# binary_name,dependency_name

for file in *; do
        readelf -d ${file} | grep "Shared library:" |  cut -d "[" -f2 | cut -d "]" -f1 | while read line; do echo "${file},${line}"; done
done
