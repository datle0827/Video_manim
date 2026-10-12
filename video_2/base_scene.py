"""
base_scene.py – Class nền chứa setup, phụ đề và các helper dùng cho mọi scene.
Updated with FaMI layout system từ fami_lib.py
"""

from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
try:
    from googletrans import Translator
    # translator initialized safely above
except Exception:
    class DummyTranslator:
        def translate(self, text, src='vi', dest='en'):
            class DummyResult:
                text = ''
            return DummyResult()
    translator = DummyTranslator()
import os
import unicodedata

from config import (
    FONT, LOGO_PATH,
    FAMI_BLUE, FAMI_CYAN, FAMI_SUB, ACCENT, DANGER, SUCCESS, TEXT_COLOR,
    C_WHITE, C_YELLOW, C_PRIMARY,
    POS_TITLE, POS_TOP_FOCUS, POS_CENTER, POS_BOTTOM_FOCUS, POS_SUBTITLE,
    LOGO_Y, SUB_VI_Y, SUB_EN_Y,
    SUBS,
)

# Khởi tạo Translator
# translator initialized safely above

# ──────────────────────────────────────────────────────────────────────────────
# UTILITY FUNCTIONS (từ fami_lib.py)
# ──────────────────────────────────────────────────────────────────────────────

def apply_fami_gradient(mobject, colors=None):
    """Áp dụng Gradient FaMI: Từ Cyan -> Blue"""
    if colors is None:
        colors = [FAMI_CYAN, FAMI_BLUE]
    for submob in mobject.family_members_with_points():
        if len(submob.points) > 0:
            submob.set_color(colors)
    return mobject


# ──────────────────────────────────────────────────────────────────────────────
# BASE CLASS (Kế thừa FaMI layout system)
# ──────────────────────────────────────────────────────────────────────────────

class LoanDecisionTreeBase(VoiceoverScene):
    """
    Class nền: khởi tạo logo, phụ đề và cung cấp các helper.
    Sử dụng bố cục FaMI (hệ tọa độ khóa cứng, gradient, nhiều style phụ đề).
    """
    
    def setup(self):
        """Khởi tạo: Logo, Phụ đề, VoiceoverService"""
        super().setup()
        self.set_speech_service(GTTSService(lang="vi"))
        
        # Logo FaMI cố định trên cùng
        try:
            self._logo = ImageMobject(LOGO_PATH).scale_to_fit_width(1.2)
            self._logo.to_edge(UP, buff=0.4)
        except Exception:
            self._logo = Text("FaMI 1956", font=FONT, font_size=25, color=FAMI_BLUE, weight=BOLD)
            self._logo.to_edge(UP, buff=0.4)
        self.add_foreground_mobject(self._logo)
        
        # Phụ đề ẩn (container)
        self._subtitle_obj = VGroup().move_to(POS_SUBTITLE)
        self.add_foreground_mobject(self._subtitle_obj)
    
    # ──────────────────────────────────────────────────────────────────────────
    # PHỤĐỀ (Subtitle Methods)
    # ──────────────────────────────────────────────────────────────────────────
    
    def update_subtitle(self, vi_text, style="default", hold_time=0):
        """
        Cập nhật phụ đề với tự động dịch sang Tiếng Anh.
        
        Styles: 'default', 'neon', 'banner', 'minimal', 'cinema'
        
        Args:
            vi_text: Văn bản Tiếng Việt
            style: Kiểu hiển thị phụ đề
            hold_time: Thời gian chờ (giây)
        """
        try:
            en_text = translator.translate(vi_text, src='vi', dest='en').text
        except:
            en_text = ""
            
        vi_text = unicodedata.normalize("NFC", vi_text)
        en_text = unicodedata.normalize("NFC", en_text)
        
        # 1. Tạo Text Objects cơ bản
        vi = Paragraph(*vi_text.split("\n"), font=FONT, font_size=22, color=C_WHITE, weight=BOLD, alignment="center", line_spacing=1.2)
        en = Paragraph(*en_text.split("\n"), font=FONT, font_size=18, color=FAMI_SUB, slant=ITALIC, alignment="center", line_spacing=1.2)
        
        text_group = VGroup(vi, en).arrange(DOWN, buff=0.15)
        if text_group.width > 7.5:
            text_group.scale_to_fit_width(7.5)
        
        # 2. Xử lý các Style khác nhau
        full_sub = VGroup()
        
        if style == "neon":
            # Neon: Chữ phát sáng, bóng màu xanh
            vi.set_color(C_WHITE).set_stroke(FAMI_CYAN, width=2, background=True)
            en.set_color(FAMI_SUB).set_stroke(C_YELLOW, width=1, background=True)
            glow = text_group.copy().set_stroke(FAMI_CYAN, width=8, opacity=0.2)
            full_sub = VGroup(glow, text_group)
        
        elif style == "banner":
            # Banner: Dải màu chạy ngang (Full width)
            bg_rect = Rectangle(
                width=config.frame_width,
                height=text_group.height + 0.6,
                fill_color=FAMI_BLUE,
                fill_opacity=0.9,
                stroke_width=0
            )
            line_top = Line(LEFT, RIGHT, color=FAMI_CYAN, stroke_width=2).scale_to_fit_width(config.frame_width)
            line_bottom = line_top.copy()
            line_top.next_to(bg_rect, UP, buff=0)
            line_bottom.next_to(bg_rect, DOWN, buff=0)
            
            full_sub = VGroup(bg_rect, line_top, line_bottom, text_group)
        
        elif style == "minimal":
            # Minimal: Chỉ bóng đổ (Shadow), không nền
            shadow = text_group.copy().set_color(BLACK).shift(0.05 * DOWN + 0.05 * RIGHT).set_opacity(0.5)
            full_sub = VGroup(shadow, text_group)
        
        elif style == "cinema":
            # Cinema: Khung xám bo tròn, giống phim rạp
            sub_bg = RoundedRectangle(
                corner_radius=0.3,
                width=text_group.width + 0.8,
                height=text_group.height + 0.5,
                fill_color="#000000",
                fill_opacity=0.7,
                stroke_width=1,
                stroke_color=GRAY_A
            )
            full_sub = VGroup(sub_bg, text_group)
        
        else:  # style == "default"
            # Default: Khung xám tối với viền Cyan
            sub_bg = RoundedRectangle(
                corner_radius=0.1,
                width=text_group.width + 0.6,
                height=text_group.height + 0.4,
                fill_color="#1A1A1A",
                fill_opacity=0.8,
                stroke_width=0.5,
                stroke_color=FAMI_CYAN
            )
            full_sub = VGroup(sub_bg, text_group)
        
        # 3. Cập nhật vị trí và hiển thị
        full_sub.move_to(POS_SUBTITLE)
        self._subtitle_obj.become(full_sub)
        
        if hold_time > 0:
            self.wait(hold_time)
    
    def sub(self, vi_txt, en_txt=None, hold=0):
        """
        Hiện phụ đề song ngữ (tương thích ngược với code cũ).
        Nếu không có en_txt, tự động dịch sang Tiếng Anh.
        
        Args:
            vi_txt: Văn bản Tiếng Việt
            en_txt: Văn bản Tiếng Anh (nếu None, tự động dịch)
            hold: Thời gian chờ (giây)
        """
        if en_txt is None:
            # Nếu không cung cấp EN, dùng tự động dịch
            self.update_subtitle(vi_txt, style="default", hold_time=hold)
        else:
            vi_txt = unicodedata.normalize("NFC", vi_txt)
            en_txt = unicodedata.normalize("NFC", en_txt)
            # Dùng text song ngữ trực tiếp (tương thích với mã cũ)
            vi = Paragraph(*vi_txt.split("\n"), font=FONT, font_size=22, color=C_WHITE, weight=BOLD, alignment="center", line_spacing=1.2)
            en = Paragraph(*en_txt.split("\n"), font=FONT, font_size=18, color=FAMI_SUB, slant=ITALIC, alignment="center", line_spacing=1.2)
            
            text_group = VGroup(vi, en).arrange(DOWN, buff=0.15)
            if text_group.width > 7.5:
                text_group.scale_to_fit_width(7.5)
            
            sub_bg = RoundedRectangle(
                corner_radius=0.1,
                width=text_group.width + 0.6,
                height=text_group.height + 0.4,
                fill_color="#1A1A1A",
                fill_opacity=0.8,
                stroke_width=0.5,
                stroke_color=FAMI_CYAN
            )
            full_sub = VGroup(sub_bg, text_group)
            full_sub.move_to(POS_SUBTITLE)
            self._subtitle_obj.become(full_sub)
            
            if hold > 0:
                self.wait(hold)
    
    def play_subs(self, key):
        """Phát tuần tự tất cả phụ đề của key từ config SUBS."""
        for vi, en, wait_before, hold in SUBS.get(key, []):
            if wait_before > 0:
                self.wait(wait_before)
            self.sub(vi, en, hold)
    
    # ──────────────────────────────────────────────────────────────────────────
    # TIÊU ĐỀ (Title Methods)
    # ──────────────────────────────────────────────────────────────────────────
    
    def create_title(self, line1, line2="", apply_gradient=True):
        """Skill: Tạo tiêu đề (Tự động Gradient & Đúng vị trí)"""
        if line2:
            t1 = Text(line1, font="Segoe UI", font_size=55, weight=BOLD)
            t2 = Text(line2, font="Segoe UI", font_size=55, weight=BOLD)
            title = VGroup(t1, t2).arrange(DOWN, buff=0.1) 
        else:
            title = Text(line1, font="Segoe UI", font_size=55, weight=BOLD)
        
        title.move_to(POS_TITLE)
        
        if title.width > 8.0:
            title.scale_to_fit_width(8.0)
            
        if apply_gradient:
            apply_fami_gradient(title)
        else:
            title.set_color(WHITE)
            
        return title
    
    # ──────────────────────────────────────────────────────────────────────────
    # HELPERS
    # ──────────────────────────────────────────────────────────────────────────
    
    def _lift(self):
        """Đưa logo & phụ đề lên lớp trên cùng."""
        self.bring_to_front(self._logo)
        self.bring_to_front(self._subtitle_obj)

    def clear_content(self, t=0.8):
        """Fade out toàn bộ nội dung, giữ lại logo và phụ đề."""
        keep = {id(self._logo), id(self._subtitle_obj)}
        to_remove = [m for m in self.mobjects if id(m) not in keep]
        if to_remove:
            self.play(
                AnimationGroup(
                    *[FadeOut(m, shift=DOWN*0.5) for m in to_remove], 
                    lag_ratio=0.05
                ),
                run_time=t
            )
        self.wait(0.3)
        self._lift()

    def _check_pop_in(self, anim):
        if getattr(anim, 'is_pop_in', False):
            return True
        if hasattr(anim, 'animations'):
            return any(self._check_pop_in(a) for a in anim.animations)
        return False

    def sp(self, *args, **kwargs):
        """play() rồi tự động đưa logo+subtitle lên trên."""
        has_pop = any(self._check_pop_in(anim) for anim in args)
        if has_pop:
            try:
                self.add_sound("audio/pop.wav")
            except:
                pass
        self.play(*args, **kwargs)
        self._lift()
