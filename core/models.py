from django.db import models

class Cropcategory(models.Model):
    categoryid = models.AutoField(primary_key=True)
    categoryname = models.CharField(max_length=512, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    createddate = models.DateTimeField(blank=True, null=True)
    createdbyuserid = models.IntegerField(blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)
    modifiedbyuserid = models.IntegerField(blank=True, null=True)
    notes = models.CharField(max_length=4000, blank=True, null=True)

    def __str__ (self):
        return self.categoryname

    class Meta:
        managed = False
        db_table = 'cropcategory'


class Crops(models.Model):
    cropid = models.AutoField(primary_key=True)
    farmid = models.IntegerField(blank=True, null=True)
    # mastercropid = models.IntegerField(blank=True, null=True)
    mastercropid = models.ForeignKey('mastercrop', on_delete=models.DO_NOTHING, db_column='mastercropid'),
    imagename = models.CharField(max_length=125, blank=True, null=True)
    isfinished = models.IntegerField(blank=True, null=True)
    notes = models.CharField(max_length=1000, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    createdbyuserid = models.IntegerField(blank=True, null=True)
    createddate = models.DateTimeField(blank=True, null=True)
    modifiedbyuserid = models.IntegerField(blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)
    # croptypeid = models.IntegerField(blank=True, null=True)
    croptypeid = models.ForeignKey('croptype', on_delete=models.DO_NOTHING, db_column='croptypeid'),
    parentname = models.CharField(max_length=125, blank=True, null=True)
    croptypename = models.CharField(max_length=125, blank=True, null=True)
    varietyname = models.CharField(max_length=125, blank=True, null=True)
    totalsuccession = models.IntegerField(blank=True, null=True)
    harvestunitdefault = models.CharField(max_length=32, blank=True, null=True)
    yeildunitdefault = models.CharField(max_length=32, blank=True, null=True)
    yeildratedefault = models.FloatField(blank=True, null=True)
    currentharvestunit = models.CharField(max_length=32, blank=True, null=True)
    color = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        if self.parentname is not None:
            return str(self.parentname)
        else:
            return ""  

    class Meta:
        managed = False
        db_table = 'crops'


class Croptype(models.Model):
    croptypeid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=512, blank=True, null=True)
    imagename = models.CharField(max_length=125, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    notes = models.CharField(max_length=512, blank=True, null=True)
    createdbyuserid = models.IntegerField(blank=True, null=True)
    createddate = models.DateTimeField(blank=True, null=True)
    modifiedbyuserid = models.IntegerField(blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)

    def __str__ (self):
        return self.name
    
    class Meta:
        managed = False
        db_table = 'croptype'


class Growingmethods(models.Model):
    growingmethodid = models.AutoField(primary_key=True)
    growingmethodname = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    createddate = models.DateTimeField(blank=True, null=True)
    createdbyuserid = models.IntegerField(blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)
    modifiedbyuserid = models.IntegerField(blank=True, null=True)

    def __str__ (self):
        return self.growingmethodname

    class Meta:
        managed = False
        db_table = 'growingmethods'


class Harvestseason(models.Model):
    harvestseasonid = models.AutoField(primary_key=True)
    harvestseasonname = models.CharField(max_length=52, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    createddate = models.DateTimeField(blank=True, null=True)
    createdbyuserid = models.IntegerField(blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)
    modifiedbyuserid = models.IntegerField(blank=True, null=True)

    def __str__ (self):
        return self.harvestseasonname

    class Meta:
        managed = False
        db_table = 'harvestseason'


class Mastercrop(models.Model):
    mastercropid = models.AutoField(primary_key=True)
    varietyname = models.CharField(max_length=512, blank=True, null=True)
    longname = models.CharField(max_length=512, blank=True, null=True)
    naturalname = models.CharField(max_length=512, blank=True, null=True)
    searchtags = models.CharField(max_length=512, blank=True, null=True)
    colorname = models.CharField(max_length=125, blank=True, null=True)
    imagename = models.CharField(max_length=125, blank=True, null=True)
    notes = models.CharField(max_length=512, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    history = models.CharField(max_length=1000, blank=True, null=True)
    farmid = models.IntegerField(blank=True, null=True)
    defaultcombinationkeyid = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    createdbyuserid = models.IntegerField(blank=True, null=True)
    createddate = models.DateTimeField(blank=True, null=True)
    modifiedbyuserid = models.IntegerField(blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)
    refimageid = models.IntegerField(blank=True, null=True)
    imagesource = models.CharField(max_length=512, blank=True, null=True)
    # parentcropid = models.IntegerField(blank=True, null=True)
    parentcropid = models.ForeignKey('parentcrop', models.DO_NOTHING, db_column='parentcropid')
    # parentcroptypeid = models.IntegerField(blank=True, null=True)
    parentcroptypeid = models.ForeignKey('parentcroptype', models.DO_NOTHING, db_column='parentcroptypeid')
    generic = models.IntegerField(blank=True, null=True)
    iscroptypedefault = models.IntegerField(blank=True, null=True)
    isparentcropdefault = models.IntegerField(blank=True, null=True)
    backup = models.CharField(max_length=1000, blank=True, null=True)
    varietysearchtags = models.CharField(max_length=512, blank=True, null=True)
    color = models.CharField(max_length=100, blank=True, null=True)

    def __str__ (self):
        return self.varietyname
    
    class Meta:
        managed = False
        db_table = 'mastercrop'


class Parentcrop(models.Model):
    parentcropid = models.AutoField(primary_key=True)
    # cropcategoryid = models.IntegerField(blank=True, null=True)
    cropcategoryid = models.ForeignKey('cropcategory', on_delete=models.DO_NOTHING, db_column='cropcategoryid'),
    name = models.CharField(max_length=125, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    imagename = models.CharField(max_length=125, blank=True, null=True)
    farmid = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    createddate = models.DateTimeField(blank=True, null=True)
    createdbyuserid = models.IntegerField(blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)
    modifiedbyuserid = models.IntegerField(blank=True, null=True)
    refimagid = models.IntegerField(blank=True, null=True)
    imagesource = models.CharField(max_length=512, blank=True, null=True)
    harvestunit = models.CharField(max_length=52, blank=True, null=True)
    searchtags = models.CharField(max_length=512, blank=True, null=True)
    note = models.CharField(max_length=512, blank=True, null=True)
    hasvariety = models.TextField(blank=True, null=True)  # This field type is a guess.
    mappingid = models.BigIntegerField(blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)
    totalplanting = models.IntegerField(blank=True, null=True)
    hasplantsale = models.TextField(blank=True, null=True)  # This field type is a guess.
    defaultseedingmethod = models.CharField(max_length=10, blank=True, null=True)

    def __str__ (self):
        return self.name

    class Meta:
        managed = False
        db_table = 'parentcrop'


class PollsQuestion(models.Model):
    id = models.AutoField(primary_key=True)
    questiontext = models.CharField(max_length=200)
    createddate = models.DateTimeField()
    objecttype = models.CharField(max_length=200)

    def __str__ (self):
        return self.questiontext

    class Meta:
        managed = False
        db_table = 'polls_question'


class Subtasktype(models.Model):
    subtypeid = models.AutoField(primary_key=True)
    tasktypeid = models.IntegerField(blank=True, null=True)
    typename = models.CharField(max_length=512, blank=True, null=True)
    groupby = models.CharField(max_length=5, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    createddate = models.DateTimeField(blank=True, null=True)
    createdbyuserid = models.IntegerField(blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)
    modifiedbyuserid = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)
    sign = models.CharField(max_length=2, blank=True, null=True)
    textcolor = models.CharField(max_length=10, blank=True, null=True)

    def __str__ (self):
        return self.typename

    class Meta:
        managed = False
        db_table = 'subtasktype'


class Parentcroptype(models.Model):
    id = models.AutoField(primary_key=True)
    # parentcropid = models.IntegerField(blank=True, null=True)
    parentcropid = models.ForeignKey('parentcrop', on_delete=models.DO_NOTHING, db_column='parentcropid'),
    # croptypeid = models.IntegerField(blank=True, null=True)
    croptypeid = models.ForeignKey('croptype', on_delete=models.DO_NOTHING, db_column='croptypeid'),
    status = models.CharField(max_length=20, blank=True, null=True)
    createddate = models.DateTimeField(blank=True, null=True)
    createdbyuserid = models.IntegerField(blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)
    modifiedbyuserid = models.IntegerField(blank=True, null=True)
    parentname = models.CharField(max_length=125, blank=True, null=True)
    croptypename = models.CharField(max_length=125, blank=True, null=True)
    imagename = models.CharField(max_length=125, blank=True, null=True)

    def __str__ (self):
        return self.croptypename

    class Meta:
        managed = False
        db_table = 'parentcroptype'


class Loggingchatbot(models.Model):
    id = models.AutoField(primary_key=True)
    createddate = models.DateTimeField()
    content = models.CharField(max_length=200)

    def __str__ (self):
        return self.content

    class Meta:
        managed = False
        db_table = 'loggingchatbot'


class Combinationdata(models.Model):
    combinationkeyid = models.CharField(max_length=50, blank=True, null=True)
    # parentcropid = models.IntegerField(blank=True, null=True)
    parentcropid = models.ForeignKey(Parentcrop, on_delete=models.DO_NOTHING, db_column='parentcropid')
    # parentcroptypeid = models.IntegerField(blank=True, null=True)
    parentcroptypeid = models.ForeignKey(Parentcroptype, on_delete=models.DO_NOTHING, db_column='parentcroptypeid')
    # mastercropid = models.IntegerField(blank=True, null=True)
    mastercropid = models.ForeignKey(Mastercrop, on_delete=models.DO_NOTHING, db_column='mastercropid')
    # growingmethodid = models.IntegerField(blank=True, null=True)
    growingmethodid = models.ForeignKey(Growingmethods, on_delete=models.DO_NOTHING, db_column='growingmethodid')
    plantingmethodid = models.IntegerField(blank=True, null=True)
    # croptypeid = models.IntegerField(blank=True, null=True)
    croptypeid = models.ForeignKey(Croptype, on_delete=models.DO_NOTHING, db_column='croptypeid')
    transplantrowspacinglow = models.FloatField(blank=True, null=True)
    transplantrowspacinghigh = models.FloatField(blank=True, null=True)
    rowspacinglow = models.FloatField(blank=True, null=True)
    rowspacinghigh = models.FloatField(blank=True, null=True)
    thinningspacinglow = models.FloatField(blank=True, null=True)
    thinningspacinghigh = models.FloatField(blank=True, null=True)
    seedingratelow = models.FloatField(blank=True, null=True)
    seedingratehigh = models.FloatField(blank=True, null=True)
    bandsseedingrateperfoot = models.FloatField(blank=True, null=True)
    daymaturity = models.IntegerField(blank=True, null=True)
    daytomaturityll = models.IntegerField(blank=True, null=True)
    daytomaturitylh = models.IntegerField(blank=True, null=True)
    daytomaturityhl = models.IntegerField(blank=True, null=True)
    daytomaturityhh = models.IntegerField(blank=True, null=True)
    daytomaturitytext = models.CharField(max_length=256, blank=True, null=True)
    yieldrate = models.FloatField(blank=True, null=True)
    daystotransplantdatefromghl = models.IntegerField(blank=True, null=True)
    daystotransplantdatefromghh = models.IntegerField(blank=True, null=True)
    daystomaturityadjtransplantl = models.IntegerField(blank=True, null=True)
    daystomaturityadjtransplanth = models.IntegerField(blank=True, null=True)
    daystomaturityadjdirectsowingl = models.IntegerField(blank=True, null=True)
    daystomaturityadjdirectsowingh = models.IntegerField(blank=True, null=True)
    seedpercelllow = models.FloatField(blank=True, null=True)
    seedpercellhigh = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    createdbyuserid = models.IntegerField(blank=True, null=True)
    modifiedbyuserid = models.IntegerField(blank=True, null=True)
    createddate = models.DateField(blank=True, null=True)
    modifieddate = models.DateField(blank=True, null=True)
    daysharvestduration = models.IntegerField(blank=True, null=True)
    finalyieldrateperrowfoot = models.FloatField(blank=True, null=True)
    pelletedoption = models.IntegerField(blank=True, null=True)
    generic = models.IntegerField(blank=True, null=True)
    harvestunit = models.CharField(max_length=20, blank=True, null=True)
    seedingmethod = models.CharField(max_length=5, blank=True, null=True)
    inrowspacinglow = models.FloatField(blank=True, null=True)
    inrowspacinghigh = models.FloatField(blank=True, null=True)
    adjusteddtmlow = models.IntegerField(blank=True, null=True)
    adjusteddtmhigh = models.IntegerField(blank=True, null=True)
    seedsperspotspacelow = models.IntegerField(blank=True, null=True)
    seedsperspotspacehigh = models.IntegerField(blank=True, null=True)
    priceperunit = models.FloatField(blank=True, null=True)
    harvestunit1 = models.CharField(max_length=60, blank=True, null=True)
    harvestunit2 = models.CharField(max_length=60, blank=True, null=True)
    harvestunit3 = models.CharField(max_length=60, blank=True, null=True)
    harvestunit4 = models.CharField(max_length=60, blank=True, null=True)
    harvestunit5 = models.CharField(max_length=60, blank=True, null=True)
    harvestunit6 = models.CharField(max_length=60, blank=True, null=True)
    harvestunit7 = models.CharField(max_length=60, blank=True, null=True)
    harvestunit8 = models.CharField(max_length=60, blank=True, null=True)
    harvestunit9 = models.CharField(max_length=60, blank=True, null=True)
    yeildratepounds = models.FloatField(blank=True, null=True)
    yeildratebunches = models.FloatField(blank=True, null=True)
    yeildrateeach = models.FloatField(blank=True, null=True)
    yeildratepint = models.FloatField(blank=True, null=True)
    retailpricedefault = models.FloatField(blank=True, null=True)
    retailpricedefaultunit = models.CharField(max_length=64, blank=True, null=True)
    yeildrateounces = models.FloatField(blank=True, null=True)
    yeildratecount = models.FloatField(blank=True, null=True)
    yeildratehead = models.FloatField(blank=True, null=True)
    yeildratecase = models.FloatField(blank=True, null=True)
    yeildrateplant = models.FloatField(blank=True, null=True)
    isparentcropdefault = models.IntegerField(blank=True, null=True)
    iscroptypedefault = models.IntegerField(blank=True, null=True)
    isgrowingdefault = models.IntegerField(blank=True, null=True)
    harvestseasonid = models.IntegerField(blank=True, null=True)
    plantingyear = models.IntegerField(blank=True, null=True)
    seedingrateacrelow = models.FloatField(blank=True, null=True)
    seedingrateacrehigh = models.FloatField(blank=True, null=True)
    seedingrateozacrelow = models.FloatField(blank=True, null=True)
    seedingrateozacrehigh = models.FloatField(blank=True, null=True)
    numoftrees = models.IntegerField(blank=True, null=True)
    familyname = models.CharField(max_length=256, blank=True, null=True)
    seedingratelow1 = models.FloatField(blank=True, null=True)
    seedingratehigh1 = models.FloatField(blank=True, null=True)
    seedingratelow2 = models.FloatField(blank=True, null=True)
    seedingratehigh2 = models.FloatField(blank=True, null=True)
    seedingratelow3 = models.FloatField(blank=True, null=True)
    seedingratehigh3 = models.FloatField(blank=True, null=True)
    note = models.CharField(max_length=1024, blank=True, null=True)
    annualperrenialbiennial = models.CharField(max_length=1024, blank=True, null=True)
    harvestfrequency = models.IntegerField(blank=True, null=True)
    harvestwindow = models.IntegerField(blank=True, null=True)
    daymaturityaverage = models.IntegerField(blank=True, null=True)
    averagedaysgreenhouse = models.FloatField(blank=True, null=True)
    seedingratelbsacre = models.FloatField(blank=True, null=True)
    seedingrateouncessqft = models.FloatField(db_column='seedingRateouncessqft', blank=True, null=True)  # Field name made lowercase.
    seedingrateounces1000sqft = models.FloatField(db_column='seedingRateounces1000sqft', blank=True, null=True)  # Field name made lowercase.
    firstharvest = models.DateTimeField(blank=True, null=True)
    lastharvest = models.DateTimeField(blank=True, null=True)
    importdataid = models.IntegerField(blank=True, null=True)
    inrowspacing = models.FloatField(blank=True, null=True)
    firstfruitingyear = models.IntegerField(blank=True, null=True)
    rowindex = models.IntegerField(blank=True, null=True)
    organicaverageseednumber = models.FloatField(blank=True, null=True)
    organicseedweightunit = models.CharField(max_length=50, blank=True, null=True)
    nonorganicaverageseednumber = models.FloatField(blank=True, null=True)
    nonorganicseedweightunit = models.CharField(max_length=50, blank=True, null=True)
    pelletedaverageseednumber = models.FloatField(blank=True, null=True)
    pelletedseedweightunit = models.CharField(max_length=50, blank=True, null=True)
    organicpelletedaverageseednumber = models.FloatField(blank=True, null=True)
    organicpelletedaverageseedunit = models.CharField(max_length=50, blank=True, null=True)
    treatedaverageseednumber = models.FloatField(blank=True, null=True)
    treatedseedweightunit = models.CharField(max_length=50, blank=True, null=True)
    backup = models.CharField(max_length=1000, blank=True, null=True)
    driplineperbed = models.IntegerField(blank=True, null=True)
    rowperbed = models.IntegerField(blank=True, null=True)
    rowfeet = models.FloatField(blank=True, null=True)
    numofplants = models.FloatField(blank=True, null=True)
    numofflats = models.FloatField(blank=True, null=True)
    flatsize = models.FloatField(blank=True, null=True)
    saleprice = models.FloatField(blank=True, null=True)
    numofplantsgreenhouse = models.FloatField(blank=True, null=True)
    rowfeetunit = models.CharField(max_length=216, blank=True, null=True)
    harvestfrequencyunit = models.CharField(max_length=30, blank=True, null=True)
    yieldunit = models.CharField(max_length=30, blank=True, null=True)
    yieldunitconversion = models.FloatField(blank=True, null=True)
    yieldperrow = models.FloatField(blank=True, null=True)
    daytotransplant = models.IntegerField(blank=True, null=True)
    salepriceunit = models.CharField(max_length=50, blank=True, null=True)
    oneworddesc = models.CharField(max_length=30, blank=True, null=True)
    yieldratedefaultunit = models.CharField(max_length=30, blank=True, null=True)
    numofflatsunitid = models.IntegerField(blank=True, null=True)
    seedsourceid = models.IntegerField(blank=True, null=True)
    organicseed = models.TextField(blank=True, null=True)  # This field type is a guess.
    growinginahoophouse = models.TextField(blank=True, null=True)  # This field type is a guess.
    rootstock = models.CharField(max_length=500, blank=True, null=True)
    seedingrate = models.FloatField(blank=True, null=True)
    seedingrateunitid = models.IntegerField(blank=True, null=True)
    estimatedloss = models.FloatField(blank=True, null=True)
    yieldrateunitplanting = models.CharField(max_length=50, blank=True, null=True)
    firstyieldrate = models.FloatField(blank=True, null=True)
    firstyieldrateunit = models.CharField(max_length=30, blank=True, null=True)
    firstyieldrateunitplanting = models.CharField(max_length=50, blank=True, null=True)
    dayspottingup = models.CharField(max_length=50, blank=True, null=True)
    datespottingup = models.CharField(max_length=500, blank=True, null=True)
    flatpottype = models.CharField(max_length=500, blank=True, null=True)
    plantpercells = models.CharField(max_length=500, blank=True, null=True)
    numofseeds = models.IntegerField(blank=True, null=True)
    seedweightavg = models.FloatField(blank=True, null=True)
    seedweight = models.FloatField(blank=True, null=True)
    seedweightunit = models.CharField(max_length=512, blank=True, null=True)
    isorganic = models.IntegerField(blank=True, null=True)
    ispelleted = models.IntegerField(blank=True, null=True)
    istreated = models.IntegerField(blank=True, null=True)
    modifieddateseed = models.DateTimeField(blank=True, null=True)
    iseditsuccession = models.IntegerField(blank=True, null=True)
    extraorder = models.FloatField(blank=True, null=True)
    seasonid = models.IntegerField(blank=True, null=True)
    dtmdefault = models.BigIntegerField(blank=True, null=True)
    harvestunitdefault = models.CharField(max_length=60, blank=True, null=True)
    measurement = models.CharField(max_length=20, blank=True, null=True)
    inrowspacingunit = models.CharField(max_length=100, blank=True, null=True)
    seederid = models.IntegerField(blank=True, null=True)
    frontgearid = models.IntegerField(blank=True, null=True)
    reargearid = models.IntegerField(blank=True, null=True)
    rollerplateid = models.IntegerField(blank=True, null=True)
    isplantsale = models.TextField(blank=True, null=True)  # This field type is a guess.
    salepriceplantsale = models.FloatField(blank=True, null=True)
    salepriceplantsaleunit = models.CharField(max_length=100, blank=True, null=True)
    plantingamountunitid = models.IntegerField(blank=True, null=True)
    salepriceplantsaleunitid = models.IntegerField(blank=True, null=True)
    seedweightperflat = models.FloatField(blank=True, null=True)
    seedweightperflatunit = models.CharField(max_length=512, blank=True, null=True)
    seedweightperflattypeunit = models.IntegerField(blank=True, null=True)
    seedweightperflatmode = models.CharField(max_length=512, blank=True, null=True)
    numofflatsvalue = models.FloatField(blank=True, null=True)
    deliveryday = models.IntegerField(blank=True, null=True)
    transplantorderday = models.IntegerField(blank=True, null=True)
    ageoftransplant = models.IntegerField(blank=True, null=True)
    secondharvestwindow = models.IntegerField(blank=True, null=True)
    plantingamount = models.FloatField(blank=True, null=True)
    plantingamountunit = models.CharField(max_length=50, blank=True, null=True)
    planby = models.CharField(max_length=256, blank=True, null=True)
    planbyamount = models.FloatField(blank=True, null=True)
    planbyunit = models.CharField(max_length=255, blank=True, null=True)
    isgrowingforsale = models.TextField(blank=True, null=True)  # This field type is a guess.
    creeping = models.CharField(max_length=255, blank=True, null=True)
    creepingamount = models.FloatField(blank=True, null=True)
    creepingunit = models.CharField(max_length=255, blank=True, null=True)
    sqareaamount = models.FloatField(blank=True, null=True)
    sqareaunit = models.CharField(max_length=255, blank=True, null=True)
    patternunit = models.CharField(max_length=255, blank=True, null=True)
    generateplantingby = models.CharField(max_length=255, blank=True, null=True)
    seedingequipmentid = models.IntegerField(blank=True, null=True)
    transplantingequipmentid = models.IntegerField(blank=True, null=True)
    weedingequipmentid = models.IntegerField(blank=True, null=True)
    harvestingequipmentid = models.IntegerField(blank=True, null=True)
    isheirloom = models.TextField(blank=True, null=True)  # This field type is a guess.
    isgmo = models.TextField(blank=True, null=True)  # This field type is a guess.
    isinoculated = models.TextField(blank=True, null=True)  # This field type is a guess.
    seedchosetype = models.CharField(max_length=255, blank=True, null=True)
    seedunitmeasure = models.CharField(max_length=255, blank=True, null=True)
    avggerminationrate = models.FloatField(blank=True, null=True)
    seedsize = models.FloatField(blank=True, null=True)
    germinationtemperature = models.FloatField(blank=True, null=True)
    seedsizeunit = models.CharField(max_length=255, blank=True, null=True)
    seedingrateunitarea = models.CharField(max_length=100, blank=True, null=True)
    betweenrowspacing = models.FloatField(blank=True, null=True)
    betweenrowspacingunit = models.CharField(max_length=100, blank=True, null=True)
    planbydate = models.CharField(max_length=125, blank=True, null=True)
    seedpercell = models.FloatField(blank=True, null=True)
    seedtypeorganic = models.CharField(max_length=100, blank=True, null=True)
    originalid = models.IntegerField(blank=True, null=True)
    daystogermination = models.IntegerField(blank=True, null=True)

    def __str__ (self):
        return self.combinationkeyid

    class Meta:
        managed = False
        db_table = 'combinationdata'


# class DjangoAdminLog(models.Model):
#     action_time = models.DateTimeField()
#     object_id = models.TextField(blank=True, null=True)
#     object_repr = models.CharField(max_length=200)
#     action_flag = models.PositiveSmallIntegerField()
#     change_message = models.TextField()
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'django_admin_log'


# class DjangoContentType(models.Model):
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)

#     class Meta:
#         managed = False
#         db_table = 'django_content_type'
#         unique_together = (('app_label', 'model'),)


# class DjangoMigrations(models.Model):
#     id = models.AutoField(primary_key=True)
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'django_migrations'


# class DjangoSession(models.Model):
#     session_key = models.CharField(primary_key=True, max_length=40)
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'django_session'


# class AuthGroup(models.Model):
#     name = models.CharField(unique=True, max_length=150)

#     class Meta:
#         managed = False
#         db_table = 'auth_group'


# class AuthGroupPermissions(models.Model):
#     id = models.AutoField(primary_key=True)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#     permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_group_permissions'
#         unique_together = (('group', 'permission'),)


# class AuthPermission(models.Model):
#     name = models.CharField(max_length=255)
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
#     codename = models.CharField(max_length=100)

#     class Meta:
#         managed = False
#         db_table = 'auth_permission'
#         unique_together = (('content_type', 'codename'),)


# class AuthUser(models.Model):
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.IntegerField()
#     username = models.CharField(unique=True, max_length=150)
#     first_name = models.CharField(max_length=150)
#     last_name = models.CharField(max_length=150)
#     email = models.CharField(max_length=254)
#     is_staff = models.IntegerField()
#     is_active = models.IntegerField()
#     date_joined = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'auth_user'


# class AuthUserGroups(models.Model):
#     id = models.AutoField(primary_key=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_user_groups'
#         unique_together = (('user', 'group'),)


# class AuthUserUserPermissions(models.Model):
#     id = models.AutoField(primary_key=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_user_user_permissions'
#         unique_together = (('user', 'permission'),)


# class PollsChoice(models.Model):
#     id = models.AutoField(primary_key=True)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField()
#     question = models.ForeignKey('PollsQuestion', models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'polls_choice'