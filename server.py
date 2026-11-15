import os
import sys
import json
import base64
import random
import math
import io
import webbrowser
import threading
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from urllib.parse import parse_qs, urlparse
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops

PORT = 8088
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FONTS_DIR = os.path.join(BASE_DIR, 'fonts')
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')
DEFAULT_NOTEBOOK = os.path.join(ASSETS_DIR, 'notebook_thanhnam_spread.jpg')

# Calibrated line baselines for the default notebook (768 x 1024)
# In lined notebooks, writing sits on line[i+1] (the line underneath the text slot)
NOTEBOOK_LINES = [
    99, 126, 152, 178, 205, 231, 257, 284, 310, 335, 361, 387, 414, 441, 467, 494, 
    521, 549, 577, 604, 632, 660, 687, 715, 743, 771, 799, 828, 856, 885, 914, 943, 973
]
DEFAULT_BASELINES = NOTEBOOK_LINES[1:]  # 32 writing lines, first line sits on y=126


class HandwritingServerHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE_DIR, **kwargs)

    def end_headers(self):
        # Enable CORS and caching rules
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_POST(self):
        parsed = urlparse(self.path)
        if parsed.path == '/api/render_pillow':
            self.handle_render_pillow()
        elif parsed.path == '/api/upload_notebook':
            self.handle_upload_notebook()
        else:
            self.send_error(404, "Endpoint not found")

    def handle_render_pillow(self):
        try:
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length)
            data = json.loads(body.decode('utf-8'))

            text = data.get('text', '')
            font_choice = data.get('font', 'JasonHandwriting3.ttf')
            font_size = int(data.get('font_size', 22))
            messiness = float(data.get('messiness', 50)) / 100.0  # 0.0 to 1.0
            ink_color = data.get('ink_color', 'black')  # 'black', 'blue', 'deep_black'
            baseline_offset = int(data.get('baseline_offset', -3))
            left_margin_base = int(data.get('left_margin', 114))
            right_margin = int(data.get('right_margin', 672))
            seed = int(data.get('seed', 42))
            page_index = int(data.get('page_index', 0))
            skip_line = bool(data.get('skip_line', False))

            # Select font file with safe fallback
            font_file = os.path.join(FONTS_DIR, font_choice)
            if not os.path.exists(font_file) or 'ChenYuluoyan' in font_choice:
                font_file = os.path.join(FONTS_DIR, 'JasonHandwriting3.ttf')
            font = ImageFont.truetype(font_file, font_size)

            # Load notebook image
            custom_bg = data.get('custom_bg', None)
            notebook_choice = data.get('notebook_template', 'notebook_thanhnam_spread.jpg')
            if custom_bg and os.path.exists(os.path.join(ASSETS_DIR, custom_bg)):
                bg_path = os.path.join(ASSETS_DIR, custom_bg)
            elif notebook_choice and os.path.exists(os.path.join(ASSETS_DIR, notebook_choice)):
                bg_path = os.path.join(ASSETS_DIR, notebook_choice)
            else:
                bg_path = DEFAULT_NOTEBOOK

            bg = Image.open(bg_path).convert('RGB')
            w, h = bg.size

            # Ink color palette
            if ink_color == 'blue':
                base_r, base_g, base_b = 22, 55, 110
            elif ink_color == 'deep_black':
                base_r, base_g, base_b = 8, 8, 12
            else:  # Gel black
                base_r, base_g, base_b = 20, 22, 28

            # Split text into pages
            lines_per_page = len(DEFAULT_BASELINES)
            all_lines = self.wrap_text_for_notebook(
                text, font, left_margin_base, right_margin, font_size
            )

            # Insert blank lines if skip_line mode is enabled
            if skip_line:
                spaced_lines = []
                for l in all_lines:
                    spaced_lines.append(l)
                    spaced_lines.append({'is_paragraph_start': False, 'chars': []})
                all_lines = spaced_lines

            total_pages = max(1, math.ceil(len(all_lines) / lines_per_page))
            page_index = min(page_index, total_pages - 1)
            page_lines = all_lines[page_index * lines_per_page : (page_index + 1) * lines_per_page]

            # Render handwriting onto ink layer
            ink_layer = Image.new('RGBA', (w, h), (0, 0, 0, 0))
            rng = random.Random(seed + page_index * 997)

            for line_idx, line_chars in enumerate(page_lines):
                if line_idx >= len(DEFAULT_BASELINES):
                    break
                base_y = DEFAULT_BASELINES[line_idx] + baseline_offset
                is_paragraph_start = line_chars.get('is_paragraph_start', False)
                chars = line_chars.get('chars', [])

                cur_x = left_margin_base + (32 if is_paragraph_start else 0)
                cur_x += rng.uniform(-2, 2) * messiness

                # Slight hand slant / drift across the line
                drift_amp = rng.uniform(-2.5, 2.5) * messiness
                slope = rng.uniform(-1.0, 1.0) * messiness

                for ch_info in chars:
                    ch = ch_info['char']
                    progress = min(1.0, max(0.0, (cur_x - left_margin_base) / (right_margin - left_margin_base)))
                    drift = math.sin(progress * math.pi) * drift_amp + (progress - 0.5) * slope

                    # Character jitter
                    jitter_x = rng.uniform(-1.2, 1.2) * messiness
                    jitter_y = rng.uniform(-2.2, 2.0) * messiness
                    angle = rng.uniform(-4.5, 4.5) * messiness
                    scale_mult = 1.0 + rng.uniform(-0.08, 0.08) * messiness

                    # Dynamic ink pressure
                    r = int(base_r + rng.randint(-3, 6))
                    g = int(base_g + rng.randint(-3, 6))
                    b = int(base_b + rng.randint(-3, 8))
                    alpha = int(rng.randint(220, 248))

                    # Render single character with rotation
                    box_size = int(font_size * 2.2)
                    char_canvas = Image.new('RGBA', (box_size, box_size), (0, 0, 0, 0))
                    char_draw = ImageDraw.Draw(char_canvas)

                    # Draw character centered
                    char_draw.text(
                        (box_size // 4, box_size // 4),
                        ch,
                        font=font,
                        fill=(r, g, b, alpha)
                    )

                    # Rotate & Scale
                    rotated = char_canvas.rotate(angle, resample=Image.BICUBIC)
                    if abs(scale_mult - 1.0) > 0.02:
                        new_w = max(10, int(box_size * scale_mult))
                        new_h = max(10, int(box_size * scale_mult))
                        rotated = rotated.resize((new_w, new_h), resample=Image.BILINEAR)
                        box_size = new_w

                    target_x = int(cur_x + jitter_x - box_size // 4)
                    target_y = int(base_y - font_size + jitter_y + drift - box_size // 8)

                    ink_layer.alpha_composite(rotated, (target_x, target_y))
                    
                    # Horizontal advance
                    if ch in '，。、；：':
                        step = font_size * 0.75 + rng.uniform(-1, 1) * messiness
                    elif ch in '「」『』()':
                        step = font_size * 0.65 + rng.uniform(-1, 1) * messiness
                    else:
                        step = font_size * 0.95 + rng.uniform(-1.5, 1.5) * messiness
                    cur_x += step

            # Gel pen ink softness (micro-bleed into paper fibers)
            if messiness > 0.1:
                ink_layer = ink_layer.filter(ImageFilter.GaussianBlur(radius=0.25))

            # Multiply blend mode with paper texture
            white_bg = Image.new('RGB', bg.size, (255, 255, 255))
            white_bg.paste(ink_layer, mask=ink_layer.split()[3])
            blended = ImageChops.multiply(bg, white_bg)

            # Export to JPEG bytes
            buf = io.BytesIO()
            blended.save(buf, format='JPEG', quality=95)
            buf.seek(0)
            img_b64 = base64.b64encode(buf.getvalue()).decode('utf-8')

            resp = {
                'success': True,
                'image': f'data:image/jpeg;base64,{img_b64}',
                'total_pages': total_pages,
                'page_index': page_index,
                'total_lines': len(all_lines)
            }
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(json.dumps(resp).encode('utf-8'))

        except Exception as e:
            self.send_response(500)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(json.dumps({'success': False, 'error': str(e)}).encode('utf-8'))

    def wrap_text_for_notebook(self, text, font, left_margin, right_margin, font_size):
        """Word/character wrap with full-width Chinese punctuation logic"""
        # Normalize half-width punctuation
        punc_map = {
            ',': '，', '.': '。', ':': '：', ';': '；', '!': '！', '?': '？',
            '(': '（', ')': '）', '[': '【', ']': '】'
        }
        text = ''.join(punc_map.get(c, c) for c in text)

        max_width = right_margin - left_margin
        lines = []
        paragraphs = text.split('\n')

        punctuation_no_start = set('，。、；：！？）》」』”’')

        for p_idx, paragraph in enumerate(paragraphs):
            p_clean = paragraph.strip()
            if not p_clean:
                lines.append({'is_paragraph_start': True, 'chars': []})
                continue

            current_line_chars = []
            cur_w = 32  # 2 characters indent for paragraph start
            is_start = True

            for ch in p_clean:
                if ch in '，。、；：':
                    char_w = font_size * 0.75
                elif ch in '「」『』()':
                    char_w = font_size * 0.65
                else:
                    char_w = font_size * 0.95

                if cur_w + char_w > max_width:
                    # Check hanging punctuation rule
                    if ch in punctuation_no_start and len(current_line_chars) > 0:
                        # Hang punctuation at end of current line
                        current_line_chars.append({'char': ch})
                        lines.append({'is_paragraph_start': is_start, 'chars': current_line_chars})
                        current_line_chars = []
                        cur_w = 0
                        is_start = False
                        continue

                    lines.append({'is_paragraph_start': is_start, 'chars': current_line_chars})
                    current_line_chars = []
                    cur_w = 0
                    is_start = False

                current_line_chars.append({'char': ch})
                cur_w += char_w

            if current_line_chars:
                lines.append({'is_paragraph_start': is_start, 'chars': current_line_chars})

        return lines

    def handle_upload_notebook(self):
        try:
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length)
            data = json.loads(body.decode('utf-8'))

            image_data = data.get('image', '')
            if ',' in image_data:
                image_data = image_data.split(',', 1)[1]
            raw_bytes = base64.b64decode(image_data)

            filename = f"custom_notebook_{int(random.random() * 100000)}.jpg"
            save_path = os.path.join(ASSETS_DIR, filename)

            img = Image.open(io.BytesIO(raw_bytes)).convert('RGB')
            # Resize if too large for web performance
            if img.width > 1200 or img.height > 1600:
                img.thumbnail((1200, 1600), Image.Resampling.LANCZOS)
            img.save(save_path, quality=95)

            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'success': True, 'filename': filename}).encode('utf-8'))
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'success': False, 'error': str(e)}).encode('utf-8'))


def run_server():
    server_address = ('', PORT)
    httpd = ThreadingHTTPServer(server_address, HandwritingServerHandler)
    url = f"http://localhost:{PORT}"
    print(f"=====================================================")
    print(f"  App Chép Tay Tiếng Trung Phồn Thể Đã Sẵn Sàng!")
    print(f"  Mở trình duyệt tại: {url}")
    print(f"=====================================================")

    # Open browser after 1 second
    threading.Timer(1.0, lambda: webbrowser.open(url)).start()

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nĐang dừng server...")
        httpd.server_close()


if __name__ == '__main__':
    run_server()
