#!/usr/bin/env python3
from PIL import Image

# Open the logo and convert to RGB
logo = Image.open('assets/images/logo.jpg')
if logo.mode != 'RGB':
    logo = logo.convert('RGB')

# Create favicon (32x32)
favicon = logo.resize((32, 32), Image.Resampling.LANCZOS)
favicon.save('assets/images/favicon.ico')

# Create apple touch icon (180x180)
apple_icon = logo.resize((180, 180), Image.Resampling.LANCZOS)
apple_icon.save('assets/images/apple-touch-icon.png')

# Create a 192x192 for Android
android_icon = logo.resize((192, 192), Image.Resampling.LANCZOS)
android_icon.save('assets/images/android-icon.png')

print('✅ Favicon and touch icons created')
