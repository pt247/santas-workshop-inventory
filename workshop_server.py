# workshop_server.py
from typing import List
from fastmcp import FastMCP
import asyncio
import json

# Initialize FastMCP server
mcp = FastMCP(name="santas-workshop-inventory")

# A single, shared in-memory database for demonstration
INVENTORY_DB = {
    "Teddy Bear": {"stock": 100, "produced": 0},
    "Toy Train": {"stock": 50, "produced": 0},
    "Doll": {"stock": 200, "produced": 0},
}

@mcp.tool()
def get_toy_stock(toy_name: str) -> dict:
    """
    Retrieves the current stock levels for a specific toy.

    Args:
        toy_name: The name of the toy (e.g., "Teddy Bear", "Toy Train", "Doll").

    Returns:
        A dictionary with the current 'stock' and 'produced' count.
    """
    if toy_name in INVENTORY_DB:
        return {
            "toy_name": toy_name,
            "stock": INVENTORY_DB[toy_name]["stock"],
            "produced": INVENTORY_DB[toy_name]["produced"],
        }
    else:
        raise ValueError(f"Toy '{toy_name}' not found in inventory.")

@mcp.tool()
async def produce_toys(toy_name: str, quantity: int) -> str:
    """
    Simulates the production of a specific quantity of toys.

    Args:
        toy_name: The name of the toy.
        quantity: The number of toys to produce.

    Returns:
        A status message once production is complete.
    """
    if toy_name not in INVENTORY_DB:
        raise ValueError(f"Toy '{toy_name}' not found in inventory.")

    print(f"Elf workshop is producing {quantity} {toy_name}s...")
    await asyncio.sleep(2) # Simulate work/database latency

    INVENTORY_DB[toy_name]["stock"] += quantity
    INVENTORY_DB[toy_name]["produced"] += quantity

    return f"Successfully produced {quantity} {toy_name}s. New stock: {INVENTORY_DB[toy_name]['stock']}"

@mcp.resource("inventory://all_stock")
def get_full_inventory() -> List[dict]:
    """Provides the full current inventory list as a resource."""
    return [{"name": name, **details} for name, details in INVENTORY_DB.items()]

if __name__ == "__main__":
    # This entry point runs the server using the default STDIO transport for local clients
    print("🎄 Starting Santa's Workshop Inventory MCP Server...")
    mcp.run()
