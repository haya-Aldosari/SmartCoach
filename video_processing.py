# -*- coding: utf-8 -*-
"""video_processing.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ZOgYGxCrGAVo5CYX0H0a4iStD-Mou2k_

--------------------------------------------------------
# SmartCoach - Video Processing for Emotion Extraction

Extracts frames from video, uses trained ResNet18 model to classify emotions, and saves the results as a JSON sequence.

--------------------------------------------------------
"""

import cv2
import torch
from torchvision import models, transforms
from PIL import Image
import json

import os
print(os.listdir('/content'))

"""# Step 1: Load pretrained emotion model (ResNet18)
--------------------------------------------------------
We load the fine-tuned model trained on emotion-labeled player images to perform frame-level emotion prediction.

"""

model = models.resnet18(weights=None)
model.fc = torch.nn.Linear(model.fc.in_features, 8)  # 8 emotion classes
model.load_state_dict(torch.load('/content/emotion_model.pth', map_location=torch.device('cpu')))
model.eval()  # Set model to inference mode

"""# Step 2: Define transformation to match training phase
--------------------------------------------------------
Ensures input frames are resized and normalized in the same way the model was trained, maintaining consistency.

"""

transform = transforms.Compose([
    transforms.Resize((224, 224)),  # Resize to ResNet input
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225])
])

"""# Step 3: Prepare video for frame extraction
--------------------------------------------------------
OpenCV is used to access and iterate through the video frames efficiently, setting a frame sampling rate to reduce overhead.

"""

video_path = '/content/[The name of the video here].mp4'
cap = cv2.VideoCapture(video_path)

frame_rate = 10     # Analyze one frame every 10 frames
frame_count = 0

# Map class indices to emotion names
emotion_map = ['Anger', 'Focus', 'Frustration', 'Happiness', 'Neutral', 'Stress', 'Surprise', 'Unclear']
results = []

"""# Step 4: Process video frame-by-frame
 --------------------------------------------------------
 For every sampled frame, we apply preprocessing, run inference using the model, and extract the predicted emotion along with the timestamp.

"""

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Process every Nth frame only
    if frame_count % frame_rate == 0:
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img_pil = Image.fromarray(img)
        input_tensor = transform(img_pil).unsqueeze(0)

        with torch.no_grad():
            output = model(input_tensor)
            pred = torch.argmax(output, dim=1).item()
            timestamp = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000.0
            results.append({
                "time": f"{timestamp:.2f}",
                "emotion": emotion_map[pred]
            })

    frame_count += 1

cap.release()

"""# Step 5: Save results to JSON file
--------------------------------------------------------
Emotions and timestamps are saved in JSON format, which is lightweight, human-readable, and ideal for integration with reporting tools or LLMs.

"""

with open("emotions.json", "w") as f:
    json.dump(results, f, indent=2)

print("✅ Analysis complete. Results saved to 'emotions.json'")