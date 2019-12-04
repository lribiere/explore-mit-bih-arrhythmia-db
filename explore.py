import plotly.graph_objects as go
import plotly.express as px
import streamlit as st
import pandas as pd
from utils import *
import glob
import wfdb
import os

ANNOTATIONS_COL_NAME = 'annotations'

'''
# MIT-BIH Arrhythmia DB Exploration
'''

record_ids = [os.path.basename(file)[:-4] for file in glob.glob('data/*.dat')]

if len(record_ids) == 0:
    st.write('Warning ! No data could be found under the ./data/ directory.',
             '*\*.dat*, *\*.hea*, *\*.atr* files and such should be placed ',
             'immediately under the ./data/ directory')
else:
    record_ids.sort()
    record_id = st.selectbox('Select a record id ', record_ids)
    record = wfdb.rdrecord('data/{}'.format(record_id))
    annotation = wfdb.rdann('data/{}'.format(record_id), 'atr')
    st.write('Signals found in this record :')
    for idx, signal in enumerate(record.sig_name):
        st.write('- `{}` : in {}, with a frequency of {}hz'.format(
            signal, record.units[idx],
            record.fs * record.samps_per_frame[idx]))
    st.write('Comments for this record : {}'.format(record.comments))
    signals_df = pd.DataFrame(record.p_signal, columns=record.sig_name)
    annot_serie = pd.Series(annotation.symbol, index=annotation.sample,
                            name=ANNOTATIONS_COL_NAME)
    full_df = pd.concat([signals_df, annot_serie], axis=1)

    ''' ## Annotations'''
    unique_annot = annot_serie.value_counts().index.values
    st.write('This record contains the following annotations :')
    for annot in unique_annot:
        st.write('- `{}` : {}'.format(annot, annotation_definitions[annot]))
    st.write('More explanations on the annotations are available here : '
             'https://archive.physionet.org/physiobank/annotations.shtml')

    # Plot count by annotation
    annot_counts_df = annot_serie \
        .value_counts() \
        .rename_axis(ANNOTATIONS_COL_NAME) \
        .reset_index(name='counts')
    bar_fig = px.bar(annot_counts_df, x=ANNOTATIONS_COL_NAME, y='counts',
                     title='Annotations by count')
    st.write(bar_fig)

    ''' ## Explore full dataset '''
    signal = st.selectbox('Select a signal', record.sig_name)
    # Plot signals and annotations
    matching_rows_by_annot = {}
    for annot in unique_annot:
        matching_rows_by_annot[annot] = full_df[ANNOTATIONS_COL_NAME] == annot
    fig = go.Figure(layout=go.Layout(title=go.layout.Title(
        text='{} signal with annotations'.format(signal))))
    fig.add_trace(go.Scatter(x=full_df.index.values,
                             y=full_df[signal],
                             mode='lines',
                             name=signal))
    for annot, annot_matching_rows in matching_rows_by_annot.items():
        fig.add_trace(go.Scatter(x=full_df.index[annot_matching_rows].values,
                                 y=full_df[annot_matching_rows][signal].values,
                                 mode='markers',
                                 name='{} (annot)'.format(annot)))
    st.plotly_chart(fig)
