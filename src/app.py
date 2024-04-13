import os
import sys

import click

from .builders.standard_builder import DynamicIniBuilder
from .data_parsers.yaml import YamlParser
from .dto.enums import BuilderEnum, ParserEnum

map_parser_to_class = {ParserEnum.YAML.value: YamlParser}

map_builder_to_class = {BuilderEnum.STANDARD.value: DynamicIniBuilder}


@click.command()
# @click.option("-d", "--debug", type=bool, is_flag=True, default=False, help="Enable logging in application")
@click.option(
    "--parser",
    type=str,
    default=ParserEnum.YAML.value,
    show_default=True,
    help=f"Parser to use. Available options: {ParserEnum.values()}",
)
@click.option(
    "--builder",
    type=str,
    default=BuilderEnum.STANDARD.value,
    show_default=True,
    help=f"Builder to use. Available options: {BuilderEnum.values()}",
)
@click.argument("filename", type=str)
def app(
    # debug: bool,
    parser: str,
    builder: str,
    filename: str,
):
    """
    Init function for dnd initiative
    """
    if not (os.path.exists(filename) and os.path.isfile(filename)):
        print(f"Configuration error: file with path '{filename}' does not exist")
        sys.exit(1)

    parser_class = map_parser_to_class.get(parser)
    if not parser_class:
        print(f"Configuration error: invalid parser '{parser}'")
        sys.exit(1)

    builder_class = map_builder_to_class.get(builder)
    if not builder_class:
        print(f"Configuration error: invalid builder '{parser}'")
        sys.exit(1)

    with open(filename, "rb") as f:
        file_data = parser_class().parse(f)
        builder_class(file_data).build()
    # print(parser, builder, filename)


if __name__ == "__main__":
    app()
