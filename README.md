# [久保統計の完全解答](https://github.com/uzanka/kubo-toukei/wiki)

## 作成環境

以下の環境で解答作成と検証を行っています。

- LLM
  - LLMサーバ：[ollama](https://ollama.com/)
  - CLI (frontend)：[Claude Code CLI](https://claude.ai/) （ollama launch claude で起動）
  - MCP：[sequential-thinking MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/sequentialthinking)
  - 使用モデル
    - [gemma4:26b](https://ollama.com/library/gemma4)：主に[画像認識、テキスト化、解答作成プロンプト](prompts/prompt.txt)で使用
    - [qwen3.6:27b](https://ollama.com/library/qwen3.6)：主に検証プロンプト（[数学的](prompts/verify-logic.txt)、[物理的](prompts/verify-physics.txt)）、修正プロンプトで使用
  - その他
    - [Node.js](https://nodejs.org/ja)（MCP使うときに必要）
    - [Python](https://www.python.org/)
      - matplotlib（図を描くときに必要）
    - ChatGPT：検証→修正のループが終わらない解答の修正で使用

- PC
  - CPU：AMD Ryzen9800X3D
  - MEMORY：64GB
  - GPU：NVIDIA RTX5060Ti 16GB
  - OS：Windows 11
