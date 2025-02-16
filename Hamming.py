def hamming_distance(str1, str2):
    """
    Computes the Hamming distance between two strings, padding the shorter one.

    Args:
        str1 (str): First string.
        str2 (str): Second string.

    Returns:
        int: Hamming distance (number of differing characters).
    """
    max_len = max(len(str1), len(str2))
    str1 = str1.ljust(max_len, "_")  # Pad with underscores
    str2 = str2.ljust(max_len, "_")

    return sum(1 for x, y in zip(str1, str2) if x != y)

# Example usage
slack_username = "xaviwho"
twitter_handle = "kanuxvi"

distance = hamming_distance(slack_username, twitter_handle)
print(f"Hamming Distance: {distance}")
