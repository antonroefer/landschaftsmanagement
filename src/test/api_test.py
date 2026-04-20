from io import BytesIO

import numpy as np
import matplotlib.pyplot as plt
import requests
from PIL import Image


def load_preview(item):
    thumbnail_url = item["assets"]["thumbnail"]["href"]
    response = requests.get(thumbnail_url, timeout=30)
    response.raise_for_status()

    rgb = np.asarray(Image.open(BytesIO(response.content)).convert("RGB"), dtype=float)
    rgb = rgb / 255.0
    return np.clip(rgb, 0, 1)


url = "https://catalogue.dataspace.copernicus.eu/stac/search"

query = {
    "collections": ["sentinel-2-l2a"],
    "bbox": [11.5, 50.8, 11.7, 50.95],
    "datetime": "2024-06-01T00:00:00Z/2024-06-10T23:59:59Z",
    "limit": 1,
}

response = requests.post(url, json=query, timeout=30)
response.raise_for_status()

data = response.json()

if not data.get("features"):
    raise ValueError("No Sentinel-2 items found for the selected query.")

item = data["features"][0]

rgb = load_preview(item)

plt.imshow(rgb)
plt.axis("off")
plt.title(item["id"])
plt.show()
