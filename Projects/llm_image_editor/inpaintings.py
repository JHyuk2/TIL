from diffusers import DiffusionPipeline
import torch
from PIL import Image

def load_inpainting_pipeline():
    """
    Load the Stable Diffusion Inpainting pipeline.
    Returns:
        Pipeline: the loaded inpainting pipeline.
    """
    pipe = DiffusionPipeline.from_pretrained(
        "alimama-creative/FLUX.1-dev-Controlnet-Inpainting-Beta",
        torch_dtype=torch.float16,
        revision="fp16"
    )
    # Use GPU if available, otherwise CPU
    pipe.to("cuda" if torch.cuda_is_available() else "cpu")
    return pipe

def run_inpainting(pipe, image: Image.Image, mask: Image.Image, prompt: str):
    """
    Run inpainting on the given image and mask with the provided prompt.
    Args:
        pipe: the inpainting pipeline.
        image: the original image (PIL format).
        mask: the mask image (PIL format, white areas to fill).
        prompt: the textual prompt for the inpainting model.
    Returns:
        Image.Image: the inpainted image.
    """
    result = pipe(
        prompt=prompt,
        image=image,
        mask_image=mask
    ).images[0]
    return result