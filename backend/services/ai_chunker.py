def chunk_code(code: str, chunk_size: int = 500):
    """
    Split code into chunks of max length `chunk_size`.
    """
    chunks = []
    for i in range(0, len(code), chunk_size):
        chunks.append(code[i:i + chunk_size])
    return chunks