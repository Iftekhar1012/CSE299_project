import re

def extract_sheet_id(sheet_link):
    """
    Extracts the ID part from a Google Sheets link.
    
    Args:
        sheet_link (str): The Google Sheets link.
        
    Returns:
        str: The extracted ID part of the link, or None if not found.
    """
    pattern = r"/d/([a-zA-Z0-9-_]+)"
    match = re.search(pattern, sheet_link)
    if match:
        return match.group(1)
    else:
        return None

# Example usage:
sheet_link = "https://docs.google.com/spreadsheets/d/13m82LlEeHzvgZ3iLTByvFp21mjG5-gXC6rezX0qcjYM/edit#gid=0"
sheet_id = extract_sheet_id(sheet_link)
print("Google Sheet ID:", sheet_id)