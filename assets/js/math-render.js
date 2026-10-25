document.addEventListener("DOMContentLoaded", () => {
  // ```math ... ``` から変換されたコードブロックを探す
  document.querySelectorAll(
    "pre > code.language-math, pre > code.math"
  ).forEach((code) => {
    const pre = code.parentElement;
    const container = document.createElement("div");
    container.className = "math-display";
    pre.replaceWith(container);

    try {
      katex.render(code.textContent, container, {
        displayMode: true,
        throwOnError: false,
        strict: "ignore"
      });
    } catch (error) {
      container.textContent = code.textContent;
      console.error("KaTeX rendering error:", error);
    }
  });

  // 通常の $...$ と $$...$$ を描画
  renderMathInElement(document.body, {
    delimiters: [
      { left: "$$", right: "$$", display: true },
      { left: "$", right: "$", display: false }
    ],
    ignoredTags: [
      "script", "noscript", "style",
      "textarea", "pre", "code", "option"
    ],
    throwOnError: false,
    strict: "ignore"
  });
});
