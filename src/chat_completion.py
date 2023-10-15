import json
from typing import List

import openai

from config import openai_endpoints
from openai_endpoint import OpenAIEndpoint


def get_prompt(length=1024) -> List[dict]:
    prompt_list = []
    with open("../material/prompts.json", "r") as f:
        origin_list = json.load(f)
        for data in origin_list:
            prompt_item = {}
            if len(data["origin_prompt"]) > length:
                prompt_item["prompt"] = "{}。{}".format(
                    data["origin_prompt"][:length], data["question"]
                )
            else:
                prompt_item["prompt"] = "{}。{}".format(
                    data["origin_prompt"][:length], data["question"]
                )
            prompt_list.append(prompt_item)
    return prompt_list


class ChatCompletion:
    def __init__(self, endpoint: OpenAIEndpoint):
        self.model = endpoint.model
        self.server = endpoint.server
        self.stop = endpoint.stop

    def send_chat(self, prompt) -> str:
        openai.api_key = "sk-"
        openai.api_base = self.server
        res = openai.ChatCompletion.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1,
            max_tokens=128,
            top_p=1,
            stop=["<|im_end|>", "<|endoftext|>"],
        )

        return res["choices"][0]["message"]["content"]


if __name__ == "__main__":
    for endpoint in openai_endpoints.values():
        for loop in range(1, 10):
            length = 1024 * loop
            prompt_list = get_prompt(length)
            for prompt_item in prompt_list:
                chat_completion = ChatCompletion(endpoint)
                res = chat_completion.send_chat(prompt_item["prompt"])
                print(res)
