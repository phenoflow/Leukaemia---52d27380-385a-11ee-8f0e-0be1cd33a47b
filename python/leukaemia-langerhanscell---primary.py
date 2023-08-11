# Sara Muller, Samantha L Hider, Karim Raza, Rebecca J Stack, Richard A Hayward, Christian D Mallen, 2023.

import sys, csv, re

codes = [{"code":"B624.12","system":"readv2"},{"code":"B626.00","system":"readv2"},{"code":"B626000","system":"readv2"},{"code":"B626z00","system":"readv2"},{"code":"B627300","system":"readv2"},{"code":"B627500","system":"readv2"},{"code":"B627A00","system":"readv2"},{"code":"B629.00","system":"readv2"},{"code":"B62A.00","system":"readv2"},{"code":"B62C.00","system":"readv2"},{"code":"B62F000","system":"readv2"},{"code":"B62F100","system":"readv2"},{"code":"B673.00","system":"readv2"},{"code":"B67y000","system":"readv2"},{"code":"B68..00","system":"readv2"},{"code":"B68y.00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('leukaemia-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["leukaemia-langerhanscell---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["leukaemia-langerhanscell---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["leukaemia-langerhanscell---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
