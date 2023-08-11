# Sara Muller, Samantha L Hider, Karim Raza, Rebecca J Stack, Richard A Hayward, Christian D Mallen, 2023.

import sys, csv, re

codes = [{"code":"B600000","system":"readv2"},{"code":"B601000","system":"readv2"},{"code":"B60y.00","system":"readv2"},{"code":"B614000","system":"readv2"},{"code":"B615000","system":"readv2"},{"code":"B61z000","system":"readv2"},{"code":"B620000","system":"readv2"},{"code":"B621000","system":"readv2"},{"code":"B623000","system":"readv2"},{"code":"B625000","system":"readv2"},{"code":"B627W00","system":"readv2"},{"code":"B627X00","system":"readv2"},{"code":"B62x.00","system":"readv2"},{"code":"B62y000","system":"readv2"},{"code":"B67..00","system":"readv2"},{"code":"B67y.00","system":"readv2"},{"code":"B67yz00","system":"readv2"},{"code":"B67z.00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('leukaemia-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["leukaemia-specified---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["leukaemia-specified---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["leukaemia-specified---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
