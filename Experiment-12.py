import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 4), columns=['Col1', 'Col2', 'Col3', 'Col4'])

def set_colors(val):
    return 'background-color: black; color: yellow'

styled_df = df.style.map(lambda x: 'background-color: black; color: yellow')

styled_df.to_html('colored_table.html')
print("File generated: colored_table.html")