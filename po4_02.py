import quandl
import pandas as pd

api_key = "Cxe41MDVyJhXQYGuVGx7"

df = quandl.get("FMAC/HPI_AK", authtoken=api_key)

fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')

print(fiddy_states[0][0])
