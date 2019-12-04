# Beat annotations
normal_beat = ('N', 'Normal beat (displayed as "·" by the PhysioBank ATM, LightWAVE, pschart, and psfd)')
left_bundle_branch_block_beat = ('L', 'Left bundle branch block beat')
right_bundle_branch_block_beat = ('R', 'Right bundle branch block beat')
bundle_branch_block_beat_unspecified = ('B', 'Bundle branch block beat (unspecified)')
atrial_premature_beat = ('A', 'Atrial premature beat')
aberrated_atrial_premature_beat = ('a', 'Aberrated atrial premature beat')
nodal_junctional_premature_beat = ('J', 'Nodal (junctional) premature beat')
supraventricular_premature_or_ectopic_beat_atrial_or_nodal = ('S', 'Supraventricular premature or ectopic beat (atrial or nodal)')
premature_ventricular_contraction = ('V', 'Premature ventricular contraction')
r_on_t_premature_ventricular_contraction = ('r', 'R-on-T premature ventricular contraction')
fusion_of_ventricular_and_normal_beat = ('F', 'Fusion of ventricular and normal beat')
atrial_escape_beat = ('e', 'Atrial escape beat')
nodal_junctional_escape_beat = ('j', 'Nodal (junctional) escape beat')
supraventricular_escape_beat_atrial_or_nodal = ('n', 'Supraventricular escape beat (atrial or nodal)')
ventricular_escape_beat = ('E', 'Ventricular escape beat')
paced_beat = ('/', 'Paced beat')
fusion_of_paced_and_normal_beat = ('f', 'Fusion of paced and normal beat')
unclassifiable_beat = ('Q', 'Unclassifiable beat')
beat_not_classified_during_learning = ('?', 'Beat not classified during learning')

beat_annotations = [normal_beat, left_bundle_branch_block_beat,
                    right_bundle_branch_block_beat,
                    bundle_branch_block_beat_unspecified,
                    atrial_premature_beat, aberrated_atrial_premature_beat,
                    nodal_junctional_premature_beat,
                    supraventricular_premature_or_ectopic_beat_atrial_or_nodal,
                    premature_ventricular_contraction,
                    r_on_t_premature_ventricular_contraction,
                    fusion_of_ventricular_and_normal_beat, atrial_escape_beat,
                    nodal_junctional_escape_beat,
                    supraventricular_escape_beat_atrial_or_nodal,
                    ventricular_escape_beat, paced_beat,
                    fusion_of_paced_and_normal_beat, unclassifiable_beat,
                    beat_not_classified_during_learning]

# Non-beat annotations
start_of_ventricular_flutter_fibrillation = ('[', 'Start of ventricular flutter/fibrillation')
ventricular_flutter_wave = ('!', 'Ventricular flutter wave')
end_of_ventricular_flutter_fibrillation = (']', 'End of ventricular flutter/fibrillation')
non_conducted_p_wave_blocked_apc = ('x', 'Non-conducted P-wave (blocked APC)')
waveform_onset = ('(', 'Waveform onset')
waveform_end = (')', 'Waveform end')
peak_of_p_wave = ('p', 'Peak of P-wave')
peak_of_t_wave = ('t', 'Peak of T-wave')
peak_of_u_wave = ('u', 'Peak of U-wave')
pq_junction = ('`', 'PQ junction')
j_point = ('\'', 'J-point')
non_captured_pacemaker_artifact = ('^', '(Non-captured) pacemaker artifact')
isolated_qrs_like_artifact = ('|', 'Isolated QRS-like artifact')
change_in_signal_quality = ('~', 'Change in signal quality')
rhythm_change = ('+', 'Rhythm change')
st_segment_change = ('s', 'ST segment change')
t_wave_change = ('T', 'T-wave change')
systole = ('*', 'Systole')
diastole = ('D', 'Diastole')
measurement_annotation = ('=', 'Measurement annotation')
comment_annotation = ('"', 'Comment annotation')
link_to_external_data = ('@', 'Link to external data')

non_beat_annotations = [ventricular_flutter_wave,
                        end_of_ventricular_flutter_fibrillation,
                        non_conducted_p_wave_blocked_apc, waveform_onset,
                        waveform_end, peak_of_p_wave, peak_of_t_wave,
                        peak_of_u_wave, pq_junction, j_point,
                        non_captured_pacemaker_artifact,
                        isolated_qrs_like_artifact, change_in_signal_quality,
                        rhythm_change, st_segment_change, t_wave_change,
                        systole, diastole, measurement_annotation,
                        comment_annotation, link_to_external_data]

annotation_definitions = dict(beat_annotations + non_beat_annotations)
