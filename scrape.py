import json
import re

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
    "types": {},
    "methods": {}
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


def get_types_tg(t: str):
    pref = ""
    if t.startswith("Array of "):
        pref = "Array of "
        t = t[len("Array of "):]
    
    types = [
        z 
        for x in t.split(" or ") 
        for y in x.split(", ") 
        for z in y.split(" and ")
    ]
    return [f"{pref}{get_types(x)}" for x in types]


def get_return(current_name):
    desc = "\n".join(RESULT["methods"][current_name]["description"])
    ret_search = re.search(
        "(?:on success,|returns)([^.]*)(?:on success)?", 
        desc, 
        re.IGNORECASE
    )
    ret_search2 = re.search("([^.]*)(?:is returned)", desc, re.IGNORECASE)
    if ret_search:
        extract_return(current_name, ret_search.group(1))
    else:
        extract_return(current_name, ret_search2.group(1))


def extract_return(c: str, t: str):
    array_match = re.search(r"((?:array of )+\w*)", t, re.IGNORECASE)
    if array_match:
        types = get_types_tg(array_match.group(1))
    else:
        types = [
            y 
            for x in t.split() 
            for y in get_types_tg(x) 
            if x[0].isupper()
        ]
    
    RESULT["methods"][c]["returns"] = types


def scrape():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")
    dev_rules = soup.find("div", {"id": "dev_page_content"})

    current_name = ""
    current_type = ""

    for x in dev_rules.children:
        if x.name == "h3" or x.name == "hr":
            current_name = ""
            current_type = ""

        if x.name == "h4":
            anchor = x.find("a")
            name = anchor.get("name")
            current_name = x.get_text()
            current_type = "types"

            if "-" in name:
                current_name = ""
                current_type = ""
                continue

            if not current_name[0].isupper():
                current_type = "methods"

            print(f"current types/methods: {current_name}")
            
            RESULT[current_type][current_name] = {
                "name": current_name,
                "href": f"{URL}#{name}"
            }
        
        if not current_name or not current_type:
            continue

        if x.name == "p":
            RESULT[current_type][current_name].setdefault(
                "description", 
                []
            ).extend(get_description(x))

        if x.name == "table":
            tbody = x.find("tbody")
            fields = RESULT[current_type][current_name]["fields"] = []

            for tr in tbody.find_all("tr"):
                children = list(tr.find_all("td"))

                if len(children) == 3 and current_type == "types":
                    desc = "\n".join(get_description(children[2]))
                    fields.append(
                        {
                            "name": children[0].get_text(),
                            "types": get_types_tg(children[1].get_text()),
                            "required": not desc.startswith("Optional. "),
                            "description": desc
                        }
                    )
                elif len(children) == 4 and current_type == "methods":
                    desc = "\n".join(get_description(children[3]))
                    fields.append(
                        {
                            "name": children[0].get_text(),
                            "types": get_types_tg(children[1].get_text()),
                            "required": children[2].get_text() == "Yes",
                            "description": desc
                        }
                    )
                else:
                    print(f"Error: {current_name}")

        if x.name == "ul":
            subtypes = []
            for li in x.find_all("li"):
                subtypes.extend(get_description(li))
            
            RESULT["types"][current_name]["subtypes"] = subtypes

            for x in subtypes:
                RESULT["types"][current_name]["description"].append(f"- {x}")

        if (
            current_type == "methods" and 
            RESULT["methods"][current_name].get("description")
        ):
            get_return(current_name)


def main():
    print("Starting scrape")
    scrape()

    for k, v in RESULT["types"].items():
        for x in v.get("subtypes", []):
            RESULT["types"][x].setdefault("subtype_of", []).append(k)

    with open("api.json", "w") as f:
        json.dump(RESULT, f, indent=4)

    print(f"Total types: {len(RESULT['types'])}")    
    print("Finish")


if __name__ == "__main__":
    main()