import pytest
import viz
import numpy as np
import pandas as pd


@pytest.mark.skip(reason="no way of currently testing this")
def test_plot_correlations():
    assert False


@pytest.fixture()
def get_sample_geodata():
    df = pd.read_csv('./tests/test_data.csv', index_col=False).drop('Unnamed: 0', axis=1)
    return df


def test_get_pca_cols(get_sample_geodata):
    cols = viz.get_pca_cols(get_sample_geodata)
    assert cols == ['amk', 'he_kika', 'he_naiset', 'hr_hy_tul', 'hr_ke_tul',
                    'hr_ovy', 'hr_pi_tul', 'pt_0_14', 'pt_elakel', 'pt_opisk', 'pt_tyoll', 'pt_tyott',
                    'pt_tyovu', 'ra_as_kpa', 'ra_asrak', 'ra_asunn', 'ra_ke', 'ra_kt_as', 'ra_muut', 'ra_pt_as',
                    'ra_raky', 'te_aik', 'te_as_valj', 'te_eil_np', 'te_elak', 'te_laps', 'te_nuor', 'te_omis_as',
                    'te_takk', 'te_vuok_as', 'tp_alku_a', 'tp_jalo_bf', 'tp_palv_gu', 'tp_tyopy', 'tr_hy_tul',
                    'tr_ke_tul',
                    'tr_mtu', 'tr_pi_tul', 'yliopistot']


def test_get_pca_data(get_sample_geodata):
    cols = viz.get_pca_cols(get_sample_geodata)
    data_to_pca = get_sample_geodata.loc[get_sample_geodata["pono.level"] == 5, :]
    # select year
    data_to_pca = data_to_pca.loc[data_to_pca['vuosi'] == 2018, :]
    y_r = np.array(get_sample_geodata.loc[:, ['pono']])
    target_names_r = data_to_pca.loc[:, ['nimi']]['nimi']
    target_names_r.index = range(len(target_names_r))
    x_r = np.array(data_to_pca.loc[:, cols])
    x, y, target_names = viz.get_pca_data(get_sample_geodata, 2018, 5)
    assert (x == x_r).all().all()
    assert (y == y_r).all()
    assert np.all(target_names == target_names_r)


@pytest.fixture()
def get_iris_pca():
    return np.array([[-2.26454173e+00, 5.05703903e-01],
                     [-2.08642550e+00, -6.55404729e-01],
                     [-2.36795045e+00, -3.18477311e-01],
                     [-2.30419716e+00, -5.75367713e-01],
                     [-2.38877749e+00, 6.74767397e-01],
                     [-2.07053681e+00, 1.51854856e+00],
                     [-2.44571134e+00, 7.45626750e-02],
                     [-2.23384186e+00, 2.47613932e-01],
                     [-2.34195768e+00, -1.09514636e+00],
                     [-2.18867576e+00, -4.48629048e-01],
                     [-2.16348656e+00, 1.07059558e+00],
                     [-2.32737775e+00, 1.58587455e-01],
                     [-2.22408272e+00, -7.09118158e-01],
                     [-2.63971626e+00, -9.38281982e-01],
                     [-2.19229151e+00, 1.88997851e+00],
                     [-2.25146521e+00, 2.72237108e+00],
                     [-2.20275048e+00, 1.51375028e+00],
                     [-2.19017916e+00, 5.14304308e-01],
                     [-1.89407429e+00, 1.43111071e+00],
                     [-2.33994907e+00, 1.15803343e+00],
                     [-1.91455639e+00, 4.30465163e-01],
                     [-2.20464540e+00, 9.52457317e-01],
                     [-2.77416979e+00, 4.89517027e-01],
                     [-1.82041156e+00, 1.06750793e-01],
                     [-2.22821750e+00, 1.62186163e-01],
                     [-1.95702401e+00, -6.07892567e-01],
                     [-2.05206331e+00, 2.66014312e-01],
                     [-2.16819365e+00, 5.52016495e-01],
                     [-2.14030596e+00, 3.36640409e-01],
                     [-2.26879019e+00, -3.14878603e-01],
                     [-2.14455443e+00, -4.83942097e-01],
                     [-1.83193810e+00, 4.45266836e-01],
                     [-2.60820287e+00, 1.82847519e+00],
                     [-2.43795086e+00, 2.18539162e+00],
                     [-2.18867576e+00, -4.48629048e-01],
                     [-2.21111990e+00, -1.84337811e-01],
                     [-2.04441652e+00, 6.84956426e-01],
                     [-2.18867576e+00, -4.48629048e-01],
                     [-2.43595220e+00, -8.82169415e-01],
                     [-2.17054720e+00, 2.92726955e-01],
                     [-2.28652724e+00, 4.67991716e-01],
                     [-1.87170722e+00, -2.32769161e+00],
                     [-2.55783442e+00, -4.53816380e-01],
                     [-1.96427929e+00, 4.97391640e-01],
                     [-2.13337283e+00, 1.17143211e+00],
                     [-2.07535759e+00, -6.91917347e-01],
                     [-2.38125822e+00, 1.15063259e+00],
                     [-2.39819169e+00, -3.62390765e-01],
                     [-2.22678121e+00, 1.02548255e+00],
                     [-2.20595417e+00, 3.22378453e-02],
                     [1.10399365e+00, 8.63112446e-01],
                     [7.32481440e-01, 5.98635573e-01],
                     [1.24210951e+00, 6.14822450e-01],
                     [3.97307283e-01, -1.75816895e+00],
                     [1.07259395e+00, -2.11757903e-01],
                     [3.84458146e-01, -5.91062469e-01],
                     [7.48715076e-01, 7.78698611e-01],
                     [-4.97863388e-01, -1.84886877e+00],
                     [9.26222368e-01, 3.03308268e-02],
                     [4.96802558e-03, -1.02940111e+00],
                     [-1.24697461e-01, -2.65806268e+00],
                     [4.38730118e-01, -5.88812850e-02],
                     [5.51633981e-01, -1.77258156e+00],
                     [7.17165066e-01, -1.85434315e-01],
                     [-3.72583830e-02, -4.32795099e-01],
                     [8.75890536e-01, 5.09998151e-01],
                     [3.48006402e-01, -1.90621647e-01],
                     [1.53392545e-01, -7.90725456e-01],
                     [1.21530321e+00, -1.63335564e+00],
                     [1.56941176e-01, -1.30310327e+00],
                     [7.38256104e-01, 4.02470382e-01],
                     [4.72369682e-01, -4.16608222e-01],
                     [1.22798821e+00, -9.40914793e-01],
                     [6.29381045e-01, -4.16811643e-01],
                     [7.00472799e-01, -6.34939277e-02],
                     [8.73536987e-01, 2.50708611e-01],
                     [1.25422219e+00, -8.26200998e-02],
                     [1.35823985e+00, 3.28820266e-01],
                     [6.62126138e-01, -2.24346071e-01],
                     [-4.72815133e-02, -1.05721241e+00],
                     [1.21534209e-01, -1.56359238e+00],
                     [1.41182261e-02, -1.57339235e+00],
                     [2.36010837e-01, -7.75923784e-01],
                     [1.05669143e+00, -6.36901284e-01],
                     [2.21417088e-01, -2.80847693e-01],
                     [4.31783161e-01, 8.55136920e-01],
                     [1.04941336e+00, 5.22197265e-01],
                     [1.03587821e+00, -1.39246648e+00],
                     [6.70675999e-02, -2.12620735e-01],
                     [2.75425066e-01, -1.32981591e+00],
                     [2.72335066e-01, -1.11944152e+00],
                     [6.23170540e-01, 2.75426333e-02],
                     [3.30005364e-01, -9.88900732e-01],
                     [-3.73627623e-01, -2.01793227e+00],
                     [2.82944343e-01, -8.53950717e-01],
                     [8.90531103e-02, -1.74908548e-01],
                     [2.24356783e-01, -3.80484659e-01],
                     [5.73883486e-01, -1.53719974e-01],
                     [-4.57012873e-01, -1.53946451e+00],
                     [2.52244473e-01, -5.95860746e-01],
                     [1.84767259e+00, 8.71696662e-01],
                     [1.15318981e+00, -7.01326114e-01],
                     [2.20634950e+00, 5.54470105e-01],
                     [1.43868540e+00, -5.00105223e-02],
                     [1.86789070e+00, 2.91192802e-01],
                     [2.75419671e+00, 7.88432206e-01],
                     [3.58374475e-01, -1.56009458e+00],
                     [2.30300590e+00, 4.09516695e-01],
                     [2.00173530e+00, -7.23865359e-01],
                     [2.26755460e+00, 1.92144299e+00],
                     [1.36590943e+00, 6.93948040e-01],
                     [1.59906459e+00, -4.28248836e-01],
                     [1.88425185e+00, 4.14332758e-01],
                     [1.25308651e+00, -1.16739134e+00],
                     [1.46406152e+00, -4.44147569e-01],
                     [1.59180930e+00, 6.77035372e-01],
                     [1.47128019e+00, 2.53192472e-01],
                     [2.43737848e+00, 2.55675734e+00],
                     [3.30914118e+00, -2.36132010e-03],
                     [1.25398099e+00, -1.71758384e+00],
                     [2.04049626e+00, 9.07398765e-01],
                     [9.73915114e-01, -5.71174376e-01],
                     [2.89806444e+00, 3.97791359e-01],
                     [1.32919369e+00, -4.86760542e-01],
                     [1.70424071e+00, 1.01414842e+00],
                     [1.95772766e+00, 1.00333452e+00],
                     [1.17190451e+00, -3.18896617e-01],
                     [1.01978105e+00, 6.55429631e-02],
                     [1.78600886e+00, -1.93272800e-01],
                     [1.86477791e+00, 5.55381532e-01],
                     [2.43549739e+00, 2.46654468e-01],
                     [2.31608241e+00, 2.62618387e+00],
                     [1.86037143e+00, -1.84672394e-01],
                     [1.11127173e+00, -2.95986102e-01],
                     [1.19746916e+00, -8.17167742e-01],
                     [2.80094940e+00, 8.44748194e-01],
                     [1.58015525e+00, 1.07247450e+00],
                     [1.34704442e+00, 4.22255966e-01],
                     [9.23432978e-01, 1.92303705e-02],
                     [1.85355198e+00, 6.72422729e-01],
                     [2.01615720e+00, 6.10397038e-01],
                     [1.90311686e+00, 6.86024832e-01],
                     [1.15318981e+00, -7.01326114e-01],
                     [2.04330844e+00, 8.64684880e-01],
                     [2.00169097e+00, 1.04855005e+00],
                     [1.87052207e+00, 3.82821838e-01],
                     [1.55849189e+00, -9.05313601e-01],
                     [1.52084506e+00, 2.66794575e-01],
                     [1.37639119e+00, 1.01636193e+00],
                     [9.59298576e-01, -2.22839447e-02]])


def test_do_pca(get_iris_pca):
    df_iris = pd.read_csv('./tests/iris.csv', index_col=False).drop('Unnamed: 0', axis=1)
    pcomp = get_iris_pca

    x_pca, pipe = viz.do_pca(df_iris.loc[:, ['sepal length', 'sepal width', 'petal length', 'petal width']], 2)
    assert np.allclose(x_pca, pcomp, atol=0.000001)


@pytest.mark.skip(reason="no way of currently testing this")
def test_pca_2d_plot():
    assert True


def test_get_outliers_bool():
    x0 = np.array([1, 2, 3, 1, 2, 3, 10])
    assert (viz.get_outliers_bool(x0) == [False, False, False, False, False, False, True]).all()
    assert (viz.get_outliers_bool(np.array([1, 2, 3])) == [False, False, False]).all()


@pytest.mark.skip(reason="no way of currently testing this")
def test_pca_3d_plot():
    assert True


def test_generate_pca_report(get_iris_pca):
    df_iris = pd.read_csv('./tests/iris.csv', index_col=False).drop('Unnamed: 0', axis=1)
    x_pca, pipe = viz.do_pca(df_iris.loc[:, ['sepal length', 'sepal width', 'petal length', 'petal width']], 2)
    pcomp = viz.generate_pca_report(pipe.named_steps['pca'])
    df_res = pd.DataFrame({"C1": [0.522372, -0.263355, 0.581254, 0.565611],
                           "C2": [0.372318, 0.925556, 0.021095, 0.065416]},
                          index=[0, 1, 2, 3])
    assert np.allclose(pcomp, df_res, atol=0.000001)


@pytest.mark.skip(reason="no way of currently testing this")
def test_pca_plot():
    assert True


@pytest.mark.skip(reason="no way of currently testing this")
def test_exploratory_pca():
    assert True


@pytest.mark.skip(reason="no way of currently testing this")
def test_missing_plot():
    assert True


def test_table_similar_with_names(get_sample_geodata):
    x, y, target_names = viz.get_pca_data(get_sample_geodata, 2018, 5)
    x_pca, pipe = viz.do_pca(x, 5)
    res = viz.table_similar_with_names(get_sample_geodata, "Vattuniemi", ["Lauttasaari", "Ruoholahti - Kamppi"],
                                       target_names, x_pca, cols=["he_kika"])
    df_res = pd.DataFrame({"nimi": ['Vattuniemi', 'Lauttasaari'],
                           "he_kika": [42.0, 40.0],
                           "dist": [0.0, 4.573346]},
                          index=[16, 11])
    assert np.allclose(res.loc[:, ["he_kika", "dist"]], df_res.loc[:, ["he_kika", "dist"]], atol=0.000001)
    assert np.all(res.nimi == df_res.nimi)


@pytest.mark.skip(reason="no way of currently testing this")
def test_visualize_similar_with_names():
    assert True
