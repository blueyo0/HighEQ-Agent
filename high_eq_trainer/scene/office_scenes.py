from .scene import register_scene, load_prompt_from_txt


register_scene(
    series="dev",
    title="0-0 暖她一整天",
    background="情人节，你暗恋的女生/男生突然向你发了早安问候。",
    npc_name="暗恋对象",
    npc_message="早呀",
    prompt=load_prompt_from_txt("prompts/0-0.txt"),
    npc_image="high_eq_trainer/assets/scene/0-0/npc.png",
    user_image="high_eq_trainer/assets/scene/0-0/user.png",
    tips="放松聊天，不要在乎条条框框",
)

register_scene(
    series="office",
    title="1-1 面对自嘲",
    background="你和领导打羽毛球，你赢了，领导叹了口气，自嘲自己老了，你想要安慰一下他。",
    npc_name="领导",
    npc_message="看来我是真老咯，不中用了。",
    prompt=load_prompt_from_txt("prompts/1-1.txt"),
    npc_image="high_eq_trainer/assets/scene/1-1/npc.png",
    user_image="high_eq_trainer/assets/scene/1-1/user.png",
    tips="和领导沟通，可以在表达尊敬的同时，展现关心。这种有点尴尬的场合也可以岔开话题试试。",
)

register_scene(
    series="office",
    title="1-2 笑对挫折",
    background="你正在参加一个会议，客户彻底否决了你们团队准备的方案，你想要挽回客户。",
    npc_name="客户",
    npc_message="别浪费我时间了，我不会再和你们合作了。",
    prompt=load_prompt_from_txt("prompts/1-2.txt"),
    npc_image="high_eq_trainer/assets/scene/1-2/npc.png",
    user_image="high_eq_trainer/assets/scene/1-2/user.png",
    tips="面对挫折，我们既需要向前的勇气，也需要接受自己的不足。",
)

register_scene(
    series="office",
    title="1-3 处理冲突",
    background="你和同事在工作中发生分歧，气氛很紧张，对方完全无法理解你的想法，你想要缓解冲突。",
    npc_name="同事",
    npc_message="你是不是脑子有坑，提出这种方案？",
    prompt=load_prompt_from_txt("prompts/1-3.txt"),
    npc_image="high_eq_trainer/assets/scene/1-3/npc.png",
    user_image="high_eq_trainer/assets/scene/1-3/user.png",
    tips="适当地表达自己的态度是职场的关键。",
)

register_scene(
    series="office",
    title="1-4 接受认可",
    background="领导在团队会议上表扬了你在一个项目中的出色表现，认可了你做出的成绩。 ",
    npc_name="领导",
    npc_message="你做得非常好，大家都应该向你学习。",
    prompt=load_prompt_from_txt("prompts/1-4.txt"),
    npc_image="high_eq_trainer/assets/scene/1-4/npc.png",
    user_image="high_eq_trainer/assets/scene/1-4/user.png",
    tips="面对褒奖，没必要故作谦虚，坦然接受也是美德。",
)