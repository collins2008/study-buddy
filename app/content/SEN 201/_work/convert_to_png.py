import os
from PIL import Image

def convert_images():
    base_dir = r'c:\Users\Collins Ibilibor\Downloads\Study Buddy\200 lvl\First Semester\SEN 201'
    past_dir = os.path.join(base_dir, 'past questions')
    out_dir = r'c:\Users\Collins Ibilibor\Downloads\Study Buddy\app\content\SEN 201\_work\png_images'
    os.makedirs(out_dir, exist_ok=True)

    images = [os.path.join(past_dir, f) for f in os.listdir(past_dir) if f.lower().endswith(('.jpeg', '.jpg', '.webp', '.png'))]
    extra = os.path.join(base_dir, 'WhatsApp Image 2026-11-17 at 21.47.00 (1).jpeg')
    if os.path.exists(extra):
        images.append(extra)

    converted = []
    for img_path in images:
        name = os.path.splitext(os.path.basename(img_path))[0]
        out_png = os.path.join(out_dir, name + '.png')
        img = Image.open(img_path)
        img.convert('RGB').save(out_png, 'PNG')
        converted.append(out_png)
        print(f"Converted {os.path.basename(img_path)} -> {os.path.basename(out_png)} ({img.size})")

    return converted

if __name__ == '__main__':
    convert_images()
