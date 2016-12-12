# Copyright (c) 2016, Vienna University of Technology, Department of Geodesy
# and Geoinformation. All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#   * Redistributions of source code must retain the above copyright
#     notice, this list of conditions and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright
#     notice, this list of conditions and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   * Neither the name of the Vienna University of Technology, Department of
#     Geodesy and Geoinformation nor the names of its contributors may be
#     used to endorse or promote products derived from this software without
#     specific prior written permission.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL VIENNA UNIVERSITY OF TECHNOLOGY,
# DEPARTMENT OF GEODESY AND GEOINFORMATION BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


import os
import unittest
from tempfile import mkdtemp
import pandas as pd
import numpy as np

from pygeobase.io_base import TsBase, StaticBase, ImageBase
from pygeobase.io_base import GriddedBase


class StaticText(StaticBase):

    def __init__(self, filename, mode='r', **kwargs):
        """
        Initialize time series csv read/write object.

        Parameters
        ----------
        filename : str
            CSV filename.
        mode : str, optional
            File opening mode. Default: 'r'
        """
        self.is_open = False
        self.fid = None
        self.data = None
        super(StaticText, self).__init__(filename, mode, **kwargs)

    def _open(self, check=None):
        """"
        Open csv file.

        Parameters
        ----------
        check : str, optional
            Check if file is open. Default: None
        """
        if not self.is_open:
            self.fid = open(self.filename, self.mode)
            self.is_open = True
        else:
            if check and self.fid.mode != check:
                raise RuntimeError('File mode not correct')

    def read(self, gpi):
        """
        Read data for specific grid point.

        Parameters
        ----------
        gpi : int
            Grid point index.
        """
        self._open()

        if self.data is None:
            self.data = pd.read_csv(self.fid)

        pos = np.where(self.data['gpi'] == gpi)[0]

        return self.data.iloc[pos]

    def write(self, data, index_label='gpi'):
        """
        Write data
        """
        self._open()
        data.to_csv(self.fid, index_label=index_label)

    def flush(self):
        """
        Flush to disk.
        """
        self.fid.flush()

    def close(self):
        """
        Close file.
        """
        self.fid.close()

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Exit the runtime context related to this object. The file will be
        closed. The parameters describe the exception that caused the
        context to be exited.
        """
        self.close()

    def __enter__(self):
        """
        Context manager initialization. Open file.

        Returns
        -------
        self : GenericIOStatic object
            self
        """
        return self


class TsText(TsBase):

    def __init__(self, filename, mode='r', **kwargs):
        """
        Initialize time series csv read/write object.

        Parameters
        ----------
        filename : str
            CSV filename.
        mode : str, optional
            File opening mode. Default: 'r'
        """
        self.is_open = False
        self.fid = None
        self.data = None
        super(TsText, self).__init__(filename, mode, **kwargs)

    def _open(self, check=None):
        """"
        Open csv file.

        Parameters
        ----------
        check : str, optional
            Check if file is open. Default: None
        """
        if not self.is_open:
            self.fid = open(self.filename, self.mode)
            self.is_open = True
        else:
            if check and self.fid.mode != check:
                raise RuntimeError('File mode not correct')

    def read(self, gpi):
        """
        Read time series for specific grid point.

        Parameters
        ----------
        gpi : int
            Grid point index.
        """
        self._open()

        if self.data is None:
            self.data = pd.read_csv(self.fid)

        pos = np.where(self.data['gpi'] == gpi)[0]
        return self.data.iloc[pos]

    def read_ts(self, *args, **kwargs):
        """
        Read time series for specific grid point.
        """
        return self.read(*args, **kwargs)

    def write(self, data, index_label='date'):
        """
        Write time series.
        """
        self._open()
        data.to_csv(self.fid, index_label=index_label)

    def write_ts(self, *args, **kwargs):
        """
        Write time series.
        """
        self.write(*args, **kwargs)

    def flush(self):
        """
        Flush to disk.
        """
        self.fid.flush()

    def close(self):
        """
        Close file.
        """
        self.fid.close()

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Exit the runtime context related to this object. The file will be
        closed. The parameters describe the exception that caused the
        context to be exited.
        """
        self.close()

    def __enter__(self):
        """
        Context manager initialization. Open file.

        Returns
        -------
        self : GenericIOStatic object
            self
        """
        return self


class ImageText(ImageBase):

    def __init__(self, filename, mode='r', **kwargs):
        """
        Initialize time series csv read/write object.

        Parameters
        ----------
        filename : str
            CSV filename.
        mode : str, optional
            File opening mode. Default: 'r'
        """
        self.is_open = False
        self.fid = None
        self.data = None
        super(ImageText, self).__init__(filename, mode, **kwargs)

    def _open(self, check=None):
        """"
        Open csv file.

        Parameters
        ----------
        check : str, optional
            Check if file is open. Default: None
        """
        if not self.is_open:
            self.fid = open(self.filename, self.mode)
            self.is_open = True
        else:
            if check and self.fid.mode != check:
                raise RuntimeError('File mode not correct')

    def read(self):
        """
        Read image.
        """
        self._open()

    def write(self, image):
        """
        Write image.
        """
        pass

    def flush(self):
        """
        Flush to disk.
        """
        self.fid.flush()

    def close(self):
        """
        Close file.
        """
        self.fid.close()

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Exit the runtime context related to this object. The file will be
        closed. The parameters describe the exception that caused the
        context to be exited.
        """
        self.close()

    def __enter__(self):
        """
        Context manager initialization. Open file.

        Returns
        -------
        self : GenericIOStatic object
            self
        """
        return self


class GriddedText(GriddedBase):
    pass


class StaticTextTest(unittest.TestCase):

    def setUp(self):
        self.filename = os.path.join(mkdtemp(), 'test.txt')

    # def tearDown(self):
    #     os.remove(self.filename)

    def test_io(self):
        """
        Simple read/write test.
        """
        data = np.arange(100)
        df = pd.DataFrame({'data': data + 100}, index=data)

        with StaticText(self.filename, mode='w') as ts:
            ts.write(df)

        gpi = 1
        ts = TsText(self.filename, mode='r')
        data = ts.read(gpi)
        ts.close()

        np.testing.assert_equal(data['data'].iloc[0], df['data'].iloc[1])


class TsTextTest(unittest.TestCase):

    def setUp(self):
        self.filename = os.path.join(mkdtemp(), 'test.txt')
        print(self.filename)

    # def tearDown(self):
        # os.remove(self.filename)

    def test_io(self):
        """
        Simple read/write test.
        """
        index = pd.date_range('2007-01-01', periods=100)

        data = np.arange(len(index))
        df = pd.DataFrame({'gpi': data, 'data2': data + 10,
                           'data3': data + 30}, index=index)
        df['gpi'].iloc[0:10] = 1
        df['gpi'].iloc[10:21] = 2
        df['gpi'].iloc[20:31] = 3
        df['gpi'].iloc[30:] = 4

        with TsText(self.filename, mode='w') as ts:
            ts.write(df)

        gpi = 1
        ts = TsText(self.filename, mode='r')
        data = ts.read(gpi)
        ts.close()

        np.testing.assert_equal(data['gpi'].values,
                                df['gpi'].iloc[0:10].values)

    def test_append(self):
        """
        Simple append test.
        """
        index = pd.date_range('2007-01-01', periods=100)

        data = np.arange(len(index))
        df = pd.DataFrame({'gpi': data, 'data2': data + 10,
                           'data3': data + 30}, index=index)
        df['gpi'].iloc[0:10] = 1
        df['gpi'].iloc[10:21] = 2
        df['gpi'].iloc[20:31] = 3
        df['gpi'].iloc[30:] = 4

        with TsText(self.filename, mode='a') as ts:
            ts.write(df)

        gpi = 1
        ts = TsText(self.filename, mode='r')
        data = ts.read(gpi)
        ts.close()
        import pdb
        pdb.set_trace()
        pass

        # np.testing.assert_equal(data['gpi'].values,
        #                         df['gpi'].iloc[0:10].values)


class ImageTextTest(unittest.TestCase):

    def setUp(self):
        self.filename = os.path.join(mkdtemp(), 'test.txt')

#     def tearDown(self):
#         os.remove(self.filename)


def test_sqlite():
    from sqlalchemy import create_engine

    filename = '/home/shahn/foo.db'
    os.remove(filename)
    engine = create_engine('sqlite:////home/shahn/foo.db')

    index = pd.date_range('2007-01-01', periods=100)
    data = np.arange(len(index))
    df = pd.DataFrame({'gpi': data, 'data2': data + 10,
                       'data3': data + 30}, index=index)
    df['gpi'].iloc[0:10] = 1
    df['gpi'].iloc[10:21] = 2
    df['gpi'].iloc[20:31] = 3
    df['gpi'].iloc[30:] = 4

    tbl = 'data'
    df.to_sql(tbl, engine)
    df_in = pd.read_sql_table(tbl, engine, index_col='index')

    gpi = 2
    query = pd.read_sql_query(
        'SELECT * FROM data WHERE gpi = {:}'.format(gpi), engine)
    print(query)


def test_sqlite_test_ds():

    from sqlalchemy import create_engine

    filename = '/home/shahn/foo.db'
    os.remove(filename)
    engine = create_engine('sqlite:////home/shahn/foo.db')


if __name__ == "__main__":
    # unittest.main()
    test_sqlite_test_ds()
