# Tim Doran, Evangelos Kontopantelis, Jose M Valderas, Stephen Campbell, Martin Roland, Chris Salisbury, David Reeves, 2023.

import sys, csv, re

codes = [{"code":"13AB.00","system":"readv2"},{"code":"13AC.00","system":"readv2"},{"code":"13B1.00","system":"readv2"},{"code":"2G5B.00","system":"readv2"},{"code":"2G5K.00","system":"readv2"},{"code":"66A3.00","system":"readv2"},{"code":"66A8.00","system":"readv2"},{"code":"66AG.00","system":"readv2"},{"code":"66AJ100","system":"readv2"},{"code":"8A13.00","system":"readv2"},{"code":"8H2J.00","system":"readv2"},{"code":"9OLA.11","system":"readv2"},{"code":"F440700","system":"readv2"},{"code":"K01x100","system":"readv2"},{"code":"Kyu0300","system":"readv2"},{"code":"M037200","system":"readv2"},{"code":"N030011","system":"readv2"},{"code":"250 A","system":"oxmis"},{"code":"250 AB","system":"oxmis"},{"code":"250 AT","system":"oxmis"},{"code":"250 C","system":"oxmis"},{"code":"250 CT","system":"oxmis"},{"code":"250 DC","system":"oxmis"},{"code":"250 DR","system":"oxmis"},{"code":"250 E","system":"oxmis"},{"code":"250 ED","system":"oxmis"},{"code":"250 F","system":"oxmis"},{"code":"250 G","system":"oxmis"},{"code":"250 GA","system":"oxmis"},{"code":"250 H","system":"oxmis"},{"code":"250 HC","system":"oxmis"},{"code":"250 HP","system":"oxmis"},{"code":"250 JA","system":"oxmis"},{"code":"250 JE","system":"oxmis"},{"code":"250 JK","system":"oxmis"},{"code":"250 JL","system":"oxmis"},{"code":"250 K","system":"oxmis"},{"code":"250 LG","system":"oxmis"},{"code":"250 M","system":"oxmis"},{"code":"250 N","system":"oxmis"},{"code":"250 NH","system":"oxmis"},{"code":"250 NT","system":"oxmis"},{"code":"250 PG","system":"oxmis"},{"code":"250 PR","system":"oxmis"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('diabetes-mellitus-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["diabetes-mellitus---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["diabetes-mellitus---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["diabetes-mellitus---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
