import os
import re

directory = "c:/Users/admin/Downloads/videoxstk"
count = 0
for filename in os.listdir(directory):
    if filename.startswith("scene_") and filename.endswith(".py"):
        filepath = os.path.join(directory, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        if "FadeIn" in content:
            content = content.replace("FadeIn", "skill_pop_in")
            
            # Ensure it is imported before class definition
            header = content[:content.find("class ")]
            if "skill_pop_in" not in header:
                if "from helpers import " in content:
                    content = content.replace("from helpers import ", "from helpers import skill_pop_in, ", 1)
                else:
                    content = content.replace("from manim import *", "from manim import *\nfrom helpers import skill_pop_in", 1)
                    
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            count += 1
            print(f"Updated {filename}")
print(f"Total updated: {count}")
