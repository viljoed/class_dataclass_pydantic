## Comparing class, @dataclass, and Pydantic class(BaseModel)
| Feature               | Regular Class | `@dataclass` | Pydantic Model    |
| --------------------- | ------------- | ------------ | ----------------- |
| Built-in Type Hints   | ✅            | ✅            | ✅                 |
| Boilerplate Reduction | ❌            | ✅            | ✅                 |
| Type Coercion (e.g., str→float) | ❌             | ❌                              | ✅                   |
| Runtime Type Checking | ❌            | ❌            | ✅                 |
| Custom Validation     | ❌            | Limited      | ✅ (`@field_validator`)  |
| Auto Serialization    | ❌            | ❌            | ✅ (`.json()`)     |
| Error Messages           | ❌             | ❌                              | ✅                   |
| Standard Library      | ✅            | ✅            | ❌ (pip install) |


## Generate Pydantic Model from water_stn.json
```bash
datamodel-codegen --input water_stn.json --input-file-type json --output esri_fc.py
```

esri_fc_demo.py uses esri_fc.Model to parse water_stn.json into Pydantic objects and shows the first feature's name and coords.

Copy contents of esri_fc.py into ChatGPT to convert to Mermaid code.  Save as esri_fc.md.