from PIL import Image

def apply_grayscale(image: Image.Image) -> Image.Image:
    """
    Converts a PIL image to grayscale.
    Args:
        image (PIL.Image.Image): Input image.
    Returns:
        PIL.Image.Image: Grayscale image.
    """
    return image.convert("L")