<p align="center">
  <img src="./assets/brand-avatar.png" width="220" height="220" alt="牛牛状态">
</p>

<h1 align="center">牛牛状态 pallas-plugin-bot-status</h1>

<p align="center">查看在线情况、群内报数，并在离线时发送邮件提醒。</p>

<p align="center">
  <img alt="官方插件" src="https://img.shields.io/badge/%E5%AE%98%E6%96%B9%E6%8F%92%E4%BB%B6-FE7D37">
  <img alt="控制台插件商店" src="https://img.shields.io/badge/%E6%8E%A7%E5%88%B6%E5%8F%B0-%E6%8F%92%E4%BB%B6%E5%95%86%E5%BA%97-4EA94B">
  <img alt="安装命令" src="https://img.shields.io/badge/uv%20run%20pallas%20ext%20install%20pallas--plugin--bot--status-586069">
  <img alt="PyPI 版本" src="https://img.shields.io/pypi/v/pallas-plugin-bot-status?label=%E7%89%88%E6%9C%AC&color=2563EB">
</p>

## 安装方式

需已安装 [Pallas-Bot](https://github.com/PallasBot/Pallas-Bot) `4.0` 或更高版本。推荐直接在控制台插件商店安装，或在本体项目中执行：

```bash
uv run pallas ext install pallas-plugin-bot-status
```

也可单独安装本包：

```bash
uv pip install pallas-plugin-bot-status
```

## 怎么使用

| 口令 / 触发 | 场景 | 说明 |
| --- | --- | --- |
| `牛牛在吗` | 群内 / 私聊 | 查看在线和离线情况。 |
| `牛牛报数` / `牛牛出列` | 群内 | 在线牛牛依次报到。 |
| `测试邮件` | 群内 / 私聊 | 测试邮件通知配置。 |

> 详细用法、限制条件和可用范围以帮助为主。

## 命令权限

| 命令 ID | 默认等级 |
| --- | --- |
| `bot_status.status` | 号主 |
| `bot_status.count` | 所有人 |
| `bot_status.test_mail` | 仅超管 |

## 配置项

> 可在控制台对应插件页中修改。

牛牛状态的常用配置包括 SMTP、通知邮箱、离线宽限时间和名册范围模式。

## 排障

| 现象 | 处理 |
| --- | --- |
| 收不到邮件 | 检查 SMTP 和通知邮箱配置。 |
| 报数不全 | 检查当前群里是否真的在线，以及分片协调是否正常。 |
| 误报离线 | 调大离线宽限时间。 |

## 实现

源码位置：[`src/pallas_plugin_bot_status/`](./src/pallas_plugin_bot_status/)

关键文件：

- [`__init__.py`](./src/pallas_plugin_bot_status/__init__.py)：注册状态查询、报数和测试邮件命令。
- [`bot_monitor.py`](./src/pallas_plugin_bot_status/bot_monitor.py)：汇总在线状态和群内可见牛牛。
- [`mail_notifier.py`](./src/pallas_plugin_bot_status/mail_notifier.py)：发送离线通知和测试邮件。

实现要点：

- `牛牛在吗` 用于聚合状态，`牛牛报数` 更偏向当前群里的现场点名。
- 邮件通知除了发到配置邮箱，还会尝试发给对应牛牛管理员的 QQ 邮箱。
- 分片模式下，报数和状态统计会受当前配置的名册范围影响。

## 相关链接

- [主仓插件文档](https://PallasBot.github.io/Pallas-Bot-Docs/plugins/bot_status)
- [Pallas-Bot](https://github.com/PallasBot/Pallas-Bot)
