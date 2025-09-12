from mcp.server.fastmcp import FastMCP
# Pass host parameter to the FastMCP constructor, not to run()
mcp = FastMCP("server")

@mcp.tool()
def greeting(name: str) -> str:
    "Send a greeting"
    return f"Hi {name}"

if __name__ == "__main__":  # Fix: __name__ instead of **name**
    mcp.run(transport="streamable-http")
