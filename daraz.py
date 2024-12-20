import requests

def search_daraz(query):
    url = f"https://www.daraz.pk/catalog/?ajax=true&from=input&json=true&q={query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        if "mods" in data and "listItems" in data["mods"]:
            products = data["mods"]["listItems"]
            with open("daraz_products.txt", "w", encoding="utf-8") as file:
                file.write(f"Found {len(products)} products for '{query}':\n")
                file.write("-" * 50 + "\n")
                
                for product in products:
                    name = product.get("name", "No Name")
                    price = product.get("price", "No Price")
                    image = product.get("image", "No Image")
                    rating = product.get("ratingScore", "No Rating")
                    reviews = product.get("review", "No Reviews")
                    seller_name = product.get("Seller_Name", "No Seller")
                    
                    file.write(f"Title: {name}\n")
                    file.write(f"Price: {price}\n")
                    file.write(f"Rating: {rating}\n")
                    file.write(f"Image: {image}\n")
                    file.write(f"Reviews: {reviews}\n")
                    file.write(f"Seller: {seller_name}\n")
                    file.write("-" * 50 + "\n")
                print(f"Data has been saved to daraz_products.txt.")
        else:
            print(f"No products found for '{query}'.")
    else:
        print(f"Failed to fetch data. Status Code: {response.status_code}")

if __name__ == "__main__":
    user_input = input("Enter a product to search: ").strip()
    search_daraz(user_input)
