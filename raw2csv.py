#================================================================================
#
# Reading copy-paste results from pawn shop search and create a csv file
#
#================================================================================


def createPawnshopcsv(rawfilename):
    '''
    Reads rawfilename and create a clean csv file
    WARNING: some are missing because the adresses are incomplete...
    '''
    csvfname = 'pawnmtl.csv'
    fcsv = open(csvfname, 'w')
    fcsv.write('streetnum,streetname,city,province,postalcode\n' )
    fraw = open(rawfilename)
    for iline in fraw.readlines():
        isplit = iline.split(',')
        if len(isplit)!=4:
            continue
        #print iline
        istrnum, istrname, icity, irest = isplit
        irestsplit = irest.split()
        iprov = irestsplit[0]
        ipostal = irestsplit[1] + irestsplit[2]
        fcsv.write('{},{},{},{},{}\n'.format(istrnum, istrname, icity, iprov, ipostal) )
        #fcsv.write(iline)
    print '\n\n Done creating csv file {}\n'.format(csvfname)
      
def createBankcsv(rawfilename):
    '''
    Reads rawfilename and create a clean csv file
    WARNING: some are missing because the adresses are incomplete...
    '''
    csvfname = 'banksmtl.csv'
    fcsv = open(csvfname, 'w')
    fcsv.write('streetnum,streetname,city,province,postalcode\n' )
    fraw = open(rawfilename)
    for iline in fraw.readlines():
        isplit = iline.split(',')
        if len(isplit)!=4:
            continue
        #print iline
        istrnum, istrname, icity, irest = isplit
        irestsplit = irest.split()
        iprov = irestsplit[0]
        ipostal = irestsplit[1] + irestsplit[2]
        fcsv.write('{},{},{},{},{}\n'.format(istrnum, istrname, icity, iprov, ipostal) )
        #fcsv.write(iline)
    print '\n\n Done creating csv file {}\n'.format(csvfname)


    
if __name__=='__main__':
    #createPawnshopcsv('pawnmtl.txt')
    createBankcsv('banksraw.txt')
