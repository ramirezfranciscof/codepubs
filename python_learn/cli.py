################################################################################
#
# Making command line commands with click...
#
# SOURCE:
# > https://dbader.org/blog/python-commandline-tools-with-click
#
################################################################################

import click

@click.command()
def main():
    print("I'm a beautiful CLI!")

if __name__ == "__main__":
    main()

################################################################################
