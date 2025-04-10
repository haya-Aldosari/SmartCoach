# SmartCoach

SmartCoach is an AI-powered assistant designed to support sports coaches by analyzing athletes’ emotional and physical states.  
It combines computer vision, deep learning, and large language models to provide psychological insights based on facial expressions and behavior—bridging the gap between human emotion and tactical decisions.

---

## Features

- Emotion detection from images and video frames using a fine-tuned ResNet18
- Frame-by-frame video analysis with results saved in structured JSON format
- Psychological report generation powered by the Hermes-2 LLM
- Early-stage UI prototype built with Figma to simulate the full user journey
- Future scope includes real-time video stream analysis and biometric tracking

---

## Technologies Used

- Python, PyTorch, TorchVision – For training the emotion recognition model  
- OpenCV – For video input, frame extraction, and image processing  
- Hugging Face Transformers – To load Hermes-2-Pro for generating natural language evaluations  
- HTML + Figma – For designing a web interface (currently in progress)  
- FastAPI – Planned for backend integration and serving predictions

---

## Project Structure

| File                 | Description                                      |
|----------------------|--------------------------------------------------|
| `emotion_model.py`   | Trains the emotion recognition model             |
| `video_processing.py`| Extracts emotions frame-by-frame from videos     |
| `image_processing.py`| Processes individual athlete images              |
| `report_generator.py`| Generates natural language psychological reports |
| `labeled_faces.zip`  | Custom dataset used for training (8 emotions)    |

---

## Future Development

The current version assumes one athlete per video to validate the core concept. For improved accuracy and scalability, we aim to:

- Integrate player tracking (e.g., YOLO + DeepSort) to isolate the target player automatically  
- Incorporate physical performance analysis such as fatigue or performance drop detection  
- Overcome current limitations including access to biometric/sensor-based datasets  
- Connect the backend system to the UI prototype for a functional end-to-end flow  
- Prepare the system for real-time video stream integration during live matches

---

## Collaboration & Support

We are currently seeking:

- Access to biometric datasets (e.g., heart rate, fatigue indicators)  
- Guidance on player tracking frameworks for real-world sports videos  
- Compute resources (GPU) for real-time deployment

---

## Contact

For inquiries or collaboration opportunities:  
Email: hayafahad4ai@email.com  
