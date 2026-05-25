from PIL import Image

img_path = r"c:\Users\KHAC THUONG\Downloads\Worklog-AWS\static\images\avarta.jpg"
img = Image.open(img_path)

# Lấy kích thước gốc
width, height = img.size
print(f"Kích thước gốc: {width}x{height}")

# Cắt phần trên (top 65% của hình)
crop_height = int(height * 0.65)
crop_box = (0, 0, width, crop_height)
cropped = img.crop(crop_box)

# Resize thành 300x300
cropped_resized = cropped.resize((300, 300), Image.Resampling.LANCZOS)

# Save
cropped_resized.save(img_path, quality=85)
print("✓ Hình đã crop và resize thành 300x300px")
