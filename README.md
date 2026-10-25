# [久保統計の完全解答](https://uzanka.github.io/kubo-toukei/)

[「大学演習　熱学・統計力学」](https://www.amazon.co.jp/dp/4785380322)（久保 亮五 著、裳華房）、通称 **久保統計** の演習問題を、
AI を使って解いた解答です。

- [Markdown のままで見る](contents.md)場合は、一部Texが正しく表示されません。
- このページには解答のみを載せています。
- 問題、解答例は原本を参照してください。
- 解答作成中に見つけた原本の誤植または矛盾点については、[正誤表](Book-Errata.md) を参照してください。
- フラクトゥール体の記号がGithubでは正常に表示できず通常の書体と見分けがつかないことがあります。例（フラクトゥール体： $\mathfrak{pv}$ ）が通常書体で表示されている場合は、正しく表示できていませんので、VSCodeで閲覧してください。
- 画像認識、解答、検証はすべてAIで行っています。
そのため、正しい解答になっていない可能性があります。
参考にする場合には十分に注意してください。

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
