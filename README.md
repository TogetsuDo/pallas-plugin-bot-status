# pallas-plugin-bot-status

Pallas-Bot 4.0 官方扩展：**牛牛状态**（在吗、报数、离线邮件）。

## 安装

需已安装 [Pallas-Bot](https://github.com/PallasBot/Pallas-Bot) **≥ 4.0**。

```bash
# 在本体项目中
uv sync --extra plugins-bot-status

# 或单独安装本包
uv pip install pallas-plugin-bot-status
```

开发联调：clone 本仓库后在本体目录 `uv pip install -e ../pallas-plugin-bot-status`。

## 功能说明

- **牛牛在吗**：列出在线/离线牛牛（名册范围可配置）
- **牛牛报数 / 牛牛出列**：群内在线牛牛依次报到（分片模式自动协调）
- **测试邮件**：验证 SMTP 配置
- **离线通知**：断线超过宽限时间后向配置邮箱与群管 QQ 邮箱发信

### 用户命令

| 口令 | 场景 | 说明 |
| --- | --- | --- |
| 牛牛在吗 | 群内或私聊 | 号主查在线/离线 |
| 牛牛报数 / 牛牛出列 | 群内 | 在线牛牛依次报到 |
| 测试邮件 | 群内或私聊 | 超管测邮件通知 |

### 命令权限

| 命令 ID | 默认等级 |
| --- | --- |
| `bot_status.status` | bot_moderator |
| `bot_status.count` | everyone |
| `bot_status.test_mail` | superuser |

### 配置

WebUI **插件 → 牛牛状态**：SMTP、通知邮箱、离线宽限、`在吗` 名册模式（`auto` / `session` / `fleet` / `connected`）。

## 多进程分片

启用分片时各 worker 须安装相同版本；**牛牛报数** 经本体 `plugin_coord` 协调顺序。

## 许可证

与 [Pallas-Bot](https://github.com/PallasBot/Pallas-Bot) 相同（见 `LICENSE`）。
