# [久保統計の完全解答](index.md)

[「大学演習　熱学・統計力学」](https://www.amazon.co.jp/dp/4785380322)（久保 亮五 著、裳華房）、通称 **久保統計** の演習問題を、
AI を使って解いた解答です。

- このページには解答のみを載せています。
- 問題、解答例は原本を参照してください。
- 取り消し線を引いてあるリンクは未検証の解答です。
- 画像認識、解答、検証はすべてAIで行っています。
そのため、正しい解答になっていない可能性があります。
参考にする場合には十分に注意してください。
- 誤記、誤答を見つけた場合は、issue、pull request を発行してください。

## AI について

以下の環境で解答作成と検証を行っています。

- LLM
  - LLMサーバ：[ollama](https://ollama.com/)
  - CLI (frontend)：[Claude Code CLI](https://claude.ai/) （ollama launch claude で起動）
  - MCP：[server-sequential-thinking MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/sequentialthinking)
  - 使用モデル
    - [画像認識、テキスト化、解答作成プロンプト](prompts/prompt.txt)：[gemma4:26b](https://ollama.com/library/gemma4)
    - 検証プロンプト（[数学的](prompts/verify-logic.txt)、[物理的](prompts/verify-physics.txt)）：[qwen3.6:27b](https://ollama.com/library/qwen3.6)

- PC
  - CPU：AMD Ryzen9800X3D
  - MEMORY：64GB
  - GPU：NVIDIA RTX5060Ti 16GB
  - OS：Windows11

## その他

解答編集時の注意点などを記載しています。

- VSCode と Github の Markdown+Tex のパーサが違うため、表示できないことがあります。以下の対策をしてください。
- Tex の **中括弧** がある場合は、ドル記号ではなく、全体をmathコードブロックで囲んでください。
```codeblock
 |```math
 |\left\{ ... \right\}
 |```
```
- Tex の **アスタリスク** が正しく表示できない場合は、代替文字を使用してください。
```codeblock
 |{H^*} → {H^{\ast}}
```
- Tex の短めのインライン記載が正しく表示できない場合は、バッククォートで囲んでください。
```codeblock
 | $J$ → $`J`$
```
- 文字列の途中に Tex が埋め込まれている場合、Tex の前後（ドル記号）に半角スペースがないと正しく表示されません。
```codeblock
 | あいう$J$かきく → あいう $J$ かきく
```
