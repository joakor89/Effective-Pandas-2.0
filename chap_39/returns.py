
def np_returns(df, col):
    values = df[col].to_numpy()

    shifted = shift(values, 1, cval=np.NaN)

    res = np.round(
        np.subtract(
            np.exp(
                np.nancumsum(
                    np.log(
                        np.divide(values, shifted)
                    )
                )
            ),
            1
        ),
        3
    )

    res[0] = np.NaN

    return pd.Series(res, index=df.index)
