# mcp_server.py
import httpx
from mcp.server.mcpserver import MCPServer

mcp = MCPServer("Iris Classifier", log_level="WARNING")


@mcp.tool()
def classify_iris(sepal_length: float, sepal_width: float, petal_length: float, petal_width: float) -> str:
    """Classify an iris flower from its four measurements, in centimeters.
    Returns the predicted species: setosa, versicolor, or virginica.
    """
    response = httpx.post(
        "http://127.0.0.1:8000/predict",
        json={
            "sepal_length": sepal_length,
            "sepal_width": sepal_width,
            "petal_length": petal_length,
            "petal_width": petal_width,
        },
    )
    return f"Predicted species: {response.json()['species']}"


@mcp.tool()
def iris_probabilities(sepal_length: float, sepal_width: float, petal_length: float, petal_width: float) -> str:
    """Get the model's confidence for each iris species, given four measurements in centimeters.
    Returns a probability (0 to 1) for setosa, versicolor, and virginica.
    Use this instead of classify_iris when the user asks how sure or confident the
    model is, or when the flower might be a borderline case between two species.
    """
    response = httpx.post(
        "http://127.0.0.1:8000/probabilities",
        json={
            "sepal_length": sepal_length,
            "sepal_width": sepal_width,
            "petal_length": petal_length,
            "petal_width": petal_width,
        },
    )
    return f"Species probabilities: {response.json()}"


if __name__ == "__main__":
    mcp.run()
