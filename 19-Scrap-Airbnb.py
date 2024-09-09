import requests
from bs4 import BeautifulSoup

# Send a request to the Airbnb listings page
url = requests.get(
    "https://www.airbnb.com/s/india/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2024-10-01&monthly_length=3&monthly_end_date=2025-01-01&price_filter_input_type=0&channel=EXPLORE&search_type=filter_change&price_filter_num_nights=5&date_picker_type=calendar&source=structured_search_input_header"
)

# Parse the page content with BeautifulSoup
soup = BeautifulSoup(url.text, "lxml")

# Find all listings based on a stable attribute, such as 'data-testid'
name_elements = soup.find_all(
    "div", {"class": "pquyp1l atm_da_cbdd7d pi11895 atm_h3_lh1qj6 dir dir-ltr"}
)
print(name_elements)
# Extract and print the names of the listings
name_list = [name.text for name in name_elements]
print(name_list)
