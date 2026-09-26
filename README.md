# 久保統計の完全解答

「大学演習　熱学・統計力学」、通称 **久保統計** の演習問題を、
AI を使って解いた解答です。

（注）
- 画像認識、解答、検証はすべてAIで行っています。
そのため、正しい解答になっていない可能性があります。
参考にする場合には十分に注意してください。
- 誤記、誤答を見つけた場合は、issue、pull request を発行してください。

## 解答

[久保統計の完全解答](index.md)

（注）
- このページには解答のみを載せています。
- 問題は原本を参照してください。
- 未検証のものは載せていません（未検証のものはリンク切れ状態になっています）。

## AI について

以下の環境で解答作成と検証を行っています。

- LLM
  - LLMサーバ：[ollama](https://ollama.com/)
  - CLI (frontend)：[claude CLI](https://claude.ai/) （ollama launch claude で起動）
  - MCP：[server-sequential-thinking MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/sequentialthinking)
  - 使用モデル
    - [画像認識、テキスト化、解答作成プロンプト](prompts/prompt.txt)：[gemma4:26b](https://ollama.com/library/gemma4)
    - 検証プロンプト（[数学的](prompts/verify-logic.txt)、[物理的](prompts/verify-physics.txt)）：[qwen3.6:27b](https://ollama.com/library/qwen3.6)

- PC
  - CPU：AMD Ryzen9800X3D
  - MEMORY：64GB
  - GPU：NVIDIA RTX5060Ti 16GB
  - OS：Windows11

（注）
- Sequential Thinking MCP は、ローカルLLMの欠点を補うために使用しています。
- ローカルLLM特有の誤動作を避けるため、プロンプト実行前には /clear でセッションをリセットしてください。
- 解答作成・検証に失敗することがよくありますので、/clear または claude CLI 再起動後に再実行してください。
