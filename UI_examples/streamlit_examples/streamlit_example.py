import streamlit as st
import pydeck as pdk
import io
import geopandas as gpd
import requests
from ipywidgets import HTML
import pandas as pd

DATA_URL = 'https://api.data.gov.sg/v1/transport/taxi-availability'
COLOR_RANGE = [
  [255, 255, 178, 25],
  [254, 217, 118, 85],
  [254, 178, 76, 127],
  [253, 141, 60, 170],
  [240, 59, 32, 212],
  [189, 0, 38, 255]
]


json = requests.get(DATA_URL).json()
df = pd.DataFrame(json["features"][0]["geometry"]["coordinates"])
df.columns = ['lng', 'lat']

text = HTML(value='Move the viewport')
layer = pdk.Layer(
    'ScatterplotLayer',
    df,
    pickable=True,
    get_position=['lng', 'lat'],
    get_fill_color=[255, 0, 0],
    get_radius=100
)
viewport = pdk.data_utils.compute_view(df[['lng', 'lat']])
r = pdk.Deck(layer, initial_view_state=viewport)

def filter_by_bbox(row, west_lng, east_lng, north_lat, south_lat):
    return west_lng < row['lng'] < east_lng and south_lat < row['lat'] < north_lat

def filter_by_viewport(widget_instance, payload):
    try:
        west_lng, north_lat = payload['data']['nw']
        east_lng, south_lat = payload['data']['se']
        filtered_df = df[df.apply(lambda row: filter_by_bbox(row, west_lng, east_lng, north_lat, south_lat), axis=1)]
        text.value = 'Points in viewport: %s' % int(filtered_df.count()['lng'])
    except Exception as e:
        text.value = 'Error: %s' % e

r.deck_widget.on_view_state_change(filter_by_viewport)

if __name__ == '__main__':
    st.title("Map test")
    subhead = st.text("Subheader")
    st.pydeck_chart(r)
