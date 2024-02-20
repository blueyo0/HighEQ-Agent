from dataclasses import dataclass

@dataclass
class Scene:
    series: str 
    title: str
    background : str
    npc_name: str
    npc_message: str
    prompt: str
    npc_image: str
    user_image: str

_REGISTERED_SCENES = []

def register_scene(series, title, background, npc_name, npc_message, prompt, npc_image, user_image):
    _REGISTERED_SCENES.append(
        Scene(series, title, background, npc_name, npc_message, prompt, npc_image, user_image)
    )

def list_sorted_scene():
    return [
        s for _, s in sorted(
            enumerate(_REGISTERED_SCENES),
            key=lambda x: (x[1].series, x[0])
        )
    ]

def load_prompt_from_txt(prompt_path):
    lines = open(prompt_path, "r", encoding="utf-8").readlines()
    content = "".join(lines)
    return content