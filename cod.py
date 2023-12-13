import torch

# Initialize the (small) network from ultralytics
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
# Load test image, could be any image
img = 'https://www.ugap.fr/images/media-wp/2023/10/Loupe_rfart_goupil_g4_3__488.jpg'
# Do inference
results = model(img)
# Show results
results.show()
