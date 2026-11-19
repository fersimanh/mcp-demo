# In-class Activity 22: MCP and the Python SDK

## Part 3: FastAPI test
Screenshot of `/docs` showing `{"species": "setosa"}` goes here.

## Part 4: Compare `classify_iris` and `predict`

**Which one does the actual prediction?**
`predict` in `api.py` does. It's the one that loads the trained model and calls `model.predict`. `classify_iris` doesn't know anything about irises or machine learning. It just sends the four numbers to the API and passes back the answer.

**What does the MCP version add?**
It makes the function something an AI app can find and use on its own. It gives the function a name, a plain-English description, and a list of inputs with their types, all in a standard format. The API already worked, but an AI had no way to know it existed or what it was for. MCP adds that.

## Part 5: Be the AI App
Screenshot of `uv run client.py` output goes here.

**Where did the tool name, description and inputs come from in `mcp_server.py`?**
- **Name:** the function name, `classify_iris`.
- **Description:** the docstring right under the function.
- **Inputs:** the function's parameters and their type hints (`sepal_length: float`, etc.).

I never wrote any of this separately. The MCP library reads it straight from the function.

**Who is `/docs` written for, and who is the client output written for?**
`/docs` is written for human developers, so they can read it and try the API by hand. The client output is written for an AI model, so it can read the description and decide whether this tool fits what the user is asking.

**Change the docstring to `"""Does a calculation."""`: would an LLM know to call this tool for "What kind of iris is this?"**
No. "Does a calculation" doesn't say anything about irises, flowers or classification, so an LLM would have no reason to connect it to the question. This shows the docstring isn't just a code comment. It's the instruction the LLM reads to decide when to use the tool, so it's really written for the LLM. (I put the original docstring back afterwards.)

## Part 6: Second tool
Screenshot of the client output showing both tools and the probabilities goes here.

I added a `/probabilities` endpoint to `api.py` and an `iris_probabilities` tool in `mcp_server.py`. Its docstring says it returns a probability for each species and tells the model to use it instead of `classify_iris` when the user asks how sure the model is or when the flower looks borderline.

**How sure is the model about 6.0, 2.7, 5.1, 1.6?**
Not very. It gave setosa 0.0, versicolor 0.68 and virginica 0.32. It's pretty confident it isn't setosa, but it's about two-to-one between versicolor and virginica, so this is a borderline flower. `classify_iris` would just say "versicolor" and hide that uncertainty, which is why the probabilities tool is useful.

## Part 7: Reflect

**Does our team's prototype need an MCP server?**
Probably not. Our own code can just call our API directly, and MCP only adds extra work: another layer to write and maintain. MCP matters when someone else's AI app, like Claude Desktop or Cursor, needs to find and use our tools without us writing custom code for each one. It would become a yes if we wanted outside AI assistants to use our product's features, if we had several tools an LLM should choose between on its own, or if we wanted other teams to plug into our service without building their own integration.
