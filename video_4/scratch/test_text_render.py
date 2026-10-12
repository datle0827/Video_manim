import sys
sys.path.append("D:/Downloads/videoxstk4")
from manim import *
from googletrans import Translator
import unicodedata
from config import FONT, C_WHITE, FAMI_SUB

translator = Translator()

class TestTextScene(Scene):
    def construct(self):
        vi_text = "sản xuất và các lĩnh vực\ndựa vào dự báo để ra quyết định."
        try:
            en_text = translator.translate(vi_text, src='vi', dest='en').text
        except Exception as e:
            en_text = f"Translation error: {e}"
            
        with open("D:/Downloads/videoxstk4/scratch/translation.txt", "w", encoding="utf-8") as f:
            f.write(f"vi_text:\n{vi_text}\n\nen_text:\n{en_text}\n")
            
        vi_text = unicodedata.normalize("NFC", vi_text)
        en_text = unicodedata.normalize("NFC", en_text)
        
        from helpers import escape_ampersand
        vi_lines = [MarkupText(escape_ampersand(line), font=FONT, font_size=22, color=C_WHITE, weight=BOLD) for line in vi_text.split("\n") if line.strip()]
        vi = VGroup(*vi_lines).arrange(DOWN, buff=0.1)
        
        en_lines = []
        if en_text.strip():
            en_lines = [MarkupText(escape_ampersand(line), font=FONT, font_size=18, color=FAMI_SUB, slant=ITALIC) for line in en_text.split("\n") if line.strip()]
        
        if en_lines:
            en = VGroup(*en_lines).arrange(DOWN, buff=0.1)
            text_group = VGroup(vi, en).arrange(DOWN, buff=0.15)
        else:
            text_group = VGroup(vi)
            
        self.add(text_group)
        self.wait(1)
