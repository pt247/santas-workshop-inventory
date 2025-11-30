# run_http_server.py
"""
Start the Santa's Workshop MCP server over HTTP so multiple Codex sessions can share it.
Defaults to 127.0.0.1:8765; override with --host/--port if needed.
"""

import argparse

from workshop_server import mcp


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run the Santa's Workshop MCP server over HTTP."
    )
    parser.add_argument("--host", default="127.0.0.1", help="Host interface to bind.")
    parser.add_argument(
        "--port", type=int, default=8765, help="Port to listen on (default: 8765)."
    )
    parser.add_argument(
        "--path",
        default="/mcp",
        help="HTTP path for the MCP endpoint (default: /mcp).",
    )
    args = parser.parse_args()

    path = args.path if args.path.startswith("/") else f"/{args.path}"

    print(
        f"Starting Santa's Workshop MCP server over HTTP on {args.host}:{args.port}{path}..."
    )
    mcp.run(transport="http", host=args.host, port=args.port, path=path)


if __name__ == "__main__":
    main()
