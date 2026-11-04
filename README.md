Why those params?###
|Parameter| Value |   Why   |
|---------|--------|-------|
|peak_width_limits |  (1.2,6)   | The tutorial says the lower bound should be about 2× the frequency resolution. Ours is 0.556 Hz, so about 1.1 Hz. The upper limit of 6 matches the tutorial’s group example. |
|max_n_peaks | 6 | The tutorial’s example value, to limit overfitting. |
|peak_threshold | 2.0 | FOOOF’s default. Old 0.5 was very permissive. |
|min_peak_height | 0.1 | Roughly 2–3× your fit errors (0.03–0.06). The tutorial says to set it relative to the noise level. |
|aperiodic_mode | fixed | The standard choice, and the plots show the 1/f slope fits well without a knee. |
| Fit range | 2–40 Hz | Kept from your original code. |
|Edge rule	|within 0.3 Hz of the window edge|	A peak at the boundary is probably the tail of something outside the window. 0.3 is about half the frequency resolution.|
|MIN_ALPHA_HEIGHT	|0.3|	The 10 heights split into 0.18–0.19 (weak) and 0.37 or more (clear). 0.3 sits in that gap.	|