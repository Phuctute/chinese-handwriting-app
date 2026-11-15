import os
import random
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

base_assets = r'C:\Users\phucv\.gemini\antigravity\scratch\chinese-handwriting-app\assets'

def create_paper_texture(w, h, base_color=(252, 250, 245), noise_intensity=3):
    im = Image.new('RGB', (w, h), base_color)
    pix = im.load()
    br, bg, bb = base_color
    for y in range(h):
        for x in range(w):
            dx = (x - w/2) / (w/2)
            dy = (y - h/2) / (h/2)
            dist_sq = dx*dx + dy*dy
            vig = int(dist_sq * 5)
            noise = random.randint(-noise_intensity, noise_intensity)
            pix[x, y] = (
                max(0, min(255, br - vig + noise)),
                max(0, min(255, bg - vig + noise)),
                max(0, min(255, bb - vig + noise))
            )
    return im

def add_3d_spine_lighting(im):
    w, h = im.size
    mid_x = w // 2 # 512
    pix = im.load()
    
    # 3D curvature shading near center crease (x = 512)
    # Gáy sách uốn cong: bóng tối sâu nhất tại x=512, tỏa rộng 70px sang hai bên
    for y in range(h):
        for x in range(mid_x - 75, mid_x + 76):
            dist = abs(x - mid_x)
            # Smooth cosine curve
            t = dist / 75.0 # 0 at center, 1 at edge
            shadow_strength = math.cos(t * math.pi * 0.5) ** 1.8
            darken = int(shadow_strength * 48)
            
            # Subtle highlight on left & right slopes where page arches up
            arch_highlight = 0
            if 30 <= dist <= 65:
                arch_highlight = int(math.sin((dist - 30) / 35.0 * math.pi) * 8)
            
            r, g, b = pix[x, y]
            pix[x, y] = (
                max(0, min(255, r - darken + arch_highlight)),
                max(0, min(255, g - darken + arch_highlight)),
                max(0, min(255, b - darken + arch_highlight))
            )
            
        # Subtle outer edge vignette (page edges)
        for x in range(0, 20):
            edge_dark = int((1.0 - x / 20.0) * 14)
            r, g, b = pix[x, y]
            pix[x, y] = (max(0, r - edge_dark), max(0, g - edge_dark), max(0, b - edge_dark))
            
        for x in range(w - 20, w):
            edge_dark = int((x - (w - 20)) / 20.0 * 14)
            r, g, b = pix[x, y]
            pix[x, y] = (max(0, r - edge_dark), max(0, g - edge_dark), max(0, b - edge_dark))
            
    return im

def draw_weather_icons(draw, x_start, y_center):
    # Draw simple elegant sun, cloud, rain
    # 1. Sun
    sx, sy = x_start, y_center
    draw.ellipse([sx-5, sy-5, sx+5, sy+5], outline=(140, 165, 200), width=1)
    for a in range(0, 360, 45):
        rad = math.radians(a)
        x1 = sx + math.cos(rad) * 7
        y1 = sy + math.sin(rad) * 7
        x2 = sx + math.cos(rad) * 10
        y2 = sy + math.sin(rad) * 10
        draw.line([(x1, y1), (x2, y2)], fill=(150, 175, 210), width=1)
        
    # 2. Cloud
    cx, cy = sx + 22, y_center
    draw.ellipse([cx-7, cy-3, cx-1, cy+4], outline=(140, 165, 200), width=1)
    draw.ellipse([cx-3, cy-6, cx+4, cy+3], outline=(140, 165, 200), width=1)
    draw.ellipse([cx+1, cy-2, cx+7, cy+4], outline=(140, 165, 200), width=1)
    draw.line([(cx-6, cy+4), (cx+6, cy+4)], fill=(140, 165, 200), width=1)
    
    # 3. Rain droplets
    rx, ry = cx + 22, y_center
    draw.line([(rx-4, ry-1), (rx-6, ry+4)], fill=(140, 165, 200), width=1)
    draw.line([(rx, ry-2), (rx-2, ry+3)], fill=(140, 165, 200), width=1)
    draw.line([(rx+4, ry-1), (rx+2, ry+4)], fill=(140, 165, 200), width=1)

def build_3d_spread(brand='hongha', paper_theme='standard'):
    w, h = 1024, 768
    
    if paper_theme == 'warm':
        base_color = (250, 245, 235) # Vintage ấm áp
        line_color = (130, 160, 200, 160)
        margin_color = (210, 110, 110, 180)
    elif paper_theme == 'soft':
        base_color = (248, 249, 246) # Dịu mắt
        line_color = (135, 165, 205, 150)
        margin_color = (215, 115, 115, 175)
    elif paper_theme == 'clean':
        base_color = (254, 254, 253) # Trắng sáng tinh khôi
        line_color = (130, 170, 220, 165)
        margin_color = (225, 95, 95, 185)
    else: # standard
        base_color = (252, 250, 245)
        line_color = (135, 165, 210, 160)
        margin_color = (220, 105, 105, 180)
        
    im = create_paper_texture(w, h, base_color=base_color, noise_intensity=2)
    im = add_3d_spine_lighting(im)
    
    # Draw ruled lines on transparent overlay for smooth alpha blending
    overlay = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    TN_AI_SPREAD = [65, 86, 107, 128, 149, 170, 191, 212, 233, 254, 275, 296, 317, 338, 359, 380, 401, 422, 443, 464, 485, 506, 527, 548, 569, 590, 611, 632, 653, 674, 695]
    
    # Draw 31 Ruled Lines on both Left and Right pages
    for y in TN_AI_SPREAD:
        # Left page: x=45 to 475
        draw.line([(45, y), (475, y)], fill=line_color, width=1)
        # Right page: x=550 to 980
        draw.line([(550, y), (980, y)], fill=line_color, width=1)
        
    # Red Margin Lines
    if brand == 'thanhnam':
        # Left page margin at x=85
        draw.line([(85, 50), (85, 715)], fill=margin_color, width=1)
        # Right page margin at x=582
        draw.line([(582, 50), (582, 715)], fill=margin_color, width=1)
        
        # Header text
        draw.text((45, 34), "Date: ...................... No: .....", fill=(210, 130, 130, 170))
        draw.text((820, 34), "Date: ...................... No: .....", fill=(210, 130, 130, 170))
        
        # Footers
        draw.text((85, 725), "Thành Nam Paper Co.", fill=(160, 160, 170, 150))
        draw.text((860, 725), "Thành Nam Paper Co.", fill=(160, 160, 170, 150))
    else: # hongha
        # Hong Ha margin at x=85 & x=582
        draw.line([(85, 50), (85, 715)], fill=(130, 160, 205, 170), width=1)
        draw.line([(582, 50), (582, 715)], fill=(130, 160, 205, 170), width=1)
        
        # Weather icons on left page
        draw_weather_icons(draw, 55, 38)
        draw.text((310, 32), "Thứ ....... ngày .......", fill=(140, 160, 190, 180))
        
        # Weather icons on right page
        draw_weather_icons(draw, 560, 38)
        draw.text((815, 32), "Thứ ....... ngày .......", fill=(140, 160, 190, 180))
        
        # Hong Ha logo footer
        draw.text((85, 725), "HỒNG HÀ", fill=(130, 160, 205, 170))
        draw.text((890, 725), "HỒNG HÀ", fill=(130, 160, 205, 170))
        
    # Merge overlay
    im.paste(overlay, (0, 0), overlay)
    return im

print('Generating 6 high-precision 3D spreads...')

# 1. Hong Ha Standard Spread
im_hh_std = build_3d_spread(brand='hongha', paper_theme='standard')
im_hh_std.save(os.path.join(base_assets, 'notebook_hongha_spread.jpg'), quality=96)
im_hh_std.save(os.path.join(base_assets, 'notebook_hongha_ai_spread.jpg'), quality=96)

# 2. Hong Ha Soft Spread
im_hh_soft = build_3d_spread(brand='hongha', paper_theme='soft')
im_hh_soft.save(os.path.join(base_assets, 'notebook_hongha_spread_soft.jpg'), quality=96)

# 3. Hong Ha Warm Spread
im_hh_warm = build_3d_spread(brand='hongha', paper_theme='warm')
im_hh_warm.save(os.path.join(base_assets, 'notebook_hongha_spread_warm.jpg'), quality=96)

# 4. Thanh Nam Standard Spread
im_tn_std = build_3d_spread(brand='thanhnam', paper_theme='standard')
im_tn_std.save(os.path.join(base_assets, 'notebook_thanhnam_spread.jpg'), quality=96)
im_tn_std.save(os.path.join(base_assets, 'notebook_thanhnam_ai_spread.jpg'), quality=96)

# 5. Thanh Nam Clean Spread
im_tn_clean = build_3d_spread(brand='thanhnam', paper_theme='clean')
im_tn_clean.save(os.path.join(base_assets, 'notebook_thanhnam_spread_clean.jpg'), quality=96)

# 6. Thanh Nam Warm Spread
im_tn_warm = build_3d_spread(brand='thanhnam', paper_theme='warm')
im_tn_warm.save(os.path.join(base_assets, 'notebook_thanhnam_spread_warm.jpg'), quality=96)

print('All 6 spreads generated successfully!')
