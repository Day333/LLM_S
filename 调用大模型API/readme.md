# 1 基本概念
## 1. Prompt
Prompt可以理解为对于大模型的输入，而大模型对应的输出则是Completion。
## 2. Temprature
LLM的生成结果具有随机性，Temprature可以影响大模型的随机性程度，当取值接近0时，预测的随机性会比较低，产生更保守、可预测的文本；如果取值接近1，预测的随机性会较高。
### 3. System Prompt
可以理解为常驻性Prompt。
# 2 调用大模型API
暂且先选择一个进行使用，这里先选择的是ChatGLM。
