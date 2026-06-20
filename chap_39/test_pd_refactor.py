
@pytest.fixture
def raw_price_df():
    return pd.read_csv(
        'data/tickers-raw.csv',
        index_col='Date',
        parse_dates=['Date'],
        dtype_backend='pyarrow',
        engine='pyarrow'
    )


def test_basic(raw_price_df):
    assert len(raw_price_df) > 1
