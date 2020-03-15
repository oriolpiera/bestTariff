import click
from curve import *

@click.command()
@click.argument('curves_file')
@click.argument('tariff')
def action(curves_file, tariff):
    tc = TariffCalculator()
    cu = CurveUtils()
    curves = cu.loadCurveFile(curves_file)
    result, allResults = tc.calculator(tariff, curves)
    click.echo("The best tariff for you is: %s" % result)
    print(allResults)

if __name__ == '__main__':
    action()
