import json
import re
import textwrap


TYPES = {
    "String": "str", 
    "Boolean": "bool", 
    "Integer": "int", 
    "Float": "float"
}


def camel_to_snake(name):
    # https://stackoverflow.com/q/1175208
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()


class Generator:
    def __init__(
        self,
        name: str, 
        description: list[str], 
        fields: list[str], 
        subtypes: list[str]
    ):
        self.name = name
        self.description = description
        self.fields = fields
        self.subtypes = subtypes

    def get_file_name(self):
        return camel_to_snake(self.name)

    def get_description(self):
        description = ""

        for i, x in enumerate(self.description):
            description += textwrap.fill(
                x,
                initial_indent="" if i == 0 else "\n    ",
                subsequent_indent="    ",
                break_long_words=False
            )

        if self.fields:
            description += "\n\n    Parameters:"

        for i, x in enumerate(self.fields):
            field = self.get_description_field(
                x["name"],
                x["types"],
                x["required"],
                x["description"]
            )
            if i == 0:
                description += f"\n{field}"
            else:
                description += f"\n\n{field}"

        return description
    
    def get_description_field(
        self, 
        name: str, 
        types: list[str], 
        required: bool, 
        description: str
    ):
        if name == "from":
            field = f"        from_user ("
        else:
            field = f"        {name} ("

        if len(types) == 1:
            field += f"{self.types_to_description(types[0])}"
        else:
            field += " | ".join(map(self.types_to_description, types))
        
        field += f"{self.is_optional(required)}):"

        field += textwrap.fill(
            description.replace("Optional. ", ""),
            initial_indent="\n            ",
            subsequent_indent="            ",
            break_long_words=False
        )

        field += "."

        return field.replace("..", ".")

    def types_to_description(self, types: str):
        if TYPES.get(types, None):
            return f"``{TYPES[types]}``"
        elif "Array" in types:
            # Array of String --> List of ``str``
            types_list = types.split("Array of ", maxsplit=1)[1]
            return f"List of {self.types_to_description(types_list)}"
        else:
            return f"`~pybotgram.types.{types}`"

    is_optional = lambda _, optional: "" if optional else ", *optional*"


def main():
    with open("api.json", "r") as f:
        docs = json.load(f)
    
    # test
    update = docs["types"]["Update"]
    gen = Generator(update["name"], update["description"], update["fields"], [])
    print(gen.get_file_name())
    print(gen.get_description())


if __name__ == "__main__":
    main()
