from PIL import Image

img_path = r"c:\Users\KHAC THUONG\Downloads\Worklog-AWS\static\images\avarta.jpg"
img = Image.open(img_path)

width, height = img.size
print(f"Kích thước gốc: {width}x{height}")

# Center crop - lấy phần giữa hình
size = min(width, height)
left = (width - size) // 2
top = (height - size) // 2
right = left + size
bottom = top + size

cropped = img.crop((left, top, right, bottom))

# Resize thành 300x300
cropped_resized = cropped.resize((300, 300), Image.Resampling.LANCZOS)

# Save
cropped_resized.save(img_path, quality=85)
print("✓ Hình đã crop center và resize thành 300x300px")
