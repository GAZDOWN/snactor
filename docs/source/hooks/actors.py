#!/bin/python

import os

import yaml

# import jinja2


TAG_SEPARATED = {}


def generate_underline(char, repeat):
    return "{}\n\n".format(str(char) * int(repeat))


def generate_underline_for(string, underline_with="="):
    return generate_underline(underline_with, len(string))


def render_doc_file(tag, path):
    doc_path = os.path.join(path, "{}.rst".format(tag.replace("-", "_").lower()))

    with open(doc_path, "w") as doc_file:
        doc_file.write("{}\n".format(tag.title()))
        doc_file.write(generate_underline_for(tag, "="))

        for name, attributes in sorted(TAG_SEPARATED[tag].items()):
            definition_path = attributes["path"]

            doc_file.write("{}\n".format(name))
            doc_file.write(generate_underline_for(name, "^"))

            with open(definition_path, "r") as definition_file:
                definition = yaml.load(definition_file)
                description = definition.get("description", None)
                doc_file.write(description)
                doc_file.write("\n")

                doc_file.write("**Tags:** ")
                first = True
                for t in attributes["tags"]:
                    if not first:
                        doc_file.write(", ")
                    else:
                        first = False

                    doc_file.write(":doc:`{}`".format(t))

                doc_file.write("\n")
                doc_file.write("\n")


def parse_definition(name, definition_path):
    print("parsing {} found in {}".format(name, definition_path))

    with open(definition_path, "r") as definition_file:
        definition = yaml.load(definition_file)
        description = definition.get("description", None)
        if description is None:
            print("Actor {} has no description, ignoring...".format(name))
            return

        tags = definition.get("tags", ["untagged"])

        for tag in tags:
            item = {name: {"path": definition_path, "tags": tags}}

            if TAG_SEPARATED.get(tag, None) is None:
                TAG_SEPARATED[tag] = item
            else:
                TAG_SEPARATED[tag].update(item)


def find_actors(path):
    for root, dirs, files in os.walk(path):
        if '_actor.yaml' in files:
            parse_definition(os.path.basename(root), os.path.join(root, '_actor.yaml'))
        else:
            for f in files:
                filename, ext = os.path.splitext(f)
                if not filename.startswith('.') and ext.lower() == '.yaml':
                    parse_definition(filename, os.path.join(root, f))


def generate_dynamic(src_path, dst_path):
    """
    :param src_path: path to actors root
    :type src_path: string

    :param src_path: path to folder where the generated templates will be stored
    :type src_path: string
    """
    find_actors(src_path)

    for tag in TAG_SEPARATED.keys():
        render_doc_file(tag, dst_path)
