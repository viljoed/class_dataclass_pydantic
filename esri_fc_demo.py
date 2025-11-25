"""water_stn.json created by saving response from this URL:
https://maps-cartes.ec.gc.ca/arcgis/rest/services/CESI_FGP_All_Layers/MapServer/6
"""
import json
from esri_fc import Model, Feature

with open("water_stn.json") as f:
    data = json.load(f)

model = Model.model_validate(data)
features: list[Feature] = model.features
for i, feature in enumerate(features, start=1):
    print(f"Feature #{i}")
    print(f"  Station Name: {feature.attributes.Station_Name}")
    print(f"  Coordinates: ({feature.geometry.x}, {feature.geometry.y})")
    print()
    break
