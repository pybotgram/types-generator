<p align="center">
    <b>Telegram types generator for Python</b>
</p>

## Types Generator
### recommendations
Types with subtypes doesn't generate from this generator.
They are:
```
ChatMember
BotCommandScope
MenuButton
InputMedia
InlineQueryResult
InputMessageContent
PassportElementError
```
An example can be found [here](types_prefabricated)
### what does it contain?
This repo contains a script for generate a JSON file (with docs of telegram).
The JSON file is after used to generate the types with `build_types` script.