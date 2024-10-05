import google.generativeai as ai
import os

# Replace 'YOUR_API_KEY' with your actual Gemini API key
gemini_api_key = os.getenv("GEMINI_API_KEY")
ai.configure(api_key=gemini_api_key)


def generate_image(prompt):
    """Generates an image based on the given prompt.

    Args:
        prompt (str): The text description of the image to generate.

    Returns:
        google.generative_ai.ImageGenerationResult: The generated image result.
    """

    try:
        result = ai.generate_images(prompts=[prompt])
        return result
    except Exception as e:
        print(f"Error generating image: {e}")
        return None

# Example usage:
prompt = "A cat wearing a hat, sitting on a chair"
result = generate_image(prompt)

if result:
    # Save the image to a file
    image_path = "generated_image.png"
    result.images[0].save(image_path)
    print(f"Image saved to: {image_path}")
else:
    print("Image generation failed.")

