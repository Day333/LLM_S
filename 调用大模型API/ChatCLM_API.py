import zhipuai
from zhipuai_llm import ZhipuAILLM

zhipuai.api_key = "" #填写控制台中获取的 APIKey 信息
model = "chatglm_std" #用于配置大模型版本

# def getText(role, content, text = []):
#     # role 是指定角色，content 是 prompt 内容
#     jsoncon = {}
#     jsoncon["role"] = role
#     jsoncon["content"] = content
#     text.append(jsoncon)
#     return text

# question = getText("user", "你好")
#
# # 请求模型
# response = zhipuai.model_api.invoke(
#     model=model,
#     prompt=question
# )
# print(response)

zhipuai_model = ZhipuAILLM(model="chatglm_std", temperature=0, zhipuai_api_key=zhipuai.api_key)
print(zhipuai_model.generate(['你好']))

