from PIL import Image, ImageOps
from diffusers import StableDiffusionInpaintPipeline
import argparse
import torch
import numpy as np

def generate_image_with_object(image_path, text_prompt, output_path):
    astronaut_image = Image.open(image_path).convert("RGBA")
    
    mask = ImageOps.invert(astronaut_image.getchannel("A")) 
    img_rgb = astronaut_image.convert("RGB")
    
    model = StableDiffusionInpaintPipeline.from_pretrained("stabilityai/stable-diffusion-2-inpainting") #, torch_dtype=torch.float16
    model = model.to("cpu")  #cuda didn't work
    
    result = model(prompt=text_prompt, image=img_rgb, mask_image=mask)
    
    generated_image = result.images[0]
    generated_image.save(output_path)
    print(f"Image successfully saved at: {output_path}")
    


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--image', type=str, required=True)
    parser.add_argument('--text-prompt', type=str, required=True)
    parser.add_argument('--output', type=str, required=True)
    
    args = parser.parse_args()
    
    generate_image_with_object(args.image, args.text_prompt, args.output)







