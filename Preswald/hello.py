from preswald import connect, get_df, query, table, text, plotly
import plotly.express as px

connect() #Initialize connection to preswald.toml data sources
df = get_df("data/data.csv")

sql = "SELECT * FROM data/data.csv WHERE bedrooms != '3.0' AND sqft_living <= '1500'"
filtered_df = query(sql, "data/data.csv")

text("# My Data Analysis App")
table(filtered_df, title="Filtered Data")

fig = px.scatter(df, x="price", y ="bedrooms", color="view")
plotly(fig)


