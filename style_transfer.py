import requests
import torch
from PIL import Image
from io import BytesIO
from diffusers import StableDiffusionImg2ImgPipeline

device = "cpu"
model_id_or_path = "digiplay/unstableDiffusersYamerMIX_v3"
pipe = StableDiffusionImg2ImgPipeline.from_pretrained(model_id_or_path)
pipe = pipe.to(device)

# Function to apply style transfer to the user-uploaded image
def apply_style_to_image(image_path, prompt, negative_prompt):
    init_image = Image.open(image_path).convert("RGB")
    init_image = init_image.resize((768, 512))
    
    pipe.safety_checker = None
    images = pipe(prompt=prompt, image=init_image, strength=0.5, guidance_scale=15, negetive_prompt=negative_prompt).images[0]
    
    return images

# Example usage
user_uploaded_file = "C:/Users/DND/style_changer/upload/example.jpg"  # Replace with the actual path
prompt = "dark skinned"
neg_prompt = "(deformed, distorted, disfigured:1.3), poorly drawn, bad anatomy, wrong anatomy, extra limb, missing limb, floating limbs, (mutated hands and fingers:1.4), disconnected limbs, mutation, mutated, ugly , disgusting, blurry, amputation, skinny, not facing camera, poorly drawn eyes"

styled_image = apply_style_to_image(user_uploaded_file, prompt, neg_prompt)
styled_image.show()  # You can save or display the styled image as needed
