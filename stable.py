from PIL import Image, ImageOps
from diffusers import StableDiffusionInpaintPipeline
import argparse
import torch
import numpy as np

def generate_image_with_object(image_path, text_prompt, output_path):
    object_image = Image.open(image_path).convert("RGBA")
    
    max_object_size = (150, 150)  #Fix size for input image
    object_image.thumbnail(max_object_size, Image.Resampling.LANCZOS)
    
    object_np = np.array(object_image)
    white_threshold = 240  #White bg

    mask_np = np.all(object_np[:, :, :3] > white_threshold, axis=-1)
    mask = Image.fromarray(np.uint8(~mask_np * 255), mode="L")
    
    canvas_size = (768, 768)  
    canvas = Image.new("RGBA", canvas_size, (255, 255, 255, 0))  #Transparent canvas
    
    
    object_position = (canvas_size[0] // 2 - object_image.size[0] // 2,  canvas_size[1] // 2 - object_image.size[1] // 2) #Image centring
    canvas.paste(object_image, object_position, object_image)  #Using input image object as mask
    

    canvas_rgb = canvas.convert("RGB")
    
    model = StableDiffusionInpaintPipeline.from_pretrained("stabilityai/stable-diffusion-2-inpainting")
    model = model.to("cpu")
    
    
    result = model(prompt=text_prompt, image=canvas_rgb, mask_image=mask) #Generating the image using the canvas and the mask with the text prompt as the background
    
    generated_image = result.images[0]
    generated_image.save(output_path)
    print(f"Image successfully saved at: {output_path}")


    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--image', type=str, required=True, help="Path to the object image")
    parser.add_argument('--text-prompt', type=str, required=True, help="Text prompt for the background scene")
    parser.add_argument('--output', type=str, required=True, help="Output path for the generated image")
    
    args = parser.parse_args()
    generate_image_with_object(args.image, args.text_prompt, args.output)


