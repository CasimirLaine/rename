import getopt
import glob
import os
import sys

import rename
from rename import strategy
from rename.file import config


class Option:
    def __init__(self, short_option, long_option, description, function):
        self.short_option = short_option
        self.long_option = long_option
        self.description = description
        self.function = function


def print_help():
    if not sys.argv:
        return
    program_name = sys.argv[0]
    print("Usage:")
    print("\t", program_name, ARG_RANDOM)
    print("\t", program_name, ARG_SEQUENTIAL, "<min_char_count>")
    print("\t", program_name, "[options]")
    print()
    print("Options:")
    for option in SUPPORTED_OPTIONS:
        print("\t", option.short_option, option.long_option, "\t", option.description)


def print_version():
    print(rename.PROGRAM_NAME, rename.PROGRAM_VERSION)


SHORT_HELP = "h"
SHORT_VERSION = "v"
LONG_HELP = "help"
LONG_VERSION = "version"

SUPPORTED_OPTIONS = [
    Option(SHORT_HELP, LONG_HELP, "Show this screen.", print_help),
    Option(SHORT_VERSION, LONG_VERSION, "Show version.", print_version)
]

ARG_RANDOM = "random"
ARG_SEQUENTIAL = "sequential"


def _short_opts_str():
    keys = ""
    for option in SUPPORTED_OPTIONS:
        keys += option.short_option
    return keys


def _long_opts_list():
    long_opts = []
    for option in SUPPORTED_OPTIONS:
        long_opts.append(option.long_option)
    return long_opts


class Program:
    def __init__(self, program_args):
        self.program_args = program_args
        self.naming_strategy = None
        self.files_to_rename = None
        self.options = None
        if len(program_args) < 2:
            return
        if program_args[1] == ARG_RANDOM:
            self.naming_strategy = strategy.RandomNamingStrategy()
        elif program_args[1] == ARG_SEQUENTIAL:
            self.naming_strategy = strategy.SequentialNamingStrategy(
                int(program_args[2]) if len(program_args) >= 3 else 0)
        if self.naming_strategy:
            configuration = config.Config()
            self.files_to_rename = []
            for file_type in configuration.file_types_regex:
                self.files_to_rename.extend(
                    glob.glob(os.path.join(rename.get_file_context(), file_type), recursive=False))
        try:
            self.options, args = getopt.gnu_getopt(program_args, _short_opts_str(), _long_opts_list())
        except getopt.GetoptError:
            pass

    def start(self):
        if self.process_options():
            return
        if self.naming_strategy:
            for file in self.files_to_rename:
                try:
                    os.rename(file, os.path.join(rename.get_file_context(), self.naming_strategy.get_name(file)))
                except FileExistsError:
                    print("File already exists with that name!")
        else:
            print_help()

    def process_options(self):
        if not self.options:
            return False
        for opt, arg in self.options:
            for supported_option in SUPPORTED_OPTIONS:
                if opt.removeprefix("-") == supported_option.short_option \
                        or opt.removeprefix("--") == supported_option.long_option:
                    supported_option.function()
                    return True
        return False
