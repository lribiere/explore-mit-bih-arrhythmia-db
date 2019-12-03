import plotly.graph_objects as go
import plotly.express as px
import streamlit as st
import pandas as pd
import glob
import wfdb
import os

'''
# MIT-BIH Arrhythmia DB Exploration
'''

record_ids = [os.path.basename(file)[:-4] for file in glob.glob('data/*.dat')]
record_ids.sort()
record_id = st.selectbox('Select a record id ', record_ids)

if record_id:
    record = wfdb.rdrecord('data/{}'.format(record_id))
    annotation = wfdb.rdann('data/{}'.format(record_id), 'atr')
    st.write('Number of signals : {} ({}), units : {}, frame / sec : {} ({})'
             .format(record.n_sig,
                     record.sig_name,
                     record.units,
                     record.fs,
                     record.samps_per_frame))
    st.write('comments : {}'.format(record.comments))
    signals_df = pd.DataFrame(record.p_signal, columns=record.sig_name)
    annot_serie = pd.Series(annotation.symbol, index=annotation.sample,
                            name='annotations')
    full_df = pd.concat([signals_df, annot_serie], axis=1)

    ''' ## Annotations'''
    st.write('Unique annotations found in this record : {}'.format(
        annot_serie.unique()))
    st.write('Some explanations on the annotations are available here : '
             'https://archive.physionet.org/physiobank/annotations.shtml')
    # Plot count by annotation
    annot_counts_df = annot_serie \
        .value_counts() \
        .rename_axis('annotations') \
        .reset_index(name='counts')
    bar_fig = px.bar(annot_counts_df, x='annotations', y='counts',
                     title='Annotations by count')
    st.write(bar_fig)

    ''' ## Explore full dataset '''
    # Display full dataframe (head 100)
    st.write('The 100 first samples : ')
    st.write(full_df.head(100))

    # Plot signal and annotations
    N_annotations = full_df['annotations'] == 'N'
    A_annotations = full_df['annotations'] == 'A'
    V_annotations = full_df['annotations'] == 'V'
    Plus_annotations = full_df['annotations'] == '+'

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=signals_df.index.values,
                             y=signals_df[record.sig_name[0]],
                             mode='lines',
                             name=record.sig_name[0]))
    fig.add_trace(go.Scatter(x=full_df.index[N_annotations].values,
                             y=signals_df[N_annotations][
                                 record.sig_name[0]].values,
                             mode='markers', name='N (annot)'))
    fig.add_trace(go.Scatter(x=full_df.index[A_annotations].values,
                             y=signals_df[A_annotations][
                                 record.sig_name[0]].values,
                             mode='markers', name='A (annot)'))
    fig.add_trace(go.Scatter(x=full_df.index[V_annotations].values,
                             y=signals_df[V_annotations][
                                 record.sig_name[0]].values,
                             mode='markers', name='V (annot)'))
    fig.add_trace(go.Scatter(x=full_df.index[Plus_annotations].values,
                             y=signals_df[Plus_annotations][
                                 record.sig_name[0]].values,
                             mode='markers', name='+ (annot)'))
    st.plotly_chart(fig)
    # fig = px.line(signals_df, x=signals_df.index.values, y=record.sig_name[0],
    #               title='Signals')
    # st.plotly_chart(fig)
