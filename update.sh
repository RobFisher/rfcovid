#!/bin/bash

export PATH=~/.local/bin:$PATH # use user's Python and Jupyter installations
export TODAY=$(date '+%Y-%m-%d')
export CSV_FILENAME=covid_${TODAY}.csv

python3.7 fetch_csv.py $CSV_FILENAME
export FETCH_TIME=$(date)

jupyter nbconvert --execute --ExecutePreprocessor.timeout=600 --ExecutePreprocessor.kernel_name='python3' --to html --no-input analysis.ipynb

mkdir -p output
rm -f output/*.csv
mkdir -p archive
cp analysis.html output/index.html
cp covid-processed-${TODAY}.csv output/

cp analysis.html archive/analysis-${TODAY}.html
cp covid-processed-${TODAY}.csv archive/
cp ${CSV_FILENAME} archive/

cd output
surge --domain https://rfcovid.surge.sh $PWD
