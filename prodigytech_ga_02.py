# Task 02: Image Generation using Pre-trained Models (Stable Diffusion Turbo)
# This script runs on both CPU and GPU.

import torch
from diffusers import StableDiffusionPipeline

def main():
    # Check CUDA availability
    print("CUDA available:", torch.cuda.is_available())
    if torch.cuda.is_available():
        print("GPU name:", torch.cuda.get_device_name(0))

    # Load model
    model_id = "stabilityai/sd-turbo"
    dtype = torch.float16 if torch.cuda.is_available() else torch.float32

    print("Loading model...")
    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=dtype)

    # Move model to GPU if possible
    device = "cuda" if torch.cuda.is_available() else "cpu"
    pipe = pipe.to(device)

    # Prompt
    prompt = "a tiger"

    print("Generating image...")
    image = pipe(prompt, num_inference_steps=2).images[0]

    # Save
    output_file = "output.png"
    image.save(output_file)
    print(f"Image saved as {output_file}")

    return image


if __name__ == "__main__":
    main()
