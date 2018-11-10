###############################################################################
###  Pandas Tutorials - Lesson 10                                           ###
###############################################################################

import pandas as pd

# Convert between DataFrame and Excel #########################################
d = [1,2,3,4,5,6,7,8,9]
df = pd.DataFrame(d, columns=['Number'])

df.to_excel(".\\Lessons\\Lesson10.xlsx", sheet_name='testing', index=False)
df = pd.read_excel(".\\Lessons\\Lesson10.xlsx", 0)

# Convert between DataFrame and JSON ##########################################
df.to_json(".\\Lessons\\Lesson10.json")
df = pd.read_json(".\\Lessons\\Lesson10.json")

