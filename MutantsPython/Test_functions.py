import pytest
from functions import *


@pytest.mark.parametrize("adn_list, res", [
    (['ATGCGA',
      'CAGTGC',
      'TCATGT',
      'AGCAGG',
      'CCCCTA',
      'TCACCG'], 2),

    (['ATGCGA',
      'TGGTGC',
      'TCAGGT',
      'AGCAAG',
      'CCCCTG',
      'TCACCG'], 1),

    (['ATTCGA',
      'TGTGGC',
      'ATATAT',
      'AAAATG',
      'CCATTA',
      'TATATG'], 2),

    (['ATTCGA',
      'CGCTAC',
      'ACAAAG',
      'AGTTGT',
      'CCAGTA',
      'TATATG'], 0)

])
def test_is_diagonal(adn_list, res):
    assert is_diagonal(adn_list) == res


@pytest.mark.parametrize("adn_list, res", [
    (['ATGCCA',
      'CAGCAC',
      'TTCAGT',
      'ACAAGG',
      'ACCCTA',
      'TCACTG'], 2),

    (['ATGCAA',
      'TGGTGC',
      'TCTTGT',
      'ATCAGG',
      'TCCTTA',
      'TCACCG'], 1),

    (['ATTCAA',
      'CGCAAC',
      'ACAAAG',
      'AGTTGT',
      'CCAGTA',
      'TATATG'], 0)

])
def test_is_reverse_diagonal(adn_list, res):
    assert is_reverse_diagonal(adn_list) == res


@pytest.mark.parametrize("adn_list, res", [
  (['TTAAAA',
    'CGCTAC',
    'ACAAAG',
    'AGTTGT',
    'CCAGTA',
    'ATTTTG'], 2),

  (['ATTCGA',
    'CCCCGG',
    'ACAAAA',
    'AGTTGT',
    'CCCCTA',
    'TATATG'], 3),

  (['ATTCGA',
    'CGCTAC',
    'GAAAAG',
    'AGTTGT',
    'CCAGTA',
    'TATATG'], 1),

  (['ATTCGA',
    'CGCTAC',
    'ACAAAG',
    'AGTTTT',
    'CCCCTA',
    'TATATG'], 2),

  (['ATTCGA',
    'CGCTAC',
    'ACAAAG',
    'AGTTGT',
    'GACCCC',
    'TATATG'], 1),

  (['ATTCGA',
    'CGCTAC',
    'ACAAAG',
    'AGTTGT',
    'GACCTC',
    'CCCCAC'], 1),

  (['ATTCGA',
    'CGCTAC',
    'ACAAAG',
    'AGTTGT',
    'CACCTC',
    'TATATG'], 0),

  (['ATTCGA',
    'CGCCAC',
    'ACAAAG',
    'AGTTGT',
    'CACCTC',
    'TATATG'], 0),

  (['ATTCGA',
    'CGCTAC',
    'ACAAAG',
    'ATTTGT',
    'CACCTC',
    'TATATG'], 0)

])
def test_is_horizontal(adn_list, res):
    assert is_horizontal(adn_list) == res


@pytest.mark.parametrize("adn_list, res",[
  (['TTATAA',
    'TGCTAC',
    'TGAAAG',
    'TGTTAT',
    'TGAGAA',
    'TATAAG'], 3),

  (['ATTCGA',
    'GCACGG',
    'GCAAAG',
    'GGTTGT',
    'GCAGTA',
    'TATATG'], 1),

  (['ATTCGA',
    'CGCTAC',
    'CACAAG',
    'CGTTGT',
    'CCAGTA',
    'CATATG'], 1),

  (['ATTCGA',
    'CTCTAC',
    'ATAAAG',
    'ATACTT',
    'CCAGTA',
    'TAAATG'], 2),

  (['ATACGA',
    'CGCTAC',
    'ACCAAG',
    'AGCTGT',
    'GACCCC',
    'TATATG'], 1),

  (['ATTCGA',
    'CGCTAC',
    'ACATAG',
    'AGTTGT',
    'GACTTC',
    'CCCCAC'], 1),

  (['ATTCGA',
    'CGCTAC',
    'ACATAG',
    'AGTTAT',
    'GACTAC',
    'CCCCGC'], 2),

  (['AGTCTC',
    'AGTCTC',
    'AGTCTC',
    'AGTCTC',
    'AGTCTC',
    'AGTCTC'], 6),

  (['ATTCGA',
    'CTCTAC',
    'ATAAAG',
    'AGTTGT',
    'CACCTC',
    'TATATG'], 0),

  (['ATTCGA',
    'CGCGAC',
    'ACAGAG',
    'AGTGGT',
    'CACCTC',
    'TATATG'], 0),

  (['ATTCGA',
    'CGCTAC',
    'ACAAAG',
    'ATTTAT',
    'CACCTC',
    'TATATG'], 0)

])
def test_is_vertical(adn_list, res):
    assert is_vertical(adn_list) == res


@pytest.mark.parametrize("string, res",[
  ('AGCTGA', True),
  ('CCCGTA', True),
  ('CCATGS', False),
  ('ATZGXC', False)
])
def test_contains_adn(string, res):
    assert contains_adn(string) == res


@pytest.mark.parametrize("adn_list, res", [
    (['ATGCGA',
      'CAGTGC',
      'TTATGT',
      'AGCAGG',
      'CCACTA',
      'TCACTG'], True),

    (['ATGCCA',
      'CAGCGC',
      'TTCTGT',
      'ACCAGG',
      'ACCCCA',
      'TCACTG'], True),

    (['ATTCGA',
      'CCCCGA',
      'ACAAAG',
      'AGTAGT',
      'CCAGTA',
      'TTTATG'], True),

    (['TTATAA',
      'TGCTAC',
      'TCAAAG',
      'TGTTGT',
      'CCAGTA',
      'TAGATG'], True),

    (['ATTCGA',
      'CGCTAC',
      'AAAAGG',
      'AGTTGT',
      'CCAGTA',
      'TATATG'], False),

    (['ATTCAA',
      'CGCAAC',
      'ACAAAG',
      'AATTGT',
      'CCAGTA',
      'TATTTG'], False),

    (['ATTCGA',
      'CGCTAC',
      'ACAAAG',
      'ATTTAT',
      'CACCAC',
      'TATATG'], False),

    (['TTTCGA',
      'CTCTAC',
      'ACTAAG',
      'ATTTAT',
      'CACCTC',
      'TATATG'], False)

])
def test_is_mutant(adn_list, res):
    assert is_mutant(adn_list) == res
