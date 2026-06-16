# AGENTS.md

## 项目

- **名称**：pallas-plugin-bot-status
- **类型**：Pallas-Bot 4.0 官方扩展（NoneBot 插件包）
- **Python**：3.12+
- **依赖**：`uv` · 运行时依赖 [Pallas-Bot](https://github.com/PallasBot/Pallas-Bot) `>=4.0`

## 本地开发

```bash
uv sync --group dev
uv run ruff check src/
uv run ruff format --check src/
```

与本体联调：在本体仓库执行 `uv pip install -e ../pallas-plugin-bot-status`。

## 约定

- 仅改 `src/`；通过 `pallas-bot` 公开 API（`src.features` / `src.platform`）访问内核。
- 提交前 `ruff check` + `ruff format --check` 通过。
