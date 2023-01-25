import codecs
import csv




def modifyUMN():
    file_output = open("wvlib/word-similarities/CUI/UMNSRS/UMNSRS_similarity_CUI.txt", "w")
    chars = "\""

    with open("wvlib/word-similarities/CUI/UMNSRS/UMNSRS_similarity.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            cui1 = row["CUI1"]
            cui2 = row["CUI2"]
            mean = row["Mean"]

            tbp = cui1.translate(str.maketrans('', '', chars)) + " " + cui2.translate(
                str.maketrans('', '', chars)) + " " + mean + "\n"
            file_output.write(tbp)

    file_output.close()

def modifyMayo():
    file_output = open("wvlib/word-similarities/CUI/mayo/mayoSRS_CUI.txt", "w")
    chars = "\""

    with open("wvlib/word-similarities/CUI/mayo/mayoSRS human judgement.txt", "r") as file:

        lines = file.readlines()

        for line in lines:

            splitted = line.split("<>")


            tbp = splitted[1] + " " + splitted[2].translate(str.maketrans('', '', '\n')) + " " + splitted[0] + "\n"
            file_output.write(tbp)

    file_output.close()

def modifyMayoTorino():
    file_output = open("wvlib/word-similarities/srs uniTO/MayoSRStorino.txt", "w")
    chars = "\""

    with open("wvlib/word-similarities/srs uniTO/MayoSRS.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            term1 = row["TERM1"]
            term2 = row["TERM2"]
            mean = row["Mean"]

            tbp = term1.translate(str.maketrans('', '', chars)) + "\t" + term2.translate(
                str.maketrans('', '', chars)) + "\t" + mean + "\n"
            file_output.write(tbp)

    file_output.close()


def modifyUMNTorino():
    file_output = open("wvlib/word-similarities/srs uniTO/UMNSRStorino.txt", "w")
    chars = "\""

    with open("wvlib/word-similarities/srs uniTO/UMNSRS_similarity_translated.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            term1 = row["TERM1"]
            term2 = row["TERM2"]
            mean = row["Mean"]

            tbp = term1.translate(str.maketrans('', '', chars)) + "\t" + term2.translate(
                str.maketrans('', '', chars)) + "\t" + mean + "\n"
            file_output.write(tbp)

    file_output.close()

modifyMayoTorino()
