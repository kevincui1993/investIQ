import click

from investiq.stock_analyzer import StockAnalyzer


@click.command()
@click.option('--stock_symbols',
              type=click.STRING,
              help='a list of comma separated stock symbols to compare')
def main(stock_symbols: str):
    stock_analyzer = StockAnalyzer(stock_symbols.split(','))
    print(stock_analyzer.recommend())


if __name__ == "__main__":
    main()
