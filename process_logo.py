from PIL import Image
import sys

def process_logo(input_path, output_dir):
    try:
        # Open the generated image
        img = Image.open(input_path).convert("RGBA")
        
        # Make the white background transparent
        datas = img.getdata()
        newData = []
        for item in datas:
            # Change all white (also shades of whites)
            # to transparent
            if item[0] > 240 and item[1] > 240 and item[2] > 240:
                newData.append((255, 255, 255, 0))
            else:
                newData.append(item)
        
        img.putdata(newData)
        
        # Crop the image to its bounding box to remove extra transparent space
        bbox = img.getbbox()
        if bbox:
            img = img.crop(bbox)

        # Save the primary logo icon
        logo_path = f"{output_dir}/logo-icon.png"
        img.save(logo_path, "PNG")
        print(f"Saved primary logo to {logo_path}")

        # Create apple-touch-icon.png (180x180)
        max_size = 180
        ratio = min(max_size / img.width, max_size / img.height)
        new_size = (int(img.width * ratio), int(img.height * ratio))
        resized = img.resize(new_size, Image.Resampling.LANCZOS)
        
        # Paste into a square 180x180 transparent image
        apple_icon = Image.new("RGBA", (180, 180), (255, 255, 255, 0))
        offset = ((180 - new_size[0]) // 2, (180 - new_size[1]) // 2)
        apple_icon.paste(resized, offset)
        apple_icon.save(f"{output_dir}/apple-touch-icon.png", "PNG")
        print("Saved apple-touch-icon.png")

        # Create favicon-32x32.png
        fav32 = apple_icon.resize((32, 32), Image.Resampling.LANCZOS)
        fav32.save(f"{output_dir}/favicon-32x32.png", "PNG")
        print("Saved favicon-32x32.png")

        # Create favicon-16x16.png
        fav16 = apple_icon.resize((16, 16), Image.Resampling.LANCZOS)
        fav16.save(f"{output_dir}/favicon-16x16.png", "PNG")
        print("Saved favicon-16x16.png")

        # Create favicon.ico (multi-size)
        apple_icon.save(f"{output_dir}/favicon.ico", format="ICO", sizes=[(16, 16), (32, 32), (48, 48), (64, 64)])
        print("Saved favicon.ico")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 2:
        process_logo(sys.argv[1], sys.argv[2])
    else:
        print("Usage: python process_logo.py <input_path> <output_dir>")
