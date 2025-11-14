"""water_stn.json created by saving response from this URL:
https://maps-cartes.ec.gc.ca/arcgis/rest/services/CESI_FGP_All_Layers/MapServer/6
"""
import json
from pathlib import Path
from esri_fc import Model, Feature

with Path("water_stn.json").open("r", encoding="utf-8") as f:
    data = json.load(f)

model = Model.model_validate(data)

# 3. Extract the list of features (each is a Pydantic Feature instance)
features: list[Feature] = model.features

# 4. Example: print some data from each feature
for i, feature in enumerate(features, start=1):
    print(f"Feature #{i}")
    print(f"  Station Name: {feature.attributes.Station_Name}")
    print(f"  Coordinates: ({feature.geometry.x}, {feature.geometry.y})")
    print()
    break
