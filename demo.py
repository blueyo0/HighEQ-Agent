import logging
import os
import re
import importlib
import gradio as gr
from high_eq_trainer.scene import list_sorted_scene
from high_eq_trainer.llms import _LLMS, get_llm_fn
from high_eq_trainer.utils import timer


_LANG = os.environ.get('QUESTION_LANG', 'cn')
assert _LANG in ['cn'], _LANG
content = importlib.import_module(f"high_eq_trainer.lang.{_LANG}")
logging.getLogger().setLevel(logging.INFO)
_LLM = list(_LLMS.keys())[0]
logging.info(f'Use {_LLM} as default option')
_SCENES = list_sorted_scene()

_CONVSATIONS = [
    [None, "早呀"],
    ["高情商", "天哪，暖我一整天~"],
    [None, "亲爱的，点击左下角的场景选择，选择想体验的场景吧~"],
]

def construct_conversation(choice):
    scene = _SCENES[choice]
    logging.info(f'select {scene.title}')
    description = f"""
    <h2 style="color: #6d28d9;"> {scene.title} </h2>
    <h4> {scene.background} </h4>
    """
    npc_obj = gr.Image(scene.npc_image, label=scene.npc_name,
                       show_label=True, show_download_button=False)
    return [
        True, [[None, scene.npc_message]], 
        gr.Button(content.button_submit, interactive=True), 
        npc_obj, scene.user_image, description, ""
    ] 

def parse_result(text):
    text = text.replace("[PAD151645]", "").replace("[PAD151643]", "").strip()
    pattern = r".*情感评分：.*?（(\d+)分）.*?目的评分：.*?（(\d+)分）.*"
    print("text:", text)
    matches = re.search(pattern, text, re.DOTALL)
    if matches:
        npc_reply = text.split("情感评分：")[0]
        emotion_score = int(matches.group(1))
        purpose_score = int(matches.group(2))
        return True, [npc_reply, emotion_score, purpose_score]
    else:
        return False, ["你说什么？刚刚有些耳背。（NPC好像走神了，请重试一次吧）", 0, 0]
        
@timer
def chat_with_llm(input_text, max_retry=2):
    print("input:", input_text)
    for _ in range(max_retry):
        answer = get_llm_fn(_LLM)(input_text)
        status, result = parse_result(answer)
        if(status==False): continue
        return result
  
def update_chat(choice, reply, conversation, is_chatbot_clear):
    scene = _SCENES[choice]
    if(is_chatbot_clear):
        npc_reply, emotion_score, purpose_score = chat_with_llm(scene.prompt+reply+"\nNPC：")
        # npc_reply, emotion_score, purpose_score = chat_with_llm(scene.prompt+reply+"\nThink step-by-step：")

        if(emotion_score>5):
            score = "【成功】高情商人类就是你！"
        else:
            score = "【失败】TA怎么这么难懂..."

        # if(emotion_score>5 and purpose_score>5):
        #     score = "获得成就：高情商人类"
        # elif(emotion_score<=5 and purpose_score>5):
        #     score = "获得成就：取悦自己，也很重要"
        # elif(emotion_score>5 and purpose_score<=5):
        #     score = "获得成就：别忘了你的出发点"
        # else:
        #     score = "获得成就：弱智吧荣誉吧主"

        return False, conversation+[[reply, npc_reply], [None, score]], gr.Button(content.button_restart, interactive=True)
    else: 
        # refresh conversation to make the chatbot clear
        return True, [[None, scene.npc_message]], gr.Button(content.button_submit, interactive=True)


if __name__ == '__main__':
    custom_css = """
        * {
            font-size: 24px;
        }
    """
    my_theme = gr.themes.Soft()

    with gr.Blocks(title="High EQ Trainer", theme=my_theme, css=custom_css) as demo:
        with gr.Row():
            banner = gr.Image("high_eq_trainer/assets/banner_v2.png", 
                                show_label=False, show_download_button=False)
        with gr.Row():
            scene_description = gr.HTML(content.description)

        with gr.Row():
            with gr.Column(scale=1):
                npc_image = gr.Image("high_eq_trainer/assets/npc_init.png", label="NPC",
                                     show_label=True, show_download_button=False)
            with gr.Column(scale=2):
                chatbot = gr.Chatbot(show_label=False, value=_CONVSATIONS)
            with gr.Column(scale=1):
                user_image = gr.Image("high_eq_trainer/assets/avatar.png", label="玩家",
                                      show_label=True, show_download_button=False)

        with gr.Row():
            with gr.Column(scale=1):
                dropdown = gr.Dropdown(choices=[(s.title, i) for i, s in enumerate(_SCENES)], 
                                       label="场景选择", interactive=True, value=0)
            with gr.Column(scale=2):
                text_input = gr.TextArea(lines=1, label="回复框", value="在这里输入回复", interactive=True)
            button = gr.Button(content.button_submit, interactive=False)
            is_chatbot_clear = gr.State(True)

        gr.Markdown(content.tos_markdown)

        dropdown.change(fn=construct_conversation, inputs=dropdown, outputs=[is_chatbot_clear, chatbot, button, npc_image, user_image, scene_description, text_input])
        button.click(fn=update_chat, inputs=[dropdown, text_input, chatbot, is_chatbot_clear], outputs=[is_chatbot_clear, chatbot, button])

    demo.launch(share=False)
