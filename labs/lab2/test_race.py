import unittest
from Race import Race
from Runner import Runner

class Test_Race(unittest.TestCase):

    def setUp(self):
        self.race = Race()


    def test_add_runner(self):
        self.race.add_runner(Runner('joe', 'joe@mail.com', 22))
        self.race.add_runner(Runner('Sagnik', 'sag@mail.com', 19))
        self.race.add_runner(Runner('Riju', 'rij@mail.com', 12))

        c = {1: ['sag@mail.com', 'rij@mail.com'], 2: ['joe@mail.com']}
        g = [Runner('joe', 'joe@mail.com', 22),Runner('Sagnik', 'sag@mail.com', 19),Runner('Riju', 'rij@mail.com', 12)]



        test = []
        for r in g:
            test.append(r.get_email())
        mails = []
        for r in self.race.get_runners():
            mails.append(r.get_email())
        self.assertEqual(mails,test)

        self.assertEqual(c,self.race.display_categories())





    if __name__ == '__main__':
        unittest.main()
