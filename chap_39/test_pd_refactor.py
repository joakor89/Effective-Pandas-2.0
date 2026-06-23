
@pytest.fixture
def raw_price_df():
    return pd.read_csv(
        'data/tickers-raw.csv',
        index_col='Date',
        parse_dates=['Date'],
        dtype_backend='pyarrow',
        engine='pyarrow'
    )


@pytest.fixture
def raw_price_df_legacy(raw_price_df):
    return raw_price_df


@pytest.fixture
def orig_price_df(raw_price_df_legacy):
    return returns.orig_price_df(raw_price_df_legacy)


def test_basic(orig_price_df):
    assert len(orig_price_df) > 1


def test_refactor(orig_price_df, raw_price_df_legacy):
    price_df_rf = raw_price_df_legacy

    K = 1_000_000

    port_tickers = [
        'QCOM', 'TSLA', 'NFLX', 'DIS',
        'PG', 'MMM', 'IBM', 'BRK-B',
        'UPS', 'F'
    ]

    bm_ticker = '^GSPC'

    ticker_list = [bm_ticker] + port_tickers
    period = '6mo'

    port_rf = returns.get_portfolio(
        port_tickers,
        price_df_rf,
        price_df_rf[bm_ticker]
    )

    new_price_df = returns.get_price(
        price_df_rf,
        bm_ticker,
        port_rf,
        K
    )

    pd.testing.assert_frame_equal(
        new_price_df,
        orig_price_df
    )
