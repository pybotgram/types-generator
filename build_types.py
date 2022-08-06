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

    def get_arguments(self):
        arguments = ""

        if self.fields or self.subtypes:
            arguments += "\n        *,"

        for x in self.fields:
            arguments += "\n        "

            if x["name"] == "from":
                arguments += "from_user: "
            else:
                arguments += f"{x['name']}: "
            
            types = x["types"]
            if len(types)==1:
                data = self.types_to_type(types[0])
                arguments += f"Optional[{data}]" if not x["required"] else data
            else:
                data = ", ".join(map(self.types_to_type, types))
                if not x["required"]:
                    arguments += f"Optional[Union[{data}]]"
                else:
                    arguments += f"Union[{data}]"
            
            arguments += " = None," if not x["required"] else ","
        
        return arguments

    def get_fields(self):
        fields = ""

        for x in self.fields:
            fields += "\n        "

            if x["name"] == "from":
                fields += "self.from_user = from_user"
            else:
                fields += f"self.{x['name']} = {x['name']}"
        
        return fields

    def get_instructions(self):
        instructions = ""

        for x in self.fields:
            if len(x["types"])==1:
                i = self.types_to_instructions(x["name"], x["types"][0])
                if i:
                    if x["name"] == "from":
                        instructions += f"\n        data[\"from_user\"] = "
                    else:
                        instructions += f"\n        data[\"{x['name']}\"] = "
                    instructions += i
        
        if instructions:
            instructions += "\n"
        
        return instructions
    
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
            return f":py:obj:`{TYPES[types]}`"
        elif "Array" in types:
            # Array of String --> List of ``str``
            types_list = types.split("Array of ", maxsplit=1)[1]
            return f"List of {self.types_to_description(types_list)}"
        else:
            return f":obj:`~pybotgram.types.{types}`"

    def types_to_type(self, types: str):
        if TYPES.get(types, None):
            return TYPES[types]
        elif "Array" in types:
            # Array of String --> List[str]
            types_list = types.split("Array of ", maxsplit=1)[1]
            return f"List[{self.types_to_type(types_list)}]"
        else:
            return f"\"types.{types}\""

    def types_to_instructions(self, name, types):
        if TYPES.get(types, None):
            return False
        elif "Array" in types:
            nname = types.split("Array of ")[-1]
            if not TYPES.get(nname, False):
                return f"types.{nname}._parse_list(data.get(\"{name}\"), bot)"
            return False
        else:
            return f"types.{types}._parse(data.get(\"{name}\"), bot)"

    is_optional = lambda _, optional: "" if optional else ", *optional*"


def main():
    with open("api.json", "r") as f:
        docs = json.load(f)
    
    with open("templates/types_class.txt") as f:
        template_class = f.read()
    
    with open("templates/types.txt") as f:
        template_types = f.read()
    
    with open("templates/init.txt") as f:
        template_init = f.read()

    lst_types = []
    
    for x in docs["types"].values():
        name = x["name"]
        subtypes = x.get("subtypes", [])
        class_object = x.get("subtype_of", "Object")

        if subtypes:
            print(f"FIX {name}")
            continue
        elif isinstance(class_object, list):
            continue

        gen = Generator(name, x["description"], x.get("fields", []), subtypes)
        file_name = gen.get_file_name()

        lst_types.append((name, file_name))
            
        import_set = {"Any", "Dict", "Optional"}
        import_types = ""
        arguments = gen.get_arguments()

        if arguments.find("types.") != -1:
            import_types += "\nfrom pybotgram import types"
        if arguments.find("Union") != -1:
            import_set.add("Union")
        if arguments.find("List") != -1:
            import_set.add("List")

        with open(f"types/{file_name}.py", "w") as f:
            f.write(template_types.format(
                import_typing=", ".join(sorted(
                    import_set, 
                    key=len, 
                    reverse=True
                )),
                import_types=import_types,
                content=template_class.format(
                    name=name,
                    class_object=class_object,
                    description=gen.get_description(),
                    arguments=gen.get_arguments(),
                    fields=gen.get_fields(),
                    instructions=gen.get_instructions()
                )
            ))

    with open("types/__init__.py", "w") as f:
        f.write(template_init.format(
            lst_all="\n    ".join([f"\"{x[0]}\"" for x in lst_types]),
            lst_import="\n".join([
                f"from .{x[1]} import {x[0]}" 
                for x in lst_types
            ])
        ))


if __name__ == "__main__":
    main()
