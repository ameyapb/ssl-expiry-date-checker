import requests
from datetime import datetime

def get_ssl_expiry_date(hostname):
    # Send a HEAD request to the website
    response = requests.head(f"https://{hostname}")

    # Retrieve the SSL certificate from the response
    cert = response.request._proxy_conn.sock.getpeercert()

    # Extract the expiry date from the certificate
    expiry_date_str = cert['notAfter']
    expiry_date = datetime.strptime(expiry_date_str, '%b %d %H:%M:%S %Y %Z')

    return expiry_date

# Example usage
website = "example.com"
expiry_date = get_ssl_expiry_date(website)

# Print the SSL expiry date
print(f"The SSL certificate for {website} expires on {expiry_date}")
