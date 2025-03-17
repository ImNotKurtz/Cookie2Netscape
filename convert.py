import json
import os
import time

def print_hacker_text(text, delay=0.05):
    """ Prints text with a hacker-style effect """
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def convert_to_netscape(json_file, netscape_file):
    """Converts a JSON cookie file to Netscape format."""
    try:
        print_hacker_text("\n[+] Starting cookie conversion...\n", 0.05)

        with open(json_file, "r", encoding="utf-8") as f:
            cookies = json.load(f)

        with open(netscape_file, "w", encoding="utf-8") as f:
            f.write("# Netscape HTTP Cookie File\n")
            f.write("# Automatically generated - Use wisely 😈\n")
            f.write("# domain\tflag\tpath\tsecure\texpiration\tname\tvalue\n")

            for cookie in cookies:
                domain = cookie.get("domain", "")
                flag = "TRUE" if domain.startswith(".") else "FALSE"
                path = cookie.get("path", "/")
                secure = "TRUE" if cookie.get("secure", False) else "FALSE"
                expiration = str(int(cookie.get("expirationDate", 0)))
                name = cookie.get("name", "")
                value = cookie.get("value", "")

                f.write(f"{domain}\t{flag}\t{path}\t{secure}\t{expiration}\t{name}\t{value}\n")

        print_hacker_text("[✅] Conversion completed! File saved as 'cookies_netscape.txt'\n", 0.03)
    except Exception as e:
        print_hacker_text(f"[❌] Error during conversion: {e}", 0.03)

if __name__ == "__main__":
    # Clear the screen before starting
    os.system("cls" if os.name == "nt" else "clear")  # Clear the screen

    print_hacker_text("""        
        _  __          _       
       | |/ /   _ _ __| |_ ____
       | ' / | | | '__| __|_  /
       | . \ |_| | |  | |_ / / 
       |_|\_\__,_|_|   \__/___|
                         

        C O O K I E  2  N E T S C A P E
    """, 0.01)

    directory = "cookies_converter"  # Make sure the folder is named this
    os.makedirs(directory, exist_ok=True)

    # Check if the Netscape file already exists
    netscape_path = os.path.join(directory, "cookies_netscape.txt")

    if os.path.exists(netscape_path):
        print_hacker_text(f"[⚠️] Cookies have already been converted and saved as '{netscape_path}'.", 0.05)
    else:
        # List all .json and .txt files in the folder
        files = [f for f in os.listdir(directory) if f.endswith((".json", ".txt"))]

        if files:
            # Get the first .json or .txt file found
            json_path = os.path.join(directory, files[0])
            
            # Make sure the file exists and is readable
            if not os.path.exists(json_path):
                print_hacker_text(f"[❌] File not found: {json_path}", 0.05)
            else:
                try:
                    # Try to load the file as JSON
                    with open(json_path, "r", encoding="utf-8") as f:
                        cookies = json.load(f)  # Try to parse it as JSON
                    
                    # Convert cookies to Netscape format
                    convert_to_netscape(json_path, netscape_path)
                except json.JSONDecodeError:
                    print_hacker_text(f"[❌] Error: The file '{json_path}' is not valid JSON.", 0.05)
        else:
            print_hacker_text(f"[❌] No .json or .txt files found in '{directory}'.", 0.05)
