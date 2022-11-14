import requests
from pandas import json_normalize
import extract_matches


def normalizing(match_id):
        read_events = requests.get("https://raw.githubusercontent.com/statsbomb/open-data/master/data/events/"+str(match_id)+'.json')       
        events = read_events.json() 
        events_df = json_normalize(events, sep = '_')
        return events_df


class ExtractEvents:
    def __init__(self):
        pass
    def matches_ids(self):
        self.extract_matches_df = extract_matches.ExtractMatches(43,3).matches_list()

        self.all_matches_ids = []
        for id in self.extract_matches_df['match_id']:
            self.all_matches_ids.append(id)

        return sorted(self.all_matches_ids)

    def event_7525(self):
        list_of_ids = self.matches_ids()

        if 7525 in list_of_ids:
            match_7525_raw = normalizing(7525)
            match_7525 = match_7525_raw.drop(columns = {'tactics_lineup','shot_freeze_frame'})
            return match_7525
        else:
            print('Match not found')

    def event_7529(self):
        list_of_ids = self.matches_ids()

        if 7529 in list_of_ids:
            match_7529_raw = normalizing(7529)
            match_7529 = match_7529_raw.drop(columns = {'tactics_lineup','shot_freeze_frame'})
            return match_7529
        else:
            print('Match not found')

    def event_7530(self):
        list_of_ids = self.matches_ids()

        if 7530 in list_of_ids:
            match_7530_raw = normalizing(7530)
            match_7530 = match_7530_raw.drop(columns = {'tactics_lineup','shot_freeze_frame'})
            return match_7530
        else:
            print('Match not found')

    def event_7531(self):
        list_of_ids = self.matches_ids()

        if 7531 in list_of_ids:
            match_7531_raw = normalizing(7531)
            match_7531 = match_7531_raw.drop(columns = {'tactics_lineup','shot_freeze_frame'})
            return match_7531
        else:
            print('Match not found')

    def event_7532(self):
        list_of_ids = self.matches_ids()

        if 7532 in list_of_ids:
            match_7532_raw = normalizing(7532)
            match_7532 = match_7532_raw.drop(columns = {'tactics_lineup','shot_freeze_frame'})
            return match_7532
        else:
            print('Match not found')

    def event_7533(self):

        list_of_ids = self.matches_ids()

        if 7533 in list_of_ids:
            match_7533_raw = normalizing(7533)
            match_7533 = match_7533_raw.drop(columns = {'tactics_lineup','shot_freeze_frame'})
            return match_7533
        else:
            print('Match not found')

    def event_7534(self):

        list_of_ids = self.matches_ids()

        if 7534 in list_of_ids:
            match_7534_raw = normalizing(7534)
            match_7534 = match_7534_raw.drop(columns = {'tactics_lineup','shot_freeze_frame'})
            return match_7534
        else:
            print('Match not found')

    def event_7535(self):
        list_of_ids = self.matches_ids()

        if 7535 in list_of_ids:
            match_7535_raw = normalizing(7535)
            match_7535 = match_7535_raw.drop(columns = {'tactics_lineup','shot_freeze_frame'})
            return match_7535
        else:
            print('Match not found')

    def event_7536(self):
        list_of_ids = self.matches_ids()

        if 7536 in list_of_ids:
            match_7536_raw = normalizing(7536)
            match_7536 = match_7536_raw.drop(columns = {'tactics_lineup','shot_freeze_frame'})
            return match_7536
        else:
            print('Match not found')

    def event_7537(self):
        list_of_ids = self.matches_ids()

        if 7537 in list_of_ids:
            match_7537_raw = normalizing(7537)
            match_7537 = match_7537_raw.drop(columns = {'tactics_lineup','shot_freeze_frame'})
            return match_7537
        else:
            print('Match not found')

    def event_7538(self):
        list_of_ids = self.matches_ids()

        if 7538 in list_of_ids:
            match_7538_raw = normalizing(7538)
            match_7538 = match_7538_raw.drop(columns = {'tactics_lineup','shot_freeze_frame'})
            return match_7538
        else:
            print('Match not found')

    def event_7539(self):
        list_of_ids = self.matches_ids()

        if 7539 in list_of_ids:
            match_7539_raw = normalizing(7539)
            match_7539 = match_7539_raw.drop(columns = {'tactics_lineup','shot_freeze_frame'})
            return match_7539
        else:
            print('Match not found')

    def event_7540(self):
        list_of_ids = self.matches_ids()

        if 7540 in list_of_ids:
            match_7540_raw = normalizing(7540)
            match_7540 = match_7540_raw.drop(columns = {'tactics_lineup','shot_freeze_frame'})
            return match_7540
        else:
            print('Match not found')

    def event_7541(self):
        list_of_ids = self.matches_ids()

        if 7541 in list_of_ids:
            match_7541_raw = normalizing(7541)
            match_7541 = match_7541_raw.drop(columns = {'tactics_lineup','shot_freeze_frame'})
            return match_7541
        else:
            print('Match not found')

    def event_7542(self):
        list_of_ids = self.matches_ids()

        if 7542 in list_of_ids:
            match_7542_raw = normalizing(7542)
            match_7542 = match_7542_raw.drop(columns = {'tactics_lineup','shot_freeze_frame'})
            return match_7542
        else:
            print('Match not found')

    def event_7543(self):
        list_of_ids = self.matches_ids()

        if 7543 in list_of_ids:
            match_7543_raw = normalizing(7543)
            match_7543 = match_7543_raw.drop(columns = {'tactics_lineup','shot_freeze_frame'})
            return match_7543
        else:
            print('Match not found')

    def event_7544(self):
        list_of_ids = self.matches_ids()

        if 7544 in list_of_ids:
            match_7544_raw = normalizing(7544)
            match_7544 = match_7544_raw.drop(columns = {'tactics_lineup','shot_freeze_frame'})
            return match_7544
        else:
            print('Match not found')

    def event_7545(self):
        list_of_ids = self.matches_ids()

        if 7545 in list_of_ids:
            match_7545_raw = normalizing(7545)
            match_7545 = match_7545_raw.drop(columns = {'tactics_lineup','shot_freeze_frame'})
            return match_7545
        else:
            print('Match not found')

    def event_7546(self):
        list_of_ids = self.matches_ids()

        if 7546 in list_of_ids:
            match_7546_raw = normalizing(7546)
            match_7546 = match_7546_raw.drop(columns = {'tactics_lineup','shot_freeze_frame'})
            return match_7546
        else:
            print('Match not found')

    def event_7547(self):
        list_of_ids = self.matches_ids()

        if 7547 in list_of_ids:
            match_7547_raw = normalizing(7547)
            match_7547 = match_7547_raw.drop(columns = {'tactics_lineup','shot_freeze_frame'})
            return match_7547
        else:
            print('Match not found')

    def event_7548(self):
        list_of_ids = self.matches_ids()

        if 7548 in list_of_ids:
            match_7548_raw = normalizing(7548)
            match_7548 = match_7548_raw.drop(columns = {'tactics_lineup','shot_freeze_frame'})
            return match_7548
        else:
            print('Match not found')

    def event_7549(self):
        list_of_ids = self.matches_ids()

        if 7549 in list_of_ids:
            match_7549_raw = normalizing(7549)
            match_7549 = match_7549_raw.drop(columns = {'tactics_lineup','shot_freeze_frame'})
            return match_7549
        else:
            print('Match not found')

    def event_7550(self):
        list_of_ids = self.matches_ids()

        if 7550 in list_of_ids:
            match_7550_raw = normalizing(7550)
            match_7550 = match_7550_raw.drop(columns = {'tactics_lineup','shot_freeze_frame'})
            return match_7550
        else:
            print('Match not found')

    def event_7551(self):
        list_of_ids = self.matches_ids()

        if 7551 in list_of_ids:
            match_7551_raw = normalizing(7551)
            match_7551 = match_7551_raw.drop(columns = {'tactics_lineup','shot_freeze_frame'})
            return match_7551
        else:
            print('Match not found')

    def event_7552(self):
        list_of_ids = self.matches_ids()

        if 7552 in list_of_ids:
            match_7552_raw = normalizing(7552)
            match_7552 = match_7552_raw.drop(columns = {'tactics_lineup','shot_freeze_frame'})
            return match_7552
        else:
            print('Match not found')

    def event_7553(self):
        list_of_ids = self.matches_ids()

        if 7553 in list_of_ids:
            match_7553_raw = normalizing(7553)
            match_7553 = match_7553_raw.drop(columns = {'tactics_lineup','shot_freeze_frame'})
            return match_7553
        else:
            print('Match not found')

    def event_7554(self):
        list_of_ids = self.matches_ids()

        if 7554 in list_of_ids:
            match_7554_raw = normalizing(7554)
            match_7554 = match_7554_raw.drop(columns = {'tactics_lineup','shot_freeze_frame'})
            return match_7554
        else:
            print('Match not found')

    def event_7555(self):
        list_of_ids = self.matches_ids()

        if 7555 in list_of_ids:
            match_7555_raw = normalizing(7555)
            match_7555 = match_7555_raw.drop(columns = {'tactics_lineup','shot_freeze_frame'})
            return match_7555
        else:
            print('Match not found')

    def event_7556(self):
        list_of_ids = self.matches_ids()

        if 7556 in list_of_ids:
            match_7556_raw = normalizing(7556)
            match_7556 = match_7556_raw.drop(columns = {'tactics_lineup','shot_freeze_frame'})
            return match_7556
        else:
            print('Match not found')

    def event_7557(self):
        list_of_ids = self.matches_ids()

        if 7557 in list_of_ids:
            match_7557_raw = normalizing(7557)
            match_7557 = match_7557_raw.drop(columns = {'tactics_lineup','shot_freeze_frame'})
            return match_7557
        else:
            print('Match not found')

    def event_7558(self):
        list_of_ids = self.matches_ids()

        if 7558 in list_of_ids:
            match_7558_raw = normalizing(7558)
            match_7558 = match_7558_raw.drop(columns = {'tactics_lineup','shot_freeze_frame'})
            return match_7558
        else:
            print('Match not found')

    def event_7559(self):
        list_of_ids = self.matches_ids()

        if 7559 in list_of_ids:
            match_7559_raw = normalizing(7559)
            match_7559 = match_7559_raw.drop(columns = {'tactics_lineup','shot_freeze_frame'})
            return match_7559
        else:
            print('Match not found')

    def event_7560(self):
        list_of_ids = self.matches_ids()

        if 7560 in list_of_ids:
            match_7560_raw = normalizing(7560)
            match_7560 = match_7560_raw.drop(columns = {'tactics_lineup','shot_freeze_frame'})
            return match_7560
        else:
            print('Match not found')

    def event_7561(self):
        list_of_ids = self.matches_ids()

        if 7561 in list_of_ids:
            match_7561_raw = normalizing(7561)
            match_7561 = match_7561_raw.drop(columns = {'tactics_lineup','shot_freeze_frame'})
            return match_7561
        else:
            print('Match not found')

    def event_7562(self):
        list_of_ids = self.matches_ids()

        if 7562 in list_of_ids:
            match_7562_raw = normalizing(7562)
            match_7562 = match_7562_raw.drop(columns = {'tactics_lineup','shot_freeze_frame'})
            return match_7562
        else:
            print('Match not found')

    def event_7563(self):
        list_of_ids = self.matches_ids()

        if 7563 in list_of_ids:
            match_7563_raw = normalizing(7563)
            match_7563 = match_7563_raw.drop(columns = {'tactics_lineup','shot_freeze_frame'})
            return match_7563
        else:
            print('Match not found')

    def event_7564(self):
        list_of_ids = self.matches_ids()

        if 7564 in list_of_ids:
            match_7564_raw = normalizing(7564)
            match_7564 = match_7564_raw.drop(columns = {'tactics_lineup','shot_freeze_frame'})
            return match_7564
        else:
            print('Match not found')

    def event_7565(self):
        list_of_ids = self.matches_ids()

        if 7565 in list_of_ids:
            match_7565_raw = normalizing(7565)
            match_7565 = match_7565_raw.drop(columns = {'tactics_lineup','shot_freeze_frame'})
            return match_7565
        else:
            print('Match not found')

    def event_7566(self):
        list_of_ids = self.matches_ids()

        if 7566 in list_of_ids:
            match_7566_raw = normalizing(7566)
            match_7566 = match_7566_raw.drop(columns = {'tactics_lineup','shot_freeze_frame'})
            return match_7566
        else:
            print('Match not found')

    def event_7567(self):
        list_of_ids = self.matches_ids()

        if 7567 in list_of_ids:
            match_7567_raw = normalizing(7567)
            match_7567 = match_7567_raw.drop(columns = {'tactics_lineup','shot_freeze_frame'})
            return match_7567
        else:
            print('Match not found')

    def event_7568(self):
        list_of_ids = self.matches_ids()

        if 7568 in list_of_ids:
            match_7568_raw = normalizing(7568)
            match_7568 = match_7568_raw.drop(columns = {'tactics_lineup','shot_freeze_frame'})
            return match_7568
        else:
            print('Match not found')

    def event_7569(self):
        list_of_ids = self.matches_ids()

        if 7569 in list_of_ids:
            match_7569_raw = normalizing(7569)
            match_7569 = match_7569_raw.drop(columns = {'tactics_lineup','shot_freeze_frame'})
            return match_7569
        else:
            print('Match not found')

    def event_7570(self):
        list_of_ids = self.matches_ids()

        if 7570 in list_of_ids:
            match_7570_raw = normalizing(7570)
            match_7570 = match_7570_raw.drop(columns = {'tactics_lineup','shot_freeze_frame'})
            return match_7570
        else:
            print('Match not found')

    def event_7571(self):
        list_of_ids = self.matches_ids()

        if 7571 in list_of_ids:
            match_7571_raw = normalizing(7571)
            match_7571 = match_7571_raw.drop(columns = {'tactics_lineup','shot_freeze_frame'})
            return match_7571
        else:
            print('Match not found')

    def event_7572(self):
        list_of_ids = self.matches_ids()

        if 7572 in list_of_ids:
            match_7572_raw = normalizing(7572)
            match_7572 = match_7572_raw.drop(columns = {'tactics_lineup','shot_freeze_frame'})
            return match_7572
        else:
            print('Match not found')

    def event_7576(self):
        list_of_ids = self.matches_ids()

        if 7576 in list_of_ids:
            match_7576_raw = normalizing(7576)
            match_7576 = match_7576_raw.drop(columns = {'tactics_lineup','shot_freeze_frame'})
            return match_7576
        else:
            print('Match not found')

    def event_7577(self):
        list_of_ids = self.matches_ids()

        if 7577 in list_of_ids:
            match_7577_raw = normalizing(7577)
            match_7577 = match_7577_raw.drop(columns = {'tactics_lineup','shot_freeze_frame'})
            return match_7577
        else:
            print('Match not found')

    def event_7578(self):
        list_of_ids = self.matches_ids()

        if 7578 in list_of_ids:
            match_7578_raw = normalizing(7578)
            match_7578 = match_7578_raw.drop(columns = {'tactics_lineup','shot_freeze_frame'})
            return match_7578
        else:
            print('Match not found')

    def event_7579(self):
        list_of_ids = self.matches_ids()

        if 7579 in list_of_ids:
            match_7579_raw = normalizing(7579)
            match_7579 = match_7579_raw.drop(columns = {'tactics_lineup','shot_freeze_frame'})
            return match_7579
        else:
            print('Match not found')

    def event_7580(self):
        list_of_ids = self.matches_ids()

        if 7580 in list_of_ids:
            match_7580_raw = normalizing(7580)
            match_7580 = match_7580_raw.drop(columns = {'tactics_lineup','shot_freeze_frame'})
            return match_7580
        else:
            print('Match not found')

    def event_7581(self):
        list_of_ids = self.matches_ids()

        if 7581 in list_of_ids:
            match_7581_raw = normalizing(7581)
            match_7581 = match_7581_raw.drop(columns = {'tactics_lineup','shot_freeze_frame'})
            return match_7581
        else:
            print('Match not found')

    def event_7582(self):
        list_of_ids = self.matches_ids()

        if 7582 in list_of_ids:
            match_7582_raw = normalizing(7582)
            match_7582 = match_7582_raw.drop(columns = {'tactics_lineup','shot_freeze_frame'})
            return match_7582
        else:
            print('Match not found')

    def event_7583(self):
        list_of_ids = self.matches_ids()

        if 7583 in list_of_ids:
            match_7583_raw = normalizing(7583)
            match_7583 = match_7583_raw.drop(columns = {'tactics_lineup','shot_freeze_frame'})
            return match_7583
        else:
            print('Match not found')

    def event_7584(self):
        list_of_ids = self.matches_ids()

        if 7584 in list_of_ids:
            match_7584_raw = normalizing(7584)
            match_7584 = match_7584_raw.drop(columns = {'tactics_lineup','shot_freeze_frame'})
            return match_7584
        else:
            print('Match not found')

    def event_7585(self):
        list_of_ids = self.matches_ids()

        if 7585 in list_of_ids:
            match_7585_raw = normalizing(7585)
            match_7585 = match_7585_raw.drop(columns = {'tactics_lineup','shot_freeze_frame'})
            return match_7585
        else:
            print('Match not found')

    def event_7586(self):
        list_of_ids = self.matches_ids()

        if 7586 in list_of_ids:
            match_7586_raw = normalizing(7586)
            match_7586 = match_7586_raw.drop(columns = {'tactics_lineup','shot_freeze_frame'})
            return match_7586
        else:
            print('Match not found')

    def event_8649(self):
        list_of_ids = self.matches_ids()

        if 8649 in list_of_ids:
            match_8649_raw = normalizing(8649)
            match_8649 = match_8649_raw.drop(columns = {'tactics_lineup','shot_freeze_frame'})
            return match_8649
        else:
            print('Match not found')

    def event_8650(self):
        list_of_ids = self.matches_ids()

        if 8650 in list_of_ids:
            match_8650_raw = normalizing(8650)
            match_8650 = match_8650_raw.drop(columns = {'tactics_lineup','shot_freeze_frame'})
            return match_8650
        else:
            print('Match not found')

    def event_8651(self):
        list_of_ids = self.matches_ids()

        if 8651 in list_of_ids:
            match_8651_raw = normalizing(8651)
            match_8651 = match_8651_raw.drop(columns = {'tactics_lineup','shot_freeze_frame'})
            return match_8651
        else:
            print('Match not found')

    def event_8652(self):
        list_of_ids = self.matches_ids()

        if 8652 in list_of_ids:
            match_8652_raw = normalizing(8652)
            match_8652 = match_8652_raw.drop(columns = {'tactics_lineup','shot_freeze_frame'})
            return match_8652
        else:
            print('Match not found')

    def event_8655(self):
        list_of_ids = self.matches_ids()

        if 8655 in list_of_ids:
            match_8655_raw = normalizing(8655)
            match_8655 = match_8655_raw.drop(columns = {'tactics_lineup','shot_freeze_frame'})
            return match_8655
        else:
            print('Match not found')

    def event_8656(self):
        list_of_ids = self.matches_ids()

        if 8656 in list_of_ids:
            match_8656_raw = normalizing(8656)
            match_8656 = match_8656_raw.drop(columns = {'tactics_lineup','shot_freeze_frame'})
            return match_8656
        else:
            print('Match not found')

    def event_8657(self):
        list_of_ids = self.matches_ids()

        if 8657 in list_of_ids:
            match_8657_raw = normalizing(8657)
            match_8657 = match_8657_raw.drop(columns = {'tactics_lineup','shot_freeze_frame'})
            return match_8657
        else:
            print('Match not found')

    def event_8658(self):
        list_of_ids = self.matches_ids()

        if 8658 in list_of_ids:
            match_8658_raw = normalizing(8658)
            match_8658 = match_8658_raw.drop(columns = {'tactics_lineup','shot_freeze_frame'})
            return match_8658
        else:
            print('Match not found')


match_7525 = ExtractEvents().event_7525()
match_7529 = ExtractEvents().event_7529()
match_7530 = ExtractEvents().event_7530()
match_7531 = ExtractEvents().event_7531()
match_7532 = ExtractEvents().event_7532()
match_7533 = ExtractEvents().event_7533()
match_7534 = ExtractEvents().event_7534()
match_7535 = ExtractEvents().event_7535()
match_7536 = ExtractEvents().event_7536()
match_7537 = ExtractEvents().event_7537()
match_7538 = ExtractEvents().event_7538()
match_7539 = ExtractEvents().event_7539()
match_7540 = ExtractEvents().event_7540()
match_7541 = ExtractEvents().event_7541()
match_7542 = ExtractEvents().event_7542()
match_7543 = ExtractEvents().event_7543()
match_7544 = ExtractEvents().event_7544()
match_7545 = ExtractEvents().event_7545()
match_7546 = ExtractEvents().event_7546()
match_7547 = ExtractEvents().event_7547()
match_7548 = ExtractEvents().event_7548()
match_7549 = ExtractEvents().event_7549()
match_7550 = ExtractEvents().event_7550()
match_7551 = ExtractEvents().event_7551()
match_7552 = ExtractEvents().event_7552()
match_7553 = ExtractEvents().event_7553()
match_7554 = ExtractEvents().event_7554()
match_7555 = ExtractEvents().event_7555()
match_7556 = ExtractEvents().event_7556()
match_7557 = ExtractEvents().event_7557()
match_7558 = ExtractEvents().event_7558()
match_7559 = ExtractEvents().event_7559()
match_7560 = ExtractEvents().event_7560()
match_7561 = ExtractEvents().event_7561()
match_7562 = ExtractEvents().event_7562()
match_7563 = ExtractEvents().event_7563()
match_7564 = ExtractEvents().event_7564()
match_7565 = ExtractEvents().event_7565()
match_7566 = ExtractEvents().event_7566()
match_7567 = ExtractEvents().event_7567()
match_7568 = ExtractEvents().event_7568()
match_7569 = ExtractEvents().event_7569()
match_7570 = ExtractEvents().event_7570()
match_7571 = ExtractEvents().event_7571()
match_7572 = ExtractEvents().event_7572()
match_7576 = ExtractEvents().event_7576()
match_7577 = ExtractEvents().event_7577()
match_7578 = ExtractEvents().event_7578()
match_7579 = ExtractEvents().event_7579()
match_7580 = ExtractEvents().event_7580()
match_7581 = ExtractEvents().event_7581()
match_7582 = ExtractEvents().event_7582()
match_7583 = ExtractEvents().event_7583()
match_7584 = ExtractEvents().event_7584()
match_7585 = ExtractEvents().event_7585()
match_7586 = ExtractEvents().event_7586()
match_8649 = ExtractEvents().event_8649()
match_8650 = ExtractEvents().event_8650()
match_8651 = ExtractEvents().event_8651()
match_8652 = ExtractEvents().event_8652()
match_8655 = ExtractEvents().event_8655()
match_8656 = ExtractEvents().event_8656()
match_8657 = ExtractEvents().event_8657()
match_8658 = ExtractEvents().event_8658()


dataframes = [match_7525, match_7529, match_7530, match_7531, match_7532, match_7533, match_7534, match_7535, match_7536, 
              match_7537, match_7538, match_7539, match_7540, match_7541, match_7542, match_7543, match_7544, match_7545, 
              match_7546, match_7547, match_7548, match_7549, match_7550, match_7551, match_7552, match_7553, match_7554, 
              match_7555, match_7556, match_7557, match_7558, match_7559, match_7560, match_7561, match_7562, match_7563, 
              match_7564, match_7565, match_7566, match_7567, match_7568, match_7569, match_7570, match_7571, match_7572, 
              match_7576, match_7577, match_7578, match_7579, match_7580, match_7581, match_7582, match_7583, match_7584, 
              match_7585, match_7586, match_8649, match_8650, match_8651, match_8652, match_8655, match_8656, match_8657, 
              match_8658]

frames = {}

for key, value in enumerate(dataframes):# index(key) and value
    frames[key] = value # assigning data frame from list to key in dictionary








