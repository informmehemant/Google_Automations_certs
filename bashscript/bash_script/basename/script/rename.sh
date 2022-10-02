#!/bin/bash

cd ../old_website/

for file in *.htm; do
 name=$(basename "$file")
 mv "$file" "$name.html"
done