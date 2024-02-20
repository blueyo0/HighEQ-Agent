from .scene import register_scene, load_prompt_from_txt

CN_TEXT_0 = """
情人节，你暗恋的女生/男生突然向你发了早安问候。你应该怎么回复？
"""

CN_MESSAGE_0 = """
早呀
"""

register_scene(
    series="dev",
    title="0-0 暖她一整天",
    background=CN_TEXT_0,
    npc_name="暗恋对象",
    npc_message=CN_MESSAGE_0,
    prompt="",
    npc_image="high_eq_trainer/assets/scene/0-0/npc.png",
    user_image="high_eq_trainer/assets/scene/0-0/user.png",
)

CN_TITLE_1 = "1-1 面对自嘲"
CN_TEXT_1 = """
你和领导打羽毛球，你赢了，领导叹了口气，自嘲自己老了。你应该怎么回复？
"""
CN_MESSAGE_1 = """
看来我是真老咯，不中用了。
"""

register_scene(
    series="office",
    title=CN_TITLE_1,
    background=CN_TEXT_1,
    npc_name="领导",
    npc_message=CN_MESSAGE_1,
    prompt=load_prompt_from_txt("prompts/1-1.txt"),
    npc_image="high_eq_trainer/assets/scene/1-1/npc.png",
    user_image="high_eq_trainer/assets/scene/1-1/user.png",
)
