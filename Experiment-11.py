import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 4), columns=['Col1', 'Col2', 'Col3', 'Col4'])

df.iloc[1, 0] = np.nan
df.iloc[3, 2] = np.nan
df.iloc[5, 1] = np.nan
df.iloc[8, 3] = np.nan

styled_df = df.style.highlight_null(color='yellow')

styled_df.to_html('nan_highlight.html')
print("File generated: nan_highlight.html")