###############################
#  TOOLS
from transaction_db import TransactionDb

from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("icarus-tools")


@mcp.tool()
async def get_current_user() -> str:
    """Returns the current user,

    Returns:
        The current user ID
    """
    db = TransactionDb()
    user = db.get_user(1)
    db.close()
    return user


@mcp.tool()
async def get_transactions(userId: str | int) -> str:
    """Returns the transactions associated to the userId provided by running this query: SELECT * FROM Transactions WHERE userId = ?.

    Args:
        userId: The userId to search transactions for

    Returns:
        The list of transactions for the provided userId
    """
    try:
        if isinstance(userId, dict):
            userId = str(userId["userId"])
        if isinstance(userId, int):
            userId = str(userId)

        db = TransactionDb()
        transactions = db.get_user_transactions(userId)
        db.close()
        return transactions

    except Exception as e:
        return f"Error: {e}'"


if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')
