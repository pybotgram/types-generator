import json

import requests
from bs4 import BeautifulSoup, Tag


URL = "https://core.telegram.org/bots/api"
TYPES = {
    "Float number": "Float",
    "Int": "Integer",
    "True": "Boolean",
    "Bool": "Boolean",
}
RESULT = {
    "types": {}
}


def get_description(t: Tag) -> list[str]:
    for br in t.find_all("br"):
        br.replace_with("\n")

    text = t.get_text()
    text = text.replace('”', '"').replace('“', '"')

    return list(map(lambda x: x.strip(), text.split("\n")))


def get_types(t: str):
    if TYPES.get(t, None):
        return TYPES[t]
    elif "Array of" in t:
        types_list = t.split("Array of ", maxsplit=1)[1]
        return f"Array of {types_list}"
    else:
        return t


def scrape():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")
    dev_rules = soup.find("div", {"id": "dev_page_content"})

    current_types = ""

    for x in dev_rules.children:
        if x.name == "h3" or x.name == "hr":
            current_types = ""

        if x.name == "h4":
            anchor = x.find("a")
            name = anchor.get("name")
            current_types = x.get_text()

            if "-" in name or not current_types[0].isupper():
                current_types = ""
                continue

            print(f"current types: {current_types}")
            
            RESULT["types"][current_types] = {
                "name": current_types,
                "href": f"{URL}#{name}"
            }
        
        if not current_types:
            continue

        if x.name == "p":
            RESULT["types"][current_types]["description"] = get_description(x)

        if x.name == "table":
            tbody = x.find("tbody")
            fields = RESULT["types"][current_types]["fields"] = []

            for tr in tbody.find_all("tr"):
                children = list(tr.find_all("td"))
                if len(children) == 3:
                    desc = "\n".join(get_description(children[2]))
                    types = list(map(
                        get_types, 
                        children[1].get_text().split(" or ")
                    ))
                    fields.append(
                        {
                            "name": children[0].get_text(),
                            "types": types,
                            "required": not desc.startswith("Optional. "),
                            "description": desc
                        }
                    )
                else:
                    print(f"Error: {current_types}")

        if x.name == "ul":
            subtypes = []
            for li in x.find_all("li"):
                subtypes.extend(get_description(li))
            
            RESULT["types"][current_types]["subtypes"] = subtypes

            for x in subtypes:
                RESULT["types"][current_types]["description"].append(f"- {x}")


def main():
    print("Starting scrape")
    scrape()

    for k, v in RESULT["types"].items():
        for x in v.get("subtypes", []):
            RESULT["types"][x]["subtype_of"] = k

    with open("api.json", "w") as f:
        json.dump(RESULT, f, indent=4)

    print(f"Total types: {len(RESULT['types'])}")    
    print("Finish")


if __name__ == "__main__":
    main()