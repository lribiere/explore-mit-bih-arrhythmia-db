# explore-mit-bih-arrhythmia-db

This small project aims at helping the exploration of the MIT-BIH Arrhythmia Database. The MIT-BIH Arrhythmia Database can be found at : https://physionet.org/content/mitdb/1.0.0/.

Some explanations on the WFDB file format are available here : https://www.physionet.org/physiotools/wpg/wpg_35.htm

## Prerequisites

Download the content of the database inside a `data` folder at the root of the project. From the project root directory, you can do this with the following commands from the terminal : 
```
wget -r -N -c -np https://physionet.org/files/mitdb/1.0.0/
mv physionet.org/files/mitdb/1.0.0/ data/
``` 

## Usage

From the terminal :
```
streamlit run explore.py
```