import pandas as pd
import numpy as np

np.random.seed(42)
data = np.random.randn(10, 4)
df = pd.DataFrame(data, columns=['B', 'C', 'D', 'E'])
df.insert(0, 'A', range(1, 11))

def color_negative_red(val):
    if isinstance(val, (int, float)) and val < 0:
        return 'color: red'
    return 'color: black'

styled_df = df.style.map(color_negative_red).format(precision=6)

styled_df.to_html('table_output.html')
print("File generated: table_output.html")