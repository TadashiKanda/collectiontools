import openai
openai.api_key = "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"

text = "�}�C�i���o�[�J�[�h���߂���g���u�������������A�u���N�ی��؂̔p�~�v�u���̕ύX�v�u����Ԕ[�v�Ȃǂɂ��č���̕�R���ŋc�_����܂����B"

response = openai.Completion.create(
    engine="davinci",
    prompt=text,
    temperature=0.7,
    max_tokens=1500,
    presence_penalty=0,
)

print(response['choices'][0]['text'])