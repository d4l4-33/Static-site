




def markdown_to_blocks(markdown):
    nodes = []
    blocks = markdown.split("\n\n")
    for block in blocks:
        if block == "":
            continue
        nodes.append(block.strip())
    return nodes
