"""
gen_drawio.py -- Tao file draw.io kien truc du an FaMI
"""
import os

BR = "&#xa;"  # xuong dong trong draw.io value

def cell(cid, val, style, x, y, w, h, parent="1"):
    return (
        f'        <mxCell id="{cid}" value="{val}" style="{style}" '
        f'vertex="1" parent="{parent}">'
        f'<mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry" />'
        f'</mxCell>\n'
    )

def edge(eid, src, tgt, style, label="", parent="1"):
    return (
        f'        <mxCell id="{eid}" value="{label}" style="{style}" '
        f'edge="1" source="{src}" target="{tgt}" parent="{parent}">'
        f'<mxGeometry relative="1" as="geometry" />'
        f'</mxCell>\n'
    )

def swimlane(cid, val, style, x, y, w, h, parent="1"):
    return (
        f'        <mxCell id="{cid}" value="{val}" style="{style}" '
        f'vertex="1" parent="{parent}">'
        f'<mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry" />'
        f'</mxCell>\n'
    )

# ---- Styles ----
S_MAIN  = "rounded=1;fillColor=#005BAA;fontColor=#ffffff;strokeColor=#45C4D9;fontStyle=1;fontSize=12;"
S_LIB   = "rounded=1;fillColor=#1a3a5c;fontColor=#DFE858;strokeColor=#45C4D9;fontStyle=1;fontSize=11;"
S_FILE  = "rounded=1;fillColor=#23272e;fontColor=#ffffff;strokeColor=#45C4D9;fontSize=10;"
S_EXT   = "rounded=1;fillColor=#2d2d2d;fontColor=#aaaaaa;strokeColor=#555555;fontSize=10;"
S_HEAD  = "text;html=1;strokeColor=none;fillColor=#005BAA;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=1;fontColor=#ffffff;fontSize=16;fontStyle=1;"
S_SEC   = "text;html=1;strokeColor=#45C4D9;fillColor=#1a3a5c;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=1;fontColor=#DFE858;fontSize=12;fontStyle=1;"
S_SWIM  = "swimlane;fillColor=#005BAA;fontColor=#ffffff;strokeColor=#45C4D9;fontSize=12;fontStyle=1;"
S_ITEM  = "rounded=1;fillColor=#23272e;fontColor=#ffffff;strokeColor=#45C4D9;fontSize=10;align=left;spacingLeft=8;"
S_ITEM2 = "rounded=1;fillColor=#23272e;fontColor=#DFE858;strokeColor=#45C4D9;fontSize=10;align=left;spacingLeft=8;"
S_CODE  = "rounded=1;fillColor=#1a3a5c;fontColor=#DFE858;strokeColor=#45C4D9;fontSize=10;align=left;spacingLeft=8;"
E_MAIN  = "edgeStyle=orthogonalEdgeStyle;strokeColor=#45C4D9;fontSize=10;"
E_INH   = "edgeStyle=orthogonalEdgeStyle;strokeColor=#00e676;endArrow=block;endFill=1;fontSize=10;"
E_DEP   = "edgeStyle=orthogonalEdgeStyle;strokeColor=#DFE858;dashed=1;fontSize=9;"

# ============================================================
# DIAGRAM 1: Kien truc du an
# ============================================================
d1 = ""
d1 += '        <mxCell id="0" />\n'
d1 += '        <mxCell id="1" parent="0" />\n'

# Tieu de
d1 += cell("t0", "Kien truc Du an FaMI Video (Manim + gTTS)", S_HEAD, 450, 20, 660, 50)

# Entry point
d1 += cell("main", f"video_3_main.py{BR}class LoanDecisionTree{BR}construct()", S_MAIN, 580, 110, 300, 80)

# Core lib
d1 += cell("lbl_core", "Thu vien loi (Core)", S_SEC, 40, 100, 160, 35)
d1 += cell("cfg",  f"config.py{BR}SCRIPTS / SUBS{BR}Colors / Positions", S_LIB, 40, 145, 200, 80)
d1 += cell("base", f"base_scene.py{BR}LoanDecisionTreeBase{BR}setup/subtitle/sp()", S_LIB, 260, 145, 220, 80)
d1 += cell("hlp",  f"helpers.py{BR}rnode / info_card{BR}load_icon / skill_pop_in", S_LIB, 40, 270, 200, 80)

# Scenes
d1 += cell("lbl_s", "Scene Mixins (S1-S9)", S_SEC, 510, 100, 200, 35)
d1 += cell("s1", f"scene_s1.py{BR}SceneIntroMixin",        S_FILE, 510, 145, 150, 60)
d1 += cell("s2", f"scene_s2.py{BR}SceneProblemMixin",      S_FILE, 670, 145, 150, 60)
d1 += cell("s3", f"scene_s3.py{BR}SceneDataMixin",         S_FILE, 830, 145, 150, 60)
d1 += cell("s4", f"scene_s4.py{BR}SceneSinglePathMixin",   S_FILE, 990, 145, 150, 60)
d1 += cell("s5", f"scene_s5.py{BR}SceneMarkMixin",         S_FILE, 510, 220, 150, 60)
d1 += cell("s6", f"scene_s6.py{BR}SceneVarMixin",          S_FILE, 670, 220, 150, 60)
d1 += cell("s7", f"scene_s7.py{BR}SceneKeywordsMixin",     S_FILE, 830, 220, 150, 60)
d1 += cell("s8", f"scene_s8.py{BR}SceneSummaryMixin",      S_FILE, 990, 220, 150, 60)
d1 += cell("s9", f"scene_s9.py{BR}SceneQuestionMixin",     S_FILE, 750, 295, 150, 60)

# Assets
d1 += cell("lbl_a", "Tai nguyen (Assets)", S_SEC, 40, 380, 160, 35)
d1 += cell("ast", f"asset/{BR}SVG vector files", S_EXT, 40, 425, 120, 60)
d1 += cell("aud", f"audio/{BR}MP3 (gTTS auto)", S_EXT, 170, 425, 120, 60)
d1 += cell("stk", f"stock/{BR}Logo co phieu", S_EXT, 300, 425, 120, 60)

# External libs
d1 += cell("lbl_e", "Thu vien ngoai (External)", S_SEC, 480, 380, 200, 35)
d1 += cell("mn",  f"Manim{BR}Animation Engine", S_EXT, 480, 425, 130, 60)
d1 += cell("mv",  f"manim-voiceover{BR}GTTSService", S_EXT, 620, 425, 130, 60)
d1 += cell("gt",  f"gTTS{BR}Google TTS (VI)", S_EXT, 760, 425, 130, 60)
d1 += cell("gtr", f"googletrans{BR}VI to EN auto", S_EXT, 900, 425, 130, 60)

# Output
d1 += cell("out", f"OUTPUT{BR}FinalVideo.mp4{BR}1080 x 1920 px (9:16)", S_MAIN, 580, 530, 300, 70)

# Edges
d1 += edge("e1",  "main", "base", E_INH,  "ke thua")
d1 += edge("e2",  "main", "cfg",  E_DEP,  "import")
d1 += edge("e3",  "base", "hlp",  E_DEP,  "import")
d1 += edge("e4",  "main", "s1",   E_MAIN, "goi scene")
d1 += edge("e5",  "main", "s2",   E_MAIN)
d1 += edge("e6",  "main", "s3",   E_MAIN)
d1 += edge("e7",  "main", "s4",   E_MAIN)
d1 += edge("e8",  "main", "s5",   E_MAIN)
d1 += edge("e9",  "main", "s6",   E_MAIN)
d1 += edge("e10", "main", "s7",   E_MAIN)
d1 += edge("e11", "main", "s8",   E_MAIN)
d1 += edge("e12", "main", "s9",   E_MAIN)
d1 += edge("e13", "s1",   "cfg",  E_DEP,  "import")
d1 += edge("e14", "s1",   "hlp",  E_DEP,  "import")
d1 += edge("e15", "base", "mv",   E_INH,  "extends")
d1 += edge("e16", "cfg",  "gt",   E_MAIN, "TTS call")
d1 += edge("e17", "base", "gtr",  E_MAIN, "translate")
d1 += edge("e18", "mn",   "out",  E_MAIN, "render")

# ============================================================
# DIAGRAM 2: Thu vien dung chung
# ============================================================
d2 = ""
d2 += '        <mxCell id="0" />\n'
d2 += '        <mxCell id="1" parent="0" />\n'

d2 += cell("t2", "Kien truc Thu vien Dung chung (Shared Library)", S_HEAD, 200, 20, 920, 50)

# --- config.py swimlane ---
d2 += swimlane("sc", "config.py", S_SWIM, 40, 100, 300, 350)
d2 += cell("sc1", "VIDEO_W=1080 / VIDEO_H=1920 / BG_COLOR / FONT", S_ITEM2, 10, 40, 280, 35, "sc")
d2 += cell("sc2", "FAMI_BLUE / FAMI_CYAN / C_DANGER / C_SUCCESS / C_WARNING", S_ITEM2, 10, 80, 280, 35, "sc")
d2 += cell("sc3", "POS_TITLE / POS_CENTER / POS_SUBTITLE / POS_TOP_FOCUS", S_ITEM2, 10, 120, 280, 35, "sc")
d2 += cell("sc4", "SCRIPTS = { 's1': '...loi thoai...', 's2': ..., 's9': ... }", S_ITEM2, 10, 160, 280, 35, "sc")
d2 += cell("sc5", "SUBS = { 's1': [(vi, en, delay, dur), ...], ... }", S_ITEM2, 10, 200, 280, 35, "sc")
d2 += cell("sc6", "generate_audio() -- gTTS -- luu /audio/sX.mp3", S_ITEM2, 10, 240, 280, 35, "sc")
d2 += cell("sc7", "audio_path(name) -- tra ve duong dan file mp3", S_ITEM2, 10, 280, 280, 35, "sc")

# --- base_scene.py swimlane ---
d2 += swimlane("sb", "base_scene.py  (LoanDecisionTreeBase extends VoiceoverScene)", S_SWIM, 380, 100, 580, 350)
d2 += cell("sb1", "setup() -- Logo FaMI co dinh + GTTSService(lang='vi') + subtitle container", S_ITEM, 10, 40, 560, 35, "sb")
d2 += cell("sb2", "create_title(line1, line2) -- gradient Cyan-Blue, auto-fit, POS_TITLE", S_ITEM, 10, 80, 560, 35, "sb")
d2 += cell("sb3", "update_subtitle(vi_text, style) -- 5 styles: default/neon/banner/minimal/cinema + auto VI-EN", S_ITEM, 10, 120, 560, 35, "sb")
d2 += cell("sb4", "sub(vi_txt, en_txt, hold) -- phu de song ngu thu cong hoac tu dong dich", S_ITEM, 10, 160, 560, 35, "sb")
d2 += cell("sb5", "sp(*args, **kwargs) -- play() roi bring_to_front logo+sub + pop sound", S_ITEM, 10, 200, 560, 35, "sb")
d2 += cell("sb6", "clear_content(t=0.8) -- FadeOut tat ca tru logo+sub | _lift() -- giu layer", S_ITEM, 10, 240, 560, 35, "sb")
d2 += cell("sb7", "apply_fami_gradient(mob) / escape_ampersand(text) / play_subs(key)", S_ITEM, 10, 280, 560, 35, "sb")

# --- helpers.py swimlane ---
d2 += swimlane("sh", "helpers.py  (UI Factory Functions)", S_SWIM, 40, 490, 300, 330)
d2 += cell("sh1", "skill_pop_in(mob, sound) -- FadeIn ease_out_back + is_pop_in flag", S_ITEM2, 10, 40, 280, 40, "sh")
d2 += cell("sh2", "rnode(text, fill, w, h, fs) -- RoundedRect + auto-wrap MarkupText", S_ITEM2, 10, 85, 280, 40, "sh")
d2 += cell("sh3", "info_card(title, body, accent, w, h) -- Card co thanh mau tren", S_ITEM2, 10, 130, 280, 40, "sh")
d2 += cell("sh4", "load_icon(name, width, bg_color) -- SVG mapping 20+ icons + fallback", S_ITEM2, 10, 175, 280, 40, "sh")
d2 += cell("sh5", "flow_block(label_top, label_bot, color) -- Khoi so do luong", S_ITEM2, 10, 220, 280, 40, "sh")
d2 += cell("sh6", "make_centered_markup / sec_title / auto_wrap / escape_ampersand", S_ITEM2, 10, 265, 280, 35, "sh")

# --- scene template swimlane ---
d2 += swimlane("ss", "scene_sX.py  (Mixin Pattern Template)", S_SWIM, 380, 490, 580, 330)
d2 += cell("ss1", "class SceneXxxMixin:", S_CODE, 10, 40, 560, 28, "ss")
d2 += cell("ss2", "  def scene_xxx(self):", S_CODE, 10, 70, 560, 28, "ss")
d2 += cell("ss3", "    ttl = self.create_title('Ten canh')  # Tu base_scene", S_CODE, 10, 100, 560, 28, "ss")
d2 += cell("ss4", "    with self.voiceover(text=SCRIPTS['sX']) as tracker:", S_CODE, 10, 130, 560, 28, "ss")
d2 += cell("ss5", "      self.update_subtitle('Phu de...', style='default')", S_CODE, 10, 160, 560, 28, "ss")
d2 += cell("ss6", "      self.sp(Write(ttl), run_time=tracker.duration * 0.4)", S_CODE, 10, 190, 560, 28, "ss")
d2 += cell("ss7", "      self.wait(max(0.1, tracker.duration - anim_time))", S_CODE, 10, 220, 560, 28, "ss")
d2 += cell("ss8", "    self._lift()      # Dua logo+sub len tren", S_CODE, 10, 250, 560, 28, "ss")
d2 += cell("ss9", "    self.clear_content()  # Lam sach cuoi canh", S_CODE, 10, 280, 560, 28, "ss")

# Edges diagram 2
d2 += edge("f1", "sb", "sc",  E_DEP,  "import config")
d2 += edge("f2", "sb", "sh",  E_DEP,  "import helpers")
d2 += edge("f3", "ss", "sb",  E_INH,  "ke thua (MRO)")
d2 += edge("f4", "ss", "sc",  E_DEP,  "import SCRIPTS")
d2 += edge("f5", "ss", "sh",  E_DEP,  "import helpers")

# ============================================================
# Assembly
# ============================================================
def wrap_diagram(did, dname, content):
    return (
        f'  <diagram id="{did}" name="{dname}">\n'
        f'    <mxGraphModel dx="1600" dy="900" grid="1" gridSize="10" '
        f'guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" '
        f'pageScale="1" pageWidth="1654" pageHeight="1169" math="0" shadow="0">\n'
        f'      <root>\n'
        f'{content}'
        f'      </root>\n'
        f'    </mxGraphModel>\n'
        f'  </diagram>\n'
    )

xml = '<?xml version="1.0" encoding="UTF-8"?>\n<mxfile version="21.0.0">\n'
xml += wrap_diagram("d1", "Kien truc Du an", d1)
xml += wrap_diagram("d2", "Thu vien Dung chung", d2)
xml += '</mxfile>\n'

out = os.path.join(
    r"C:\Users\admin\.gemini\antigravity\brain\085f1634-5ece-460c-8d30-3c5152f3816d",
    "fami_architecture.drawio"
)
with open(out, "w", encoding="utf-8") as f:
    f.write(xml)
print(f"Done: {out}")
print(f"Size: {len(xml)} bytes")
