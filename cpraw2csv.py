#================================================================================
#
# Reading copy-paste results from wiki page to create a clean csv file
# the file was copied from:
# http://en.wikipedia.org/w/index.php?title=List_of_H_postal_codes_of_Canada&action=edit
#
#================================================================================

def createcsv(rawfilename, csvfname = 'CP.csv'):
    """
    Creates a csv file from a copy-paste of wikipedia (edit)
    """
    fraw = open(rawfilename)
    fcsv = open(csvfname, 'w')
    fcsv.write("CP:arrondissement\n")
    for iline in fraw.readlines():
        if len(iline)<15:
            continue
        #if iline[:4] != '\'\'\'H':
        if iline[:3] != '\'\'\'':
            continue
        iline = iline.strip('\'')
        icp = iline[:3]
        iarr = None
        if iline.find("Not assigned") < 1:
            #print iline
            iarr = iline.split('[[')[1].split(']]')[0]
        fcsv.write("{}:{}\n".format(icp, iarr))
    print '\n\nDone producing csv file: {}\n'.format(csvfname)


if __name__=='__main__':
    createcsv('codepostaux.txt')
