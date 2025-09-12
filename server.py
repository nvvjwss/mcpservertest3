from mcp.server.fastmcp import FastMCP

# Explicitly set host to 0.0.0.0 to allow external connections
mcp = FastMCP("server", host="0.0.0.0", port=8000)

@mcp.tool()
def greeting(name: str) -> str:
    "Send a greeting"
    return f"Hi {name}"

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
