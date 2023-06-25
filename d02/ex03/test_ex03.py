import pytest
import os
from csvreader import CsvReader

dir_path = os.path.dirname(os.path.realpath(__file__))

test_cases = [
    (os.path.join(dir_path, 'csv_files/good.csv'), True, ',', 0, 0, ['name', 'age'], [['Alice', '20'], ['Bob', '25'], ['Charlie', '30']]),
    (os.path.join(dir_path, 'csv_files/bad.csv'), True, ',', 0, 0, None, None),
    (os.path.join(dir_path, 'csv_files/good_no_header.csv'), False, ',', 0, 0, None, [['Alice', '20'], ['Bob', '25'], ['Charlie', '30']]),
    (os.path.join(dir_path, 'csv_files/bad_no_header.csv'), False, ',', 0, 0, None, None),
    (os.path.join(dir_path, 'csv_files/good_skip_top.csv'), True, ',', 2, 0, ['name', 'age'], [['Alice', '20'], ['Bob', '25'], ['Charlie', '30']]),
    (os.path.join(dir_path, 'csv_files/bad_skip_top.csv'), True, ',', 2, 0, None, None),
    (os.path.join(dir_path, 'csv_files/good_skip_bottom.csv'), True, ',', 0, 2, ['name', 'age'], [['Alice', '20'], ['Bob', '25'], ['Charlie', '30']]),
    (os.path.join(dir_path, 'csv_files/bad_skip_bottom.csv'), True, ',', 0, 2, None, None),
    (os.path.join(dir_path, 'csv_files/good_different_sep.csv'), True, ';', 0, 0, ['name', 'age'], [['Alice', '20'], ['Bob', '25'], ['Charlie', '30']]),
    (os.path.join(dir_path, 'csv_files/bad_different_sep.csv'), True, ';', 0, 0, None, None),
]

@pytest.mark.parametrize("filename,header,sep,skip_top,skip_bottom,expected_header,expected_data", test_cases)
def test_csvreader(filename, header, sep, skip_top, skip_bottom, expected_header, expected_data):
    with CsvReader(filename, sep=sep, header=header, skip_top=skip_top, skip_bottom=skip_bottom) as file:
        if expected_header is None and expected_data is None:
            assert file is None
        else:
            assert file.getheader() == expected_header
            assert file.getdata() == expected_data
