# Santa's Workshop Inventory MCP Server

This project demonstrates the efficiency of sharing a single Model Context Protocol (MCP) server instance versus running multiple dedicated instances. It uses a festive "Santa's Workshop Inventory" theme, built with the lightweight FastMCP framework in Python.

## Project Structure

* `README.md`: This file.
* `workshop_server.py`: FastMCP server logic and tools.
* `requirements.txt`: Python dependencies.

## Getting Started

### Prerequisites

* Python 3.10+
* `uv` package manager

### 1. Clone the repository

```bash
git clone https://github.com/<your-org>/santas-workshop-inventory.git
cd santas-workshop-inventory
```

### 2. Create a virtual environment (optional but recommended)

```bash
uv venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
uv pip install -r requirements.txt
```

### 4. Run the MCP server

The server uses FastMCP's default STDIO transport. Start it locally and connect with your MCP-compatible client:

```bash
python workshop_server.py
```

## Available tools

The MCP server exposes these tools (see `workshop_server.py` for details):

- `get_toy_stock(toy_name)`: Fetch current stock and produced counts for a toy.
- `produce_toys(toy_name, quantity)`: Simulate producing toys and update inventory.
- Resource `inventory://all_stock`: Returns the full inventory list.

## Presenting the slides

1. Install dev extras (includes Jupyter/nbconvert for Reveal.js slides):
   ```bash
   uv pip install -r requirements-dev.txt
   ```
   or with `pip`:
   ```bash
   pip install -r requirements-dev.txt
   ```
2. Serve the deck as slides:
   ```bash
   jupyter nbconvert --to slides santas_workshop_slides.ipynb --post serve
   ```
   This starts a local server and opens the Reveal.js slideshow. You can also open the notebook in Jupyter and use *View > Cell Toolbar > Slideshow* to tweak slide breaks.

## Using with Codex

- **Codex starts its own instance (one per session)**  
  Add an entry to your Codex config (`~/.codex/config.toml`) so each session launches a fresh STDIO server:
  ```toml
  [mcp_servers."santas-workshop-inventory"]
  command = "/Users/prashant/code/santas-workshop-inventory/.venv/bin/python"
  args = ["workshop_server.py"]
  cwd = "/Users/prashant/code/santas-workshop-inventory"
  transport = "stdio"
  ```

- **Reuse a single shared server for all Codex sessions**  
  Start the server once with an HTTP transport, then point Codex at it:
  ```bash
  cd /Users/prashant/code/santas-workshop-inventory
  . .venv/bin/activate
  python run_http_server.py --host 127.0.0.1 --port 8765 --path /mcp
  ```
  Update Codex config to reuse that server (note the `/mcp` path):
  ```toml
  [mcp_servers."santas-workshop-inventory"]
  transport = "http"
  url = "http://127.0.0.1:8765/mcp"
  ```
  If you prefer a different path, pass `--path /your-path` and mirror it in the `url` above.
