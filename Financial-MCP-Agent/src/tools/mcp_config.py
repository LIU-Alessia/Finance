"""
MCP服务器配置模块 - 包含连接A股MCP服务器的配置信息
"""

import sys


SERVER_CONFIGS = {
    "a_share_mcp_v2": {
        "command": sys.executable,
        "args": [
            "/root/autodl-tmp/Finance/a-share-mcp-is-just-i-need/mcp_server.py"
        ],
        "transport": "stdio",
    }
}