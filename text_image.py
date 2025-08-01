import os
import requests
from openai import OpenAI

print("🧠 Welcome to the AI Text-to-Image Converter!")
print("This tool uses OpenAI's DALL·E to generate images from text.\n")

# 🔐 Step 1: Ask for API Key
api_key = input("👉 Paste your OpenAI API key: ").strip()
if not api_key:
    print("❌ API key is required.")
    exit()

client = OpenAI(api_key=api_key)

# 🖋 Step 2: Ask for prompt
prompt = input("\n🖊 Describe what image you'd like to generate:\n👉 ").strip()
if not prompt:
    print("❌ Prompt is required.")
    exit()

# 🖼 Step 3: Ask for image size
print("\n📏 Choose image size:")
print("1. Square (1024x1024)")
print("2. Portrait (1024x1792)")
print("3. Landscape (1792x1024)")
size_choice = input("👉 Enter 1, 2, or 3: ").strip()
size_map = {
    "1": "1024x1024",
    "2": "1024x1792",
    "3": "1792x1024"
}
size = size_map.get(size_choice, "1024x1024")


# ⚙ Step 4: Generate image
print("\n⏳ Generating image... Please wait.\n")

try:
    response = client.images.generate(
        model="dall-e-3",  # Or "dall-e-2" if you don't have GPT-4 API access
        prompt=prompt,
        size=size,
        quality="standard",
        n=1,
    )

    image_url = response.data[0].url
    filename = prompt.replace(" ", "_")[:40] + ".png"

    # 💾 Download the image
    image_data = requests.get(image_url).content
    with open(filename, 'wb') as f:
        f.write(image_data)

    print(f"✅ Image saved as: {filename}")
    print(f"🌐 Image URL: {image_url}")

except Exception as e:
    print(f"\n❌ An error occurred: {e}")
