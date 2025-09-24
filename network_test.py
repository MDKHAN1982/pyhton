import requests

def check_network_timeout(url, timeout_seconds=5):
    """
    Checks for a network connection timeout by attempting to reach a given URL.

    Args:
        url (str): The URL to attempt to connect to.
        timeout_seconds (int): The maximum time in seconds to wait for a response.

    Returns:
        bool: True if the connection is successful within the timeout, False otherwise.
    """
    try:
        response = requests.get(url, timeout=timeout_seconds)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        print(f"Successfully connected to {url} within {timeout_seconds} seconds.")
        return True
    except requests.exceptions.Timeout:
        print(f"Connection to {url} timed out after {timeout_seconds} seconds.")
        return False
    except requests.exceptions.ConnectionError:
        print(f"Could not establish a connection to {url}. Network is unreachable or host is down.")
        return False
    except requests.exceptions.RequestException as e:
        print(f"An unexpected error occurred while connecting to {url}: {e}")
        return False

# Example usage:
if __name__ == "__main__":
    target_url = "http://www.google.com"  # You can change this to any URL
    timeout_duration = 3  # Set a shorter timeout for demonstration

    if check_network_timeout(target_url, timeout_duration):
        print("Network connection is stable.")
    else:
        print("Network connection issues detected.")

    # Another example with a potentially unreachable address or very short timeout
    unreachable_url = "http://localhost:80"
    short_timeout = 1
    if check_network_timeout(unreachable_url, short_timeout):
        print("Network connection is stable (for unreachable URL).")
    else:
        print("Network connection issues detected (for unreachable URL).")