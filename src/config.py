from openai_endpoint import OpenAIEndpoint

openai_endpoints = {
    "45-qwen-dev": OpenAIEndpoint(
        "http://172.26.1.45:8001/v1",
        "qwen-7b-chat",
        stop=["<|im_end|>", "<|endoftext|>"],
    ),
    "45-qwen": OpenAIEndpoint(
        "http://172.26.1.45:8001/v1",
        "qwen-7b-chat",
        stop=["<|im_end|>", "<|endoftext|>"],
    ),
}
