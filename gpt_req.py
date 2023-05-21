import openai

openai.api_key = 'token'


def get_gpt_ans(request: str):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": request}
        ]
    )

    return completion.choices[0].message["content"]
