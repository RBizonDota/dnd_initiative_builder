import os
import sys

import click

from src.builders.base import BaseIniBuilder
from src.builders.standard_builder import DynamicIniBuilder
from src.data_parsers.base import BaseParser
from src.data_parsers.yaml import YamlParser
from src.dto.enums import BuilderEnum, ParserEnum
from src.web.main import run_web

map_parser_to_class: dict[str, type[BaseParser]] = {ParserEnum.YAML.value: YamlParser}

map_builder_to_class: dict[str, type[BaseIniBuilder]] = {
    BuilderEnum.STANDARD.value: DynamicIniBuilder
}


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
@click.option(
    "-w", "--web", type=bool, is_flag=True, default=False, help="Open web interface"
)
@click.argument("filename", type=str)
def app(
    # debug: bool,
    parser: str,
    builder: str,
    web: bool,
    filename: str,
):
    """
    Init function for dnd initiative
    """
    if not (os.path.exists(filename) and os.path.isfile(filename)):
        print(f"Configuration error: file with path '{filename}' does not exist")
        sys.exit(1)

    parser_class: type[BaseParser] = map_parser_to_class.get(parser)
    if not parser_class:
        print(f"Configuration error: invalid parser '{parser}'")
        sys.exit(1)

    builder_class: type[BaseIniBuilder] = map_builder_to_class.get(builder)
    if not builder_class:
        print(f"Configuration error: invalid builder '{parser}'")
        sys.exit(1)

    file_data = parser_class().parse(filename)

    if not web:
        builder_class(file_data).print_table()
        sys.exit(1)

    run_web(builder_class(file_data))


if __name__ == "__main__":
    app()
