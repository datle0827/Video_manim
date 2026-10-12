import sys

with open('base_scene.py', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace(
    'vi = Paragraph(vi_txt, font=FONT, font_size=22, color=C_WHITE, weight=BOLD, alignment="center")',
    'vi = Paragraph(*vi_txt.split("\\n"), font=FONT, font_size=22, color=C_WHITE, weight=BOLD, alignment="center", line_spacing=1.2)'
)
text = text.replace(
    'en = Paragraph(en_txt, font=FONT, font_size=18, color=FAMI_SUB, slant=ITALIC, alignment="center")',
    'en = Paragraph(*en_txt.split("\\n"), font=FONT, font_size=18, color=FAMI_SUB, slant=ITALIC, alignment="center", line_spacing=1.2)'
)
text = text.replace(
    'text_group = VGroup(vi, en).arrange(DOWN, buff=0.15)',
    'text_group = VGroup(vi, en).arrange(DOWN, buff=0.3)'
)

with open('base_scene.py', 'w', encoding='utf-8') as f:
    f.write(text)
print("done")
