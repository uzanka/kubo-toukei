# 久保統計の完全解答

[「大学演習　熱学・統計力学」](https://www.amazon.co.jp/dp/4785380322)（久保 亮五 著、裳華房）、通称 **久保統計** の演習問題を、
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
- 問題、解答例は原本を参照してください。
- 取り消し線を引いてあるリンクは未検証の解答です。

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

## その他

解答編集時の注意点などを記載しています。
VSCode はガバガバなので表示できますが、Github の Markdown + Tex は条件が厳しいです。

- Markdown 中に記載する Tex のうち、中括弧を表現する
  ```codeblock
  ・VSCode で表示できて、Github で表示できない。
  \left\{ ... \right\}
  ・Github で表示できて、VSCode で表示できない。
  \left\\{ ... \right\\}
  ```
  が、Github 上では正しく表示されません（Github の Markdown パーサがエスケープシーケンスを勝手に削除してしまう問題）。
  GitHub 上で正しく表示できるようにエスケープシーケンスを重ねています。
  逆に VSCode では表示できません。
  VSCode で閲覧する場合は、エラーになる個所でこのエスケープを1個削除してください。

- Github では、Markdown や Tex の区切り部分に半角スペースがないと正しく表示されません。VSCode で修正・確認する場合は注意が必要です。

- Github では、Markdown 中の Tex に `*` を書くと Markdown が先に解釈してしまい Tex が認識しないことがあります。そのときは、`{\ast}`を使用してください。
