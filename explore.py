import plotly.graph_objects as go
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
    record_id = st.selectbox('Select a record id', record_ids)
    record = wfdb.rdrecord(f'data/{record_id}')
    annotation = wfdb.rdann(f'data/{record_id}', 'atr')
    st.write('Signals found in this record :')
    for idx, signal in enumerate(record.sig_name):
        st.write(f'- `{signal}` : in {record.units[idx]}, with a frequency of '
                 f'{record.fs * record.samps_per_frame[idx]}hz')
    st.write(f'Comments for this record : {record.comments}')
    signals_df = pd.DataFrame(record.p_signal, columns=record.sig_name)
    annot_serie = pd.Series(annotation.symbol, index=annotation.sample,
                            name=ANNOTATIONS_COL_NAME)
    full_df = pd.concat([signals_df, annot_serie], axis=1)

    ''' ## Annotations '''
    beat_annot_count = annot_serie.isin(dict(beat_annotations)).sum()
    non_beat_annot_count = annot_serie.isin(dict(non_beat_annotations)).sum()
    unique_annot = annot_serie.value_counts().index.values
    st.write(f'This record contains `{annot_serie.size}` annotations '
             f'among which `{beat_annot_count}` beat annotations and '
             f'`{non_beat_annot_count}` non beat annotation(s).')
    st.write('The annotations are the followings :')
    for annot in unique_annot:
        st.write(f'- `{annot}` : {annotation_definitions[annot]}')
    st.write('More explanations on the annotations are available here : '
             'https://archive.physionet.org/physiobank/annotations.shtml')

    # Plot counts for each annotation
    annot_counts_df = annot_serie \
        .value_counts() \
        .rename_axis(ANNOTATIONS_COL_NAME) \
        .reset_index(name='counts')
    bar_fig = go.Figure(data=[go.Bar(x=annot_counts_df[ANNOTATIONS_COL_NAME],
                                     y=annot_counts_df['counts'],
                                     text=annot_counts_df['counts'],
                                     textposition='auto'
                                     )])
    bar_fig.update_layout(title='Annotations by count', yaxis_title='counts',
                          xaxis_title='annotations')
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
