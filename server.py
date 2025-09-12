from mcp.server.fastmcp import FastMCP

# Pass host parameter to the FastMCP constructor, not to run()
mcp = FastMCP()

@mcp.tool()
def greeting(name: str) -> str:
    "Send a greeting"
    return f"Hi {name}"

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
