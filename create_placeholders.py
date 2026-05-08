#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
import os

# Create directories
os.makedirs('assets/images/team', exist_ok=True)
os.makedirs('assets/images/blog', exist_ok=True)
os.makedirs('assets/images/gallery', exist_ok=True)
os.makedirs('assets/images/stories', exist_ok=True)
os.makedirs('assets/images/programs', exist_ok=True)

def create_placeholder(filename, width, height, text, color):
    """Create a placeholder image with text"""
    img = Image.new('RGB', (width, height), color=color)
    draw = ImageDraw.Draw(img)
    
    # Try to use a font, fall back to default if not available
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 40)
    except:
        font = ImageFont.load_default()
    
    # Get text bounding box
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    # Center text
    x = (width - text_width) // 2
    y = (height - text_height) // 2
    
    draw.text((x, y), text, fill='white', font=font)
    img.save(filename)
    print(f"Created: {filename}")

# Colors
green = (44, 95, 45)
light_green = (151, 191, 13)
orange = (247, 148, 29)
blue = (52, 152, 219)

# Hero image
create_placeholder('assets/images/hero-bg.jpg', 1920, 1080, 'AOHF Foundation', green)

# Team member photos
team_members = [
    'odusote-abdullahi', 'odusote-ahmad', 'yunus-sharafudeen',
    'sikirullah-tajudeen', 'sunmola-wasiu', 'olagoke-faruq',
    'asuni-jamiu', 'dr-abdulganiyu', 'balogun-muslim',
    'abdulganiyu-abdulsalam', 'abdulshakur-abdulsalam'
]

for member in team_members:
    create_placeholder(f'assets/images/team/{member}.jpg', 400, 400, 'Team\nMember', blue)

# Program images
programs = [
    'food-distribution', 'clean-water', 'education',
    'emergency-relief', 'healthcare', 'orphan-support', 'mosque-construction'
]

for program in programs:
    create_placeholder(f'assets/images/programs/{program}.jpg', 800, 600, program.replace('-', ' ').title(), green)

# Blog images
for i in range(1, 10):
    create_placeholder(f'assets/images/blog/blog-{i}.jpg', 800, 500, f'Blog Post {i}', orange)

create_placeholder('assets/images/blog/blog-post-featured.jpg', 1200, 600, 'Featured Post', orange)

# Gallery images
for i in range(1, 13):
    create_placeholder(f'assets/images/gallery/gallery-{i}.jpg', 600, 600, f'Gallery {i}', light_green)

# Success stories
for i in range(1, 7):
    create_placeholder(f'assets/images/stories/story-{i}.jpg', 800, 500, f'Success Story {i}', blue)

print("\n✅ All placeholder images created successfully!")
