# 🖼️ Task 02 – Image Generation Using Pre-trained Models

This project demonstrates how to generate images from text prompts using a **pre-trained generative model**.  
For this task, we use **Stable Diffusion Turbo (SD-Turbo)** from Stability AI — a lightweight, fast model ideal for quick inference.

---

## 🚀 Features
- Uses **Stable Diffusion Turbo** (600MB, very fast)
- Works on **GPU** (recommended) and **CPU**
- Simple Python script for easy execution
- Saves generated images locally
- Colab-compatible and VS Code-compatible

---

## 📂 Project Files
| File | Description |
|------|-------------|
| `task2_image_generation.py` | Main Python script for generating images |
| `output.png` | Example generated image (created when you run the script) |
| `README.md` | Documentation for the project |

---

## 🛠️ Installation

Install the required dependencies:

```bash
pip install torch diffusers transformers accelerate safetensors

## How It Works
1. Loads a pre-trained Stable Diffusion SD-Turbo model
2. Accepts a text prompt from the user
3. Runs inference using GPU/CPU
4. Saves the generated image locally


