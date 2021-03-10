import os

class Scene:
    def __init__(self):
        pass

    def load_scene(self, filename):
        here = os.path.dirname(os.path.abspath(__file__))
        scene_path = os.path.join(here, "scenes", filename)
        with open(scene_path, "r") as fp:
            lines = fp.readlines()

        return lines

    def parse_title(self, lines):
        for line in lines:
            pos = line.find("TITLE=")
            if pos != -1:
                title_pos = pos + 6
                return line[title_pos:]

    def parse_paragraph(self, lines):
        text = []
        found_text = False
        for line in lines:
            if found_text:
                ## PRINT THE PARAGRAPH UNTIL WE REACH END ##
                text.append(line)
            else:
                ## LOOK FOR A 'BEGIN' TOKEN ##
                pos = line.find("BEGIN")
                if pos != -1:
                    found_text = True

        return text

### TESTING ###
if __name__ == '__main__':
    scene = Scene()
    lines = scene.load_scene("scene_004.txt")
    print(scene.parse_title(lines))
    story = scene.parse_paragraph(lines)
    for line in story:
        print(line)