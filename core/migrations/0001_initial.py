# Generated by Django 4.2.1 on 2023-06-15 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Combinationdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('combinationkeyid', models.CharField(blank=True, max_length=50, null=True)),
                ('plantingmethodid', models.IntegerField(blank=True, null=True)),
                ('transplantrowspacinglow', models.FloatField(blank=True, null=True)),
                ('transplantrowspacinghigh', models.FloatField(blank=True, null=True)),
                ('rowspacinglow', models.FloatField(blank=True, null=True)),
                ('rowspacinghigh', models.FloatField(blank=True, null=True)),
                ('thinningspacinglow', models.FloatField(blank=True, null=True)),
                ('thinningspacinghigh', models.FloatField(blank=True, null=True)),
                ('seedingratelow', models.FloatField(blank=True, null=True)),
                ('seedingratehigh', models.FloatField(blank=True, null=True)),
                ('bandsseedingrateperfoot', models.FloatField(blank=True, null=True)),
                ('daymaturity', models.IntegerField(blank=True, null=True)),
                ('daytomaturityll', models.IntegerField(blank=True, null=True)),
                ('daytomaturitylh', models.IntegerField(blank=True, null=True)),
                ('daytomaturityhl', models.IntegerField(blank=True, null=True)),
                ('daytomaturityhh', models.IntegerField(blank=True, null=True)),
                ('daytomaturitytext', models.CharField(blank=True, max_length=256, null=True)),
                ('yieldrate', models.FloatField(blank=True, null=True)),
                ('daystotransplantdatefromghl', models.IntegerField(blank=True, null=True)),
                ('daystotransplantdatefromghh', models.IntegerField(blank=True, null=True)),
                ('daystomaturityadjtransplantl', models.IntegerField(blank=True, null=True)),
                ('daystomaturityadjtransplanth', models.IntegerField(blank=True, null=True)),
                ('daystomaturityadjdirectsowingl', models.IntegerField(blank=True, null=True)),
                ('daystomaturityadjdirectsowingh', models.IntegerField(blank=True, null=True)),
                ('seedpercelllow', models.FloatField(blank=True, null=True)),
                ('seedpercellhigh', models.FloatField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=20, null=True)),
                ('createdbyuserid', models.IntegerField(blank=True, null=True)),
                ('modifiedbyuserid', models.IntegerField(blank=True, null=True)),
                ('createddate', models.DateField(blank=True, null=True)),
                ('modifieddate', models.DateField(blank=True, null=True)),
                ('daysharvestduration', models.IntegerField(blank=True, null=True)),
                ('finalyieldrateperrowfoot', models.FloatField(blank=True, null=True)),
                ('pelletedoption', models.IntegerField(blank=True, null=True)),
                ('generic', models.IntegerField(blank=True, null=True)),
                ('harvestunit', models.CharField(blank=True, max_length=20, null=True)),
                ('seedingmethod', models.CharField(blank=True, max_length=5, null=True)),
                ('inrowspacinglow', models.FloatField(blank=True, null=True)),
                ('inrowspacinghigh', models.FloatField(blank=True, null=True)),
                ('adjusteddtmlow', models.IntegerField(blank=True, null=True)),
                ('adjusteddtmhigh', models.IntegerField(blank=True, null=True)),
                ('seedsperspotspacelow', models.IntegerField(blank=True, null=True)),
                ('seedsperspotspacehigh', models.IntegerField(blank=True, null=True)),
                ('priceperunit', models.FloatField(blank=True, null=True)),
                ('harvestunit1', models.CharField(blank=True, max_length=60, null=True)),
                ('harvestunit2', models.CharField(blank=True, max_length=60, null=True)),
                ('harvestunit3', models.CharField(blank=True, max_length=60, null=True)),
                ('harvestunit4', models.CharField(blank=True, max_length=60, null=True)),
                ('harvestunit5', models.CharField(blank=True, max_length=60, null=True)),
                ('harvestunit6', models.CharField(blank=True, max_length=60, null=True)),
                ('harvestunit7', models.CharField(blank=True, max_length=60, null=True)),
                ('harvestunit8', models.CharField(blank=True, max_length=60, null=True)),
                ('harvestunit9', models.CharField(blank=True, max_length=60, null=True)),
                ('yeildratepounds', models.FloatField(blank=True, null=True)),
                ('yeildratebunches', models.FloatField(blank=True, null=True)),
                ('yeildrateeach', models.FloatField(blank=True, null=True)),
                ('yeildratepint', models.FloatField(blank=True, null=True)),
                ('retailpricedefault', models.FloatField(blank=True, null=True)),
                ('retailpricedefaultunit', models.CharField(blank=True, max_length=64, null=True)),
                ('yeildrateounces', models.FloatField(blank=True, null=True)),
                ('yeildratecount', models.FloatField(blank=True, null=True)),
                ('yeildratehead', models.FloatField(blank=True, null=True)),
                ('yeildratecase', models.FloatField(blank=True, null=True)),
                ('yeildrateplant', models.FloatField(blank=True, null=True)),
                ('isparentcropdefault', models.IntegerField(blank=True, null=True)),
                ('iscroptypedefault', models.IntegerField(blank=True, null=True)),
                ('isgrowingdefault', models.IntegerField(blank=True, null=True)),
                ('harvestseasonid', models.IntegerField(blank=True, null=True)),
                ('plantingyear', models.IntegerField(blank=True, null=True)),
                ('seedingrateacrelow', models.FloatField(blank=True, null=True)),
                ('seedingrateacrehigh', models.FloatField(blank=True, null=True)),
                ('seedingrateozacrelow', models.FloatField(blank=True, null=True)),
                ('seedingrateozacrehigh', models.FloatField(blank=True, null=True)),
                ('numoftrees', models.IntegerField(blank=True, null=True)),
                ('familyname', models.CharField(blank=True, max_length=256, null=True)),
                ('seedingratelow1', models.FloatField(blank=True, null=True)),
                ('seedingratehigh1', models.FloatField(blank=True, null=True)),
                ('seedingratelow2', models.FloatField(blank=True, null=True)),
                ('seedingratehigh2', models.FloatField(blank=True, null=True)),
                ('seedingratelow3', models.FloatField(blank=True, null=True)),
                ('seedingratehigh3', models.FloatField(blank=True, null=True)),
                ('note', models.CharField(blank=True, max_length=1024, null=True)),
                ('annualperrenialbiennial', models.CharField(blank=True, max_length=1024, null=True)),
                ('harvestfrequency', models.IntegerField(blank=True, null=True)),
                ('harvestwindow', models.IntegerField(blank=True, null=True)),
                ('daymaturityaverage', models.IntegerField(blank=True, null=True)),
                ('averagedaysgreenhouse', models.FloatField(blank=True, null=True)),
                ('seedingratelbsacre', models.FloatField(blank=True, null=True)),
                ('seedingrateouncessqft', models.FloatField(blank=True, db_column='seedingRateouncessqft', null=True)),
                ('seedingrateounces1000sqft', models.FloatField(blank=True, db_column='seedingRateounces1000sqft', null=True)),
                ('firstharvest', models.DateTimeField(blank=True, null=True)),
                ('lastharvest', models.DateTimeField(blank=True, null=True)),
                ('importdataid', models.IntegerField(blank=True, null=True)),
                ('inrowspacing', models.FloatField(blank=True, null=True)),
                ('firstfruitingyear', models.IntegerField(blank=True, null=True)),
                ('rowindex', models.IntegerField(blank=True, null=True)),
                ('organicaverageseednumber', models.FloatField(blank=True, null=True)),
                ('organicseedweightunit', models.CharField(blank=True, max_length=50, null=True)),
                ('nonorganicaverageseednumber', models.FloatField(blank=True, null=True)),
                ('nonorganicseedweightunit', models.CharField(blank=True, max_length=50, null=True)),
                ('pelletedaverageseednumber', models.FloatField(blank=True, null=True)),
                ('pelletedseedweightunit', models.CharField(blank=True, max_length=50, null=True)),
                ('organicpelletedaverageseednumber', models.FloatField(blank=True, null=True)),
                ('organicpelletedaverageseedunit', models.CharField(blank=True, max_length=50, null=True)),
                ('treatedaverageseednumber', models.FloatField(blank=True, null=True)),
                ('treatedseedweightunit', models.CharField(blank=True, max_length=50, null=True)),
                ('backup', models.CharField(blank=True, max_length=1000, null=True)),
                ('driplineperbed', models.IntegerField(blank=True, null=True)),
                ('rowperbed', models.IntegerField(blank=True, null=True)),
                ('rowfeet', models.FloatField(blank=True, null=True)),
                ('numofplants', models.FloatField(blank=True, null=True)),
                ('numofflats', models.FloatField(blank=True, null=True)),
                ('flatsize', models.FloatField(blank=True, null=True)),
                ('saleprice', models.FloatField(blank=True, null=True)),
                ('numofplantsgreenhouse', models.FloatField(blank=True, null=True)),
                ('rowfeetunit', models.CharField(blank=True, max_length=216, null=True)),
                ('harvestfrequencyunit', models.CharField(blank=True, max_length=30, null=True)),
                ('yieldunit', models.CharField(blank=True, max_length=30, null=True)),
                ('yieldunitconversion', models.FloatField(blank=True, null=True)),
                ('yieldperrow', models.FloatField(blank=True, null=True)),
                ('daytotransplant', models.IntegerField(blank=True, null=True)),
                ('salepriceunit', models.CharField(blank=True, max_length=50, null=True)),
                ('oneworddesc', models.CharField(blank=True, max_length=30, null=True)),
                ('yieldratedefaultunit', models.CharField(blank=True, max_length=30, null=True)),
                ('numofflatsunitid', models.IntegerField(blank=True, null=True)),
                ('seedsourceid', models.IntegerField(blank=True, null=True)),
                ('organicseed', models.TextField(blank=True, null=True)),
                ('growinginahoophouse', models.TextField(blank=True, null=True)),
                ('rootstock', models.CharField(blank=True, max_length=500, null=True)),
                ('seedingrate', models.FloatField(blank=True, null=True)),
                ('seedingrateunitid', models.IntegerField(blank=True, null=True)),
                ('estimatedloss', models.FloatField(blank=True, null=True)),
                ('yieldrateunitplanting', models.CharField(blank=True, max_length=50, null=True)),
                ('firstyieldrate', models.FloatField(blank=True, null=True)),
                ('firstyieldrateunit', models.CharField(blank=True, max_length=30, null=True)),
                ('firstyieldrateunitplanting', models.CharField(blank=True, max_length=50, null=True)),
                ('dayspottingup', models.CharField(blank=True, max_length=50, null=True)),
                ('datespottingup', models.CharField(blank=True, max_length=500, null=True)),
                ('flatpottype', models.CharField(blank=True, max_length=500, null=True)),
                ('plantpercells', models.CharField(blank=True, max_length=500, null=True)),
                ('numofseeds', models.IntegerField(blank=True, null=True)),
                ('seedweightavg', models.FloatField(blank=True, null=True)),
                ('seedweight', models.FloatField(blank=True, null=True)),
                ('seedweightunit', models.CharField(blank=True, max_length=512, null=True)),
                ('isorganic', models.IntegerField(blank=True, null=True)),
                ('ispelleted', models.IntegerField(blank=True, null=True)),
                ('istreated', models.IntegerField(blank=True, null=True)),
                ('modifieddateseed', models.DateTimeField(blank=True, null=True)),
                ('iseditsuccession', models.IntegerField(blank=True, null=True)),
                ('extraorder', models.FloatField(blank=True, null=True)),
                ('seasonid', models.IntegerField(blank=True, null=True)),
                ('dtmdefault', models.BigIntegerField(blank=True, null=True)),
                ('harvestunitdefault', models.CharField(blank=True, max_length=60, null=True)),
                ('measurement', models.CharField(blank=True, max_length=20, null=True)),
                ('inrowspacingunit', models.CharField(blank=True, max_length=100, null=True)),
                ('seederid', models.IntegerField(blank=True, null=True)),
                ('frontgearid', models.IntegerField(blank=True, null=True)),
                ('reargearid', models.IntegerField(blank=True, null=True)),
                ('rollerplateid', models.IntegerField(blank=True, null=True)),
                ('isplantsale', models.TextField(blank=True, null=True)),
                ('salepriceplantsale', models.FloatField(blank=True, null=True)),
                ('salepriceplantsaleunit', models.CharField(blank=True, max_length=100, null=True)),
                ('plantingamountunitid', models.IntegerField(blank=True, null=True)),
                ('salepriceplantsaleunitid', models.IntegerField(blank=True, null=True)),
                ('seedweightperflat', models.FloatField(blank=True, null=True)),
                ('seedweightperflatunit', models.CharField(blank=True, max_length=512, null=True)),
                ('seedweightperflattypeunit', models.IntegerField(blank=True, null=True)),
                ('seedweightperflatmode', models.CharField(blank=True, max_length=512, null=True)),
                ('numofflatsvalue', models.FloatField(blank=True, null=True)),
                ('deliveryday', models.IntegerField(blank=True, null=True)),
                ('transplantorderday', models.IntegerField(blank=True, null=True)),
                ('ageoftransplant', models.IntegerField(blank=True, null=True)),
                ('secondharvestwindow', models.IntegerField(blank=True, null=True)),
                ('plantingamount', models.FloatField(blank=True, null=True)),
                ('plantingamountunit', models.CharField(blank=True, max_length=50, null=True)),
                ('planby', models.CharField(blank=True, max_length=256, null=True)),
                ('planbyamount', models.FloatField(blank=True, null=True)),
                ('planbyunit', models.CharField(blank=True, max_length=255, null=True)),
                ('isgrowingforsale', models.TextField(blank=True, null=True)),
                ('creeping', models.CharField(blank=True, max_length=255, null=True)),
                ('creepingamount', models.FloatField(blank=True, null=True)),
                ('creepingunit', models.CharField(blank=True, max_length=255, null=True)),
                ('sqareaamount', models.FloatField(blank=True, null=True)),
                ('sqareaunit', models.CharField(blank=True, max_length=255, null=True)),
                ('patternunit', models.CharField(blank=True, max_length=255, null=True)),
                ('generateplantingby', models.CharField(blank=True, max_length=255, null=True)),
                ('seedingequipmentid', models.IntegerField(blank=True, null=True)),
                ('transplantingequipmentid', models.IntegerField(blank=True, null=True)),
                ('weedingequipmentid', models.IntegerField(blank=True, null=True)),
                ('harvestingequipmentid', models.IntegerField(blank=True, null=True)),
                ('isheirloom', models.TextField(blank=True, null=True)),
                ('isgmo', models.TextField(blank=True, null=True)),
                ('isinoculated', models.TextField(blank=True, null=True)),
                ('seedchosetype', models.CharField(blank=True, max_length=255, null=True)),
                ('seedunitmeasure', models.CharField(blank=True, max_length=255, null=True)),
                ('avggerminationrate', models.FloatField(blank=True, null=True)),
                ('seedsize', models.FloatField(blank=True, null=True)),
                ('germinationtemperature', models.FloatField(blank=True, null=True)),
                ('seedsizeunit', models.CharField(blank=True, max_length=255, null=True)),
                ('seedingrateunitarea', models.CharField(blank=True, max_length=100, null=True)),
                ('betweenrowspacing', models.FloatField(blank=True, null=True)),
                ('betweenrowspacingunit', models.CharField(blank=True, max_length=100, null=True)),
                ('planbydate', models.CharField(blank=True, max_length=125, null=True)),
                ('seedpercell', models.FloatField(blank=True, null=True)),
                ('seedtypeorganic', models.CharField(blank=True, max_length=100, null=True)),
                ('originalid', models.IntegerField(blank=True, null=True)),
                ('daystogermination', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'combinationdata',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cropcategory',
            fields=[
                ('categoryid', models.AutoField(primary_key=True, serialize=False)),
                ('categoryname', models.CharField(blank=True, max_length=512, null=True)),
                ('status', models.CharField(blank=True, max_length=20, null=True)),
                ('createddate', models.DateTimeField(blank=True, null=True)),
                ('createdbyuserid', models.IntegerField(blank=True, null=True)),
                ('modifieddate', models.DateTimeField(blank=True, null=True)),
                ('modifiedbyuserid', models.IntegerField(blank=True, null=True)),
                ('notes', models.CharField(blank=True, max_length=4000, null=True)),
            ],
            options={
                'db_table': 'cropcategory',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Crops',
            fields=[
                ('cropid', models.AutoField(primary_key=True, serialize=False)),
                ('farmid', models.IntegerField(blank=True, null=True)),
                ('imagename', models.CharField(blank=True, max_length=125, null=True)),
                ('isfinished', models.IntegerField(blank=True, null=True)),
                ('notes', models.CharField(blank=True, max_length=1000, null=True)),
                ('status', models.CharField(blank=True, max_length=20, null=True)),
                ('createdbyuserid', models.IntegerField(blank=True, null=True)),
                ('createddate', models.DateTimeField(blank=True, null=True)),
                ('modifiedbyuserid', models.IntegerField(blank=True, null=True)),
                ('modifieddate', models.DateTimeField(blank=True, null=True)),
                ('parentname', models.CharField(blank=True, max_length=125, null=True)),
                ('croptypename', models.CharField(blank=True, max_length=125, null=True)),
                ('varietyname', models.CharField(blank=True, max_length=125, null=True)),
                ('totalsuccession', models.IntegerField(blank=True, null=True)),
                ('harvestunitdefault', models.CharField(blank=True, max_length=32, null=True)),
                ('yeildunitdefault', models.CharField(blank=True, max_length=32, null=True)),
                ('yeildratedefault', models.FloatField(blank=True, null=True)),
                ('currentharvestunit', models.CharField(blank=True, max_length=32, null=True)),
                ('color', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'crops',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Croptype',
            fields=[
                ('croptypeid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=512, null=True)),
                ('imagename', models.CharField(blank=True, max_length=125, null=True)),
                ('status', models.CharField(blank=True, max_length=20, null=True)),
                ('notes', models.CharField(blank=True, max_length=512, null=True)),
                ('createdbyuserid', models.IntegerField(blank=True, null=True)),
                ('createddate', models.DateTimeField(blank=True, null=True)),
                ('modifiedbyuserid', models.IntegerField(blank=True, null=True)),
                ('modifieddate', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'croptype',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Growingmethods',
            fields=[
                ('growingmethodid', models.AutoField(primary_key=True, serialize=False)),
                ('growingmethodname', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.CharField(blank=True, max_length=20, null=True)),
                ('createddate', models.DateTimeField(blank=True, null=True)),
                ('createdbyuserid', models.IntegerField(blank=True, null=True)),
                ('modifieddate', models.DateTimeField(blank=True, null=True)),
                ('modifiedbyuserid', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'growingmethods',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Harvestseason',
            fields=[
                ('harvestseasonid', models.AutoField(primary_key=True, serialize=False)),
                ('harvestseasonname', models.CharField(blank=True, max_length=52, null=True)),
                ('status', models.CharField(blank=True, max_length=20, null=True)),
                ('createddate', models.DateTimeField(blank=True, null=True)),
                ('createdbyuserid', models.IntegerField(blank=True, null=True)),
                ('modifieddate', models.DateTimeField(blank=True, null=True)),
                ('modifiedbyuserid', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'harvestseason',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Mastercrop',
            fields=[
                ('mastercropid', models.AutoField(primary_key=True, serialize=False)),
                ('varietyname', models.CharField(blank=True, max_length=512, null=True)),
                ('longname', models.CharField(blank=True, max_length=512, null=True)),
                ('naturalname', models.CharField(blank=True, max_length=512, null=True)),
                ('searchtags', models.CharField(blank=True, max_length=512, null=True)),
                ('colorname', models.CharField(blank=True, max_length=125, null=True)),
                ('imagename', models.CharField(blank=True, max_length=125, null=True)),
                ('notes', models.CharField(blank=True, max_length=512, null=True)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('history', models.CharField(blank=True, max_length=1000, null=True)),
                ('farmid', models.IntegerField(blank=True, null=True)),
                ('defaultcombinationkeyid', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.CharField(blank=True, max_length=20, null=True)),
                ('createdbyuserid', models.IntegerField(blank=True, null=True)),
                ('createddate', models.DateTimeField(blank=True, null=True)),
                ('modifiedbyuserid', models.IntegerField(blank=True, null=True)),
                ('modifieddate', models.DateTimeField(blank=True, null=True)),
                ('refimageid', models.IntegerField(blank=True, null=True)),
                ('imagesource', models.CharField(blank=True, max_length=512, null=True)),
                ('generic', models.IntegerField(blank=True, null=True)),
                ('iscroptypedefault', models.IntegerField(blank=True, null=True)),
                ('isparentcropdefault', models.IntegerField(blank=True, null=True)),
                ('backup', models.CharField(blank=True, max_length=1000, null=True)),
                ('varietysearchtags', models.CharField(blank=True, max_length=512, null=True)),
                ('color', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'mastercrop',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Parentcrop',
            fields=[
                ('parentcropid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=125, null=True)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('imagename', models.CharField(blank=True, max_length=125, null=True)),
                ('farmid', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=20, null=True)),
                ('createddate', models.DateTimeField(blank=True, null=True)),
                ('createdbyuserid', models.IntegerField(blank=True, null=True)),
                ('modifieddate', models.DateTimeField(blank=True, null=True)),
                ('modifiedbyuserid', models.IntegerField(blank=True, null=True)),
                ('refimagid', models.IntegerField(blank=True, null=True)),
                ('imagesource', models.CharField(blank=True, max_length=512, null=True)),
                ('harvestunit', models.CharField(blank=True, max_length=52, null=True)),
                ('searchtags', models.CharField(blank=True, max_length=512, null=True)),
                ('note', models.CharField(blank=True, max_length=512, null=True)),
                ('hasvariety', models.TextField(blank=True, null=True)),
                ('mappingid', models.BigIntegerField(blank=True, null=True)),
                ('color', models.CharField(blank=True, max_length=255, null=True)),
                ('totalplanting', models.IntegerField(blank=True, null=True)),
                ('hasplantsale', models.TextField(blank=True, null=True)),
                ('defaultseedingmethod', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'parentcrop',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Parentcroptype',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(blank=True, max_length=20, null=True)),
                ('createddate', models.DateTimeField(blank=True, null=True)),
                ('createdbyuserid', models.IntegerField(blank=True, null=True)),
                ('modifieddate', models.DateTimeField(blank=True, null=True)),
                ('modifiedbyuserid', models.IntegerField(blank=True, null=True)),
                ('parentname', models.CharField(blank=True, max_length=125, null=True)),
                ('croptypename', models.CharField(blank=True, max_length=125, null=True)),
                ('imagename', models.CharField(blank=True, max_length=125, null=True)),
            ],
            options={
                'db_table': 'parentcroptype',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PollsQuestion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('questiontext', models.CharField(max_length=200)),
                ('createddate', models.DateTimeField()),
            ],
            options={
                'db_table': 'polls_question',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Subtasktype',
            fields=[
                ('subtypeid', models.AutoField(primary_key=True, serialize=False)),
                ('tasktypeid', models.IntegerField(blank=True, null=True)),
                ('typename', models.CharField(blank=True, max_length=512, null=True)),
                ('groupby', models.CharField(blank=True, max_length=5, null=True)),
                ('status', models.CharField(blank=True, max_length=20, null=True)),
                ('createddate', models.DateTimeField(blank=True, null=True)),
                ('createdbyuserid', models.IntegerField(blank=True, null=True)),
                ('modifieddate', models.DateTimeField(blank=True, null=True)),
                ('modifiedbyuserid', models.IntegerField(blank=True, null=True)),
                ('color', models.CharField(blank=True, max_length=10, null=True)),
                ('sign', models.CharField(blank=True, max_length=2, null=True)),
                ('textcolor', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'subtasktype',
                'managed': False,
            },
        ),
    ]
