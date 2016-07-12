#!/bin/bash

files="/Users/sasakiyo/Downloads/OneDrive-2016-03-27/*"
for filepath in ${files}
do
  filename=`basename ${filepath}`
  echo ${filename}
done
read wait
