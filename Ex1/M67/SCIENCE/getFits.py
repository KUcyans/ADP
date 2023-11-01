

class GetFits:
    data = []
    header = []

    def __init__(self) -> None:
        self.buildData
        self.buildHeader

    def buildData():
        data.append(fits.getdata(
            'EFOSC.2000-12-30T07:58:50.968.fits', header=False))
        data.append(fits.getdata(
            'EFOSC.2000-12-30T07:59:36.806.fits', header=False))
        data.append(fits.getdata(
            'EFOSC.2000-12-30T08:00:22.811.fits', header=False))
        data.append(fits.getdata(
            'EFOSC.2001-01-02T04:56:43.016.fits', header=False))
        data.append(fits.getdata(
            'EFOSC.2001-01-02T05:00:00.454.fits', header=False))
        data.append(fits.getdata(
            'EFOSC.2001-01-02T05:01:30.597.fits', header=False))

    def buildHeader():
        header.append(fits.getheader(
            'EFOSC.2000-12-30T07:58:50.968.fits'))
        header.append(fits.getheader(
            'EFOSC.2000-12-30T07:59:36.806.fits'))
        header.append(fits.getheader(
            'EFOSC.2000-12-30T08:00:22.811.fits'))
        header.append(fits.getheader(
            'EFOSC.2001-01-02T04:56:43.016.fits'))
        header.append(fits.getheader(
            'EFOSC.2001-01-02T05:00:00.454.fits'))
        header.append(fits.getheader(
            'EFOSC.2001-01-02T05:01:30.597.fits'))

    def getData():
        return data

    def getHeader():
        return header

    def len(list):
        return len(list)
