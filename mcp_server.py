from mcp.server.fastmcp import FastMCP

mcp = FastMCP("First MCP Server")

@mcp.tool()
def calculate(expression: str) -> str:
    """Считает математические выражения."""
    result = eval(expression)
    return str(result)

@mcp.tool()
def greet(name: str) -> str:
    """Приветствует пользователя по имени."""
    return f"Привет, {name}!"

if __name__ == "__main__":
    mcp.run()
    