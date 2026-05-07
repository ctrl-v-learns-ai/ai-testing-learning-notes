# 🧪 AI Testing Learning Notes

> **从测试工程师到AI测试工程师的完整学习路径**
> 
> 系统学习AI技术，掌握AI测试方法，构建可落地的项目经验

---

## 👤 关于我

- 🎯 软件测试工程师，目前在某汽车公司做外包测试
- 🚀 正在系统学习AI相关知识，目标是转行AI测试工程师
- 📝 记录学习过程，分享给同样想转行的测试同学
- 💡 相信：**测试工程师转AI有天然优势——我们更懂质量、更懂边界、更懂用户体验**

---

## 🎯 学习路线

```
基础巩固 → 机器学习 → 深度学习 → AI测试专项 → 项目实战 → 面试准备
   ↓          ↓          ↓           ↓           ↓          ↓
 NumPy     线性回归     PyTorch    LangChain    完整项目    面试准备
 Pandas    分类算法     神经网络    Prompt工程   RAG应用    项目展示
 Python    聚类算法     CNN        LLM评估      AI测试工具  技术沉淀
 统计学                                            安全测试
 SQL
```

---

## 📚 学习内容

### 🧱 基础模块（01-foundations）

| 模块 | 内容 | 笔记 | 练习 | 项目 |
|------|------|------|------|------|
| **NumPy** | 数组操作、数学函数、线性代数 | 3篇 | 7个 | 3个 |
| **Pandas** | 数据处理、清洗、可视化 | 4篇 | 10个 | 4个 |
| **Python进阶** | 装饰器、生成器、上下文管理器、类型提示 | 4篇 | 4个 | 2个 |
| **统计学** | 描述性统计、概率、假设检验 | 3篇 | 3个 | 2个 |
| **SQL** | 基本查询、表连接、分组聚合 | 3篇 | 3个 | 2个 |

### 🤖 机器学习（02-machine-learning）

| 内容 | 说明 |
|------|------|
| 线性回归 | 预测连续值、模型评估 |
| 分类算法 | 逻辑回归、决策树、随机森林、SVM |
| 聚类算法 | K-Means、层次聚类、DBSCAN |

### 🧠 深度学习（03-deep-learning）

| 内容 | 说明 |
|------|------|
| PyTorch基础 | 张量操作、自动求导 |
| 神经网络 | 全连接网络、激活函数、优化器 |
| CNN | 卷积层、池化层、图像分类 |

### 🧪 AI测试专项（04-ai-testing）⭐ 重点

| 模块 | 内容 | 项目 |
|------|------|------|
| **LangChain** | 6阶段完整学习：Model I/O → Retrieval → Chains → Memory → Agents → Deploy | 6个 |
| **Prompt工程** | 提示词设计、A/B测试、优化技巧 | 1个 |
| **LLM评估** | 评估指标、评估工具、自动化评估 | 1个 |
| **AI测试方法** | 测试策略、测试用例设计、自动化测试 | 1个 |
| **AI安全与伦理** | 幻觉检测、偏见评估、提示注入防护 | - |

### 🚀 项目实战（05-projects）

共 **22个完整项目**，涵盖：

```
📊 数据分析：学生成绩管理、销售数据分析、数据可视化仪表板
🤖 机器学习：房价预测、客户细分
🧠 深度学习：MNIST分类、情感分析
🔗 LangChain：聊天机器人、RAG系统、AI助手
🧪 AI测试：提示词优化、LLM评估平台、测试用例生成器
```

### 💼 面试准备（06-interview）

| 内容 | 说明 |
|------|------|
| Python面试 | 数据类型、装饰器、生成器、常见编程题 |
| ML面试 | 算法原理、评估指标、特征工程 |
| AI测试面试 | 测试方法、评估工具、项目经验 |
| 项目经历 | STAR法则、项目展示模板 |

---

## 🛠 技术栈

### 核心技术
- **Python** - 主要编程语言
- **LangChain** - LLM应用开发框架
- **PyTorch** - 深度学习框架

### 数据处理
- **NumPy** - 数值计算
- **Pandas** - 数据分析
- **Matplotlib/Seaborn** - 数据可视化

### AI/ML
- **scikit-learn** - 机器学习
- **OpenAI API** - 大语言模型
- **FAISS** - 向量数据库

### 测试评估
- **LangSmith** - LLM监控评估
- **DeepEval** - LLM评估框架
- **RAGAS** - RAG系统评估

---

## 📂 项目结构

```
ai-testing-learning-notes/
├── 01-foundations/          # 基础模块
│   ├── 01-numpy/
│   ├── 02-pandas/
│   ├── 03-python-advanced/
│   ├── 04-statistics/
│   └── 05-sql/
├── 02-machine-learning/     # 机器学习
├── 03-deep-learning/        # 深度学习
├── 04-ai-testing/           # AI测试专项
│   ├── 01-LangChain/
│   ├── 02-prompt-engineering/
│   ├── 03-llm-evaluation/
│   ├── 04-ai-testing-methods/
│   └── 05-ai-safety-ethics/
├── 05-projects/             # 项目实战
├── 06-interview/            # 面试准备
├── .env                     # API密钥（已gitignore）
└── AGENTS.md                # 项目说明
```

---

## 🚀 快速开始

### 环境准备

```bash
# 克隆仓库
git clone https://github.com/ctrl-v-learns-ai/ai-testing-learning-notes.git

# 进入项目目录
cd ai-testing-learning-notes

# 创建虚拟环境
python -m venv venv

# 激活虚拟环境（Windows）
.\venv\Scripts\activate

# 安装依赖（按项目安装）
cd 05-projects/08-langchain/01_model_io
pip install -r requirements.txt
```

### 运行示例

```bash
# 运行练习
cd 01-foundations/01-numpy/exercises/01_basic_array
python 01_create_array.py

# 运行项目
cd 05-projects/08-langchain/01_model_io
python main.py
```

---

## 📊 学习进度

| 阶段 | 内容 | 状态 | 完成度 |
|------|------|------|--------|
| 第1阶段 | 基础巩固与拓展 | ✅ 已完成 | 100% |
| 第2阶段 | 机器学习核心 | ✅ 已完成 | 100% |
| 第3阶段 | 深度学习与实践 | ✅ 已完成 | 100% |
| 第4阶段 | AI测试专项 | ✅ 已完成 | 100% |
| 第5阶段 | 项目实战与综合提升 | ✅ 已完成 | 100% |
| 第6阶段 | 面试准备与冲刺 | ✅ 已完成 | 100% |

---

## 💡 学习心得

### 测试工程师转AI的优势

1. **质量思维** - 我们更关注输出的准确性和可靠性
2. **边界意识** - 我们更擅长设计边界测试用例
3. **系统性思维** - 我们更懂测试策略和方法论
4. **用户视角** - 我们更关注用户体验和场景覆盖

### 学习建议

1. **先动手，再理解** - 不要纠结于数学公式，先跑通代码
2. **项目驱动** - 每个知识点都配一个实际项目
3. **测试思维** - 用测试的角度学习AI，更容易理解
4. **持续输出** - 写笔记、做项目、分享经验

---

## 🔗 相关链接

- 📱 我的小红书：[Ctrl V--转岗AI测试](https://www.xiaohongshu.com/user/profile/639eccff0000000026004f96)
- 💻 项目合集仓库：[ai-testing-projects](https://github.com/ctrl-v-learns-ai/ai-testing-projects)

---

## ⭐ 支持

如果这个项目对你有帮助，欢迎：

- ⭐ **Star** - 给个星星鼓励一下
- 🍴 **Fork** - Fork后自己改改
- 📝 **Issue** - 提出建议和问题
- 🔀 **PR** - 欢迎贡献代码

---

## 📞 联系我

- 有问题？提 [Issue](https://github.com/ctrl-v-learns-ai/ai-testing-learning-notes/issues)
- 想交流？欢迎评论区讨论
- 想合作？欢迎私信联系

---

**最后更新：2026年5月**

> 💪 **测试工程师转AI，不是转行，是升级！**
