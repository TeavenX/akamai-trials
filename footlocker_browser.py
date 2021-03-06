import subprocess, sys, json, time, re, random

def install_dependencies():
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'requests'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'lxml'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'selenium'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'hyper'])

try:
    import requests, lxml.html as html, selenium
except:
    install_dependencies()
    import requests, lxml.html as html, selenium

rvals = ['1919619550','-1085185828','1577591477','1958559063','1590583886','803501153','1321416369','1332131968','-1787050453','-1476045391','-1249560680','-307900961','-897401638','1709140274','1475048621','-1170855828','-1829873084','-1512615331','-573415275','1361126098','-2058573278','40959895','-2105304209','259585831','1470773690','55918365','1320231474','2084738809','-505295563','1143137388','1913218796','-1192897860','1203223295','66119495','-1778730229','26628770','1296154381','-584358640','1600682329','1579143043','1593248957','832443918','1377201322','-1383584158','1294939072','-1871959036','-1859781450','-117935709','-382099010','625436701','-476385877','531048646','-759251245','911774456','-563759534','2061970342','-40119995','775316417','218935197','-933630176','-947094648','868242717','648976153','-1731653358','804413516','978905451','-916086900','2139001865','1931134240','-1783140051','-787136693','-883743074','846118576','-1508152253','282043467','360055229','1473945851','1079789831','435692209','-2061578350','1241732011','-1372025774','-220843305','187994788','1993212253','1260714330','1416566123','-841711560','-682481916','-410254237','-1870430781','349043025','1209088994','-1035776494','1847290625','859915229','197242163','228750819','1586905910','1710257694','-533479225','1190868050','-1167295923','-478770949','-844097030','-880781543','867322169','991305586','-316899420','1749902403','-958883221','-1474626848','-2000791231','-87268314','155229937','142006334','1246607029','1063218567','369994210','-574654566','233802077','-654616279','-1544608205','248066775','819991921','813579045','318510261','-2099981713','1916819915','426522241','1982873175','259558704','7390247','2123810049','-498916225','809855726','-644707227','1459695271','98083533','1765877848','-1551103271','-1914916132','-1624805901','171353429','1385742293','653579005','-1028161146','1398744446','-547031256','-626036720','614558751','-602697365','-1427703445','2085005153','-668277544','1867726891','-573393068','-2043001444','-1466500821','-601805002','-427186192','1532988208','-1782305859','546785630','-2006567750','1192026764','-1757464415','-323512492','-1481594226','107746788','-858095953','363553961','-1759692542','1099214035','-2087355482','-197391300','-2097876531','2019372932','-330462884','1802059905','827112250','1440380285','1224635923','228661045','-1700148237','-1107885465','1708523220','2121425108','145400717','2053165989','1991074146','-2059670094','907970681','-889775473','2053089761','-796487964','-905019286','-286402639','-16013481','1129656526','71710774','-1505440343','-189767019','125070456','1378857335','-1819753785','-1385511694','847630339','1478808121','-72336616','-972855174','1853700035','1801350837','1934535310','1072274748','473072677','286672874','1290074182','-1856922812','-751522268','-5098406','356375750','1578087896','750250045','-1379127821','1092940192','-587861234','478201070','-1428052155','-1695993807','-2097043394','-1593190121','-1199433119','1599735567','-1057332641','1170598106','-1695964367','-1246392310','-70986664','-1433865461','1338821594','2024394737','896291655','-1063918748','-889163780','109743002','-145873267','2055065344','-1705839794','-2006674797','-480956040','-1801080376','-590775339','1538551486','-369683672','519497992','384909440','-1388416608','-787454481','-1993255848','1682716682','1037609751','-810606368','1736687363','2000510099','-2102281879','1558637769','-311097705','-1192178266','47773444','1948656569','1161873092','-951048736','-2079626833','2009426827','345761982','894304389','-1626697646','721107868','-1546260301','-1637707796','-781064993','-750124620','-367108824','-673525963','264304389','549744999','-794556539','1717972987','1435020634','-1675825286','-107081082','1112523616','699759256','367377917','-1463603969','1324441104','-1816593552','-1613456344','490869722','1559339448','-74067172','-541683715','1662192069','2018599618','-572959812','2042829851','189160142','-1249815335','1103785409','1936119145','-1517947305','-1284864849','197088676','-1816834394','766141118','1704433804','-1286731005','-1366250393','-2105571876','-598615157','-1055442565','-1593803786','143630437','-1139822055','-1142992358','-1509630362','-1012102527','-1691277749','521886955','-1716457990','30418429','-1557083596','876328815','-1940689271','1445117709','-379192052','-544296800','522795208','805163601','1181531659','650394837','-837844458','688294557','-809360006','-1106953850','-2069658129','158071672','-1816789096','387608022','1262981659','2075336241','-1052535199','-84295270','2039801045','1276180853','637924993','1761797088','882312534','1485075697','415436276','1147321921','-603917496','-644104911','502702167','1539510865','125269488','712783122','-1710715380','1974577398','-1052131244','-1371148462','-1210879278','325829703','371811250','-1314100125','318722185','-1067219145','-454382934','1017004869','-1591108851','334070382','1814993873','-1748920183','-1091228950','-327186554','1378219086','-254827027','-303888314','575503543','2101976840','-488884528','932886960','-1316884601','-1650200082','-1224963172','-27412011','-1301969228','-1456099475','-384672208','-1282496015','1642829565','-657050157','-1628632322','180234781','-1998929305','-2005169686','-1444815886','-1635151002','522310787','1152247591','-1493472039','1943273938','-1090594941','1517780680','318350641','1642543420','-1873809268','858902114','-1429342033','1838638956','-1683478365','665412037','1541783728','-567529029','413806678','-2055651255','636169542','-1097141109','250339755','1945935419','2060519484','523155448','200546586','870091150','-523266311','1401089708','474982693','-107353058','-764546294','1290155937','648169110','-1320563705','-1387098377','1705503167','-1965727635','-352219242','-1179114679','113420698','-1100580052','570846249','1810139608','-1212825446','885702877','-169899872','1790033482','-1650719770','-263385051','-515136820','1038161212','317063640','1459420136','194496814','-533533230','1790297585','-1356734580','1331104353','296857357','-715706796','447515501','-1433405406','1761512573','2036266399','-755055013','-515076464','-1025441582','1929424273','610575639','-574041051','-1771809176','1949280899','330438175','-1141750351','-1980914855','-1606097695','-955729054','-452179264','-1922482972','526417380','-879823317','-775008737','-596702145','-573966033','1241876679','887262855','-1588822933','-1415955404','-773804218','1581815637','948966626','-1216149413','2139016132','337975345','-33573428','1213617969','1989911681','-2119608821','-41213167','-1990340325','1834833636','-293848541','-1425858879','-1986458541','-623467536','-797506645','362056146','212473745','-1689230474','-394425087','236803916','-1872666547','1405902914','951398908','1978095236','-1593291806','123009671','1205853975','1403527966','-1535915116','-488721237','-1049181822','-812742045','-167445342','-39111674','-1263330878','-1706879567','2067347052','982074201','1748313762','-333885754','2033293397','-659584628','1865178895','1965226239','1232653383','-1645832522','1731531052','-1001276925','193495896','-1426769622','498218889','1139220575','-841147282','880018530','-579566316','1403698366','68664375','1425788026','1039285343','697015034','-685385141','2076465263','312455508','985223281','1632686677','2105252647','238813255','-1466408624','-800527828','1688527567','726270712','-273068484','-726541808','-1701515442','510058953','-1534596372','-1327913956','280878654','-1324291206','1501903306','841134610','685838628','-551483193','-345330306','534424447','2023905992','-1615955669','794703389','-115709429','1209222046','1315141481','815463239','2047279810','-2025460172','-1750175514','-1026160150','1337853564','-1317189646','-667146955','1281707187','726798222','-635429788','-224987203','268950833','1079521959','990740997','-1915046840','2033183409','282386831','-881951289','-508220569','-693708758','360287008','-980578635','-1023114224','-1178122384','1695913874','551421118','850857098','1118854806','-1870334140','-327051239','453167828','582032928','529726466','1856049528','1438779730','-1389088879','1185846267','-29590896','-26864499','-915073899','1287113505','-1012843874','-111481341','-2134174216','375329486','-485558004','1282244679','-437044291','1262878945','405976126','425027485','1640831637','-1998447229','697505007','2135664190','1245141298','-1895666662','-1664600460','-1350685246','1996466766','-24736851','409021118','-1898505742','-2075970813','-821660025','-1814984979','12457071','-722582323','-1618844546','-1849135422','1682648929','-1254657902','-330070004','-843349991','1140300733','-2104779918','-349196793','-756992228','-954685976','1409756506','-1665844891','-299911622','1674235834','-516388511','857219923','479618590','-1596197028','-486496326','-1109871583','725503010','1210767108','-2128244318','1065527946','1464577803','1092653781','-1644477249','1233143389','-586023797','106384330','-2104041319','-1186319692','461243905','25595756','2102931830','-2133233931','410839511','-536078475','2028681347','-356864107','1422912419','-889542184','1817091230','1722631231','1964091435','-1630525560','-1585076229','-1115408152','-843016217','20573414','-801466790','1557792708','-867996866','-1454633379','1076138799','-1357611649','-1218451156','-101911350','1024649994','-1512516031','631301906','1401505396','-1522596724','-1351629660','163639791','888976073','-1661044280','-836766707','-1333016539','290258312','-522928569','2049946935','-200820066','32267053','-595624768','1047589054','985289260','1018747539','1961266294','724419348','-2141826340','1694081546','1306390764','1692599052','-1274503199','1644933566','-1782654497','-1207306799','1275759741','326929227','1730222348','-752979964','-101275514','-851366329','39138225','1365900813','1048068885','-1280957322','-12389475','-395545193','-1850619405','-681971173','155092670','2045809383','-222166599','-402383755','-909988708','-673094192','-708418333','1094974742','1878991571','-342061404','1174397370','-475783969','561390485','-866490938','-501870104','-1997306345','1788909846','-1847105454','-646097017','326653692','1207248055','598579603','-1706102054','972107653','2016692204','1742990036','615859509','-607090009','-995226329','1055874457','754841899','1542602917','-1564904467','-227616559','1690073697','-2088041129','-1209227257','-1434421297','-1448483309','-171069966','804911300','1492063891','-905259337','-1222671165','938157229','601827615','2018066515','-645964021','-2070414920','-360038513','1974644765','-2087292635','-1723552797','-306772180','1203905298','-1908503090','-1006565309','1678863212','-2140648882','-1460807595','-1129912713','-1368034651','-1897427641','-2061237009','826452833','-787700695','1426796525','-1610918874','1407647153','-1446689838','-1558338916','-99229512','-995602057','1335767898','-1104928729','410396303','-195281507','1537641829','-1699256547','354357359','-1435475507','-913544525','-1489773790','1119691483','-294321125','-892508414','-518339455','-213264468','236525672','-640446385','-1367499487','1522715265','-2018131672','1748855587','2007912115','-1825637043','881267438','988765549','-1541764875','1156607637','2120958635','-475143287','1028948223','-688947661','-718263351','-2049931440','-896473677','-1291404919','-1309608661','-735887547','-581097353','236726374','-1218530790','-2038950847','800074848','-965821767','1110904680','2040457953','1491280598','-933294525','1842626322','-291911095','-347923040','974385755','-1623222261','1319938952','-1399404455','-1314198589','-1140436709','-2007850929','892869667','1404342648','-1583754088','2054458945','1556165059','1024518257','-1184516413','-677424192','76628288','-1949070449','-1963003581','-1152369909','1231195435','-154917313','-1858093635','-423581049','1807559394','-279068014','-1579275590','-400738553','-35169951','1242709077','1576684620','-901182146','1958273577','-2031111477','-676273039','-1071253297','2032870686','-1511014805','399977971','-1557524590','-760599068','-1637305005','-1500165290','-1513990412','1943858191','34933398','-1379734258','-1175187724','-2007974800','450452824','-392732510','-569033888','1907535507','1898254782','-1964345534','-1312717925','-853349348','301076558','2018173149','-475534013','-1873719190','734604905','-46071940','-1320077394','-621772815','-334779638','371678636','-153881615','-948969914','1094860572','-943061160','61717600','720942721','-688268688','1962480368','865954035','903215997','-1084085295','-459129557','-616624552','-1516832268','-1082178193','275490211','-818190931','-1815615777','839588370','1239995079','1523860565','1235718686','-796000342','291017469','-1444906757','1048973760','-6896623','-435979846','-1577743332','-1291127461','-1325702419','381771464','278610750','-1297185420','-1634487454','-722322252','2140384648','-78991288','915446287','1896467987','799927925','1739901143','-1066737431','-295613692','-1841472770','919889803','930017324','-285064489','1184470398']

class footlockerbrowser():
    def __init__(self, query, keywords, excluded_keywords, style, size, proxy = None):
        with open('../device id ftl/device_id.json', 'r') as device_json:
            self.device_id = json.load(device_json)['device_id']
        self.bmak_permissions = '11321144241322243122'
        self.url = 'https://www.footlocker.com/'
        self.indx = 0
        self.rval = random.randint(0, 1001)
        self.rcfp = rvals[self.rval]
        self.query = query
        self.style = style
        self.size = size
        self.key_words = keywords
        self.excluded_key_words = excluded_keywords
        self.session = requests.session()
        if proxy!= None:
            self.session.proxies.update({'https':proxy})
        self.get_abck()


        self.find_item()
        self.get_product_id()
        # raise Exception()
        self.validate_abck()

        self.atc()
        self.session_timestamp()

        self.get_checkout()
        self.url = 'https://www.footlocker.com/checkout'
        self.indx = 1
        self.api_current_entries()
        self.validate_abck()

        self.api_satori()
        self.validate_abck()
        
        self.api_verification()
        self.validate_abck()

        self.api_email()
        self.api_current_entries()
        self.validate_abck()

        self.api_shipping()
        self.validate_abck()

        self.api_set_billing()
        self.api_current_entries()
        self.validate_abck()
        
        self.api_origin_key()
        self.validate_abck()

        time.sleep(1)
        self.get_adyen_key()
        self.get_encrypted_card_info()
        self.final_checkout()

    def get_adyen_key(self):
        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
            'Accept': '*/*',
            'Sec-Fetch-Site': 'same-site',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Dest': 'script',
            'Referer': 'https://checkoutshopper-live.adyen.com/checkoutshopper/assets/html/pub.v2.2615645779051917.aHR0cHM6Ly93d3cuZm9vdGxvY2tlci5jb20.ZI0osm1K5qAPJ1tNpTndq11GR78SVuXmn6UCYtYe-NU/securedFields.1.5.5.html',
            'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        }

        response = self.session.get('https://live.adyen.com/hpp/cse/js/2615645779051917.shtml', headers=headers).text
        self.adyen_key = re.search('"10001.*?"', response).group().strip('"')
        print(self.adyen_key)

    def get_encrypted_card_info(self):
        params = {'adyen_key':self.adyen_key, 'number':'4207 6702 3606 8972','month':'05','year':'2025','cvv':'422','name':'omar hu'}
        response = self.session.get('http://127.0.0.1:7000/adyen', params = params)
        self.adyen_encrypted = json.loads(response.text)

    def modify_sensor_data(self):
        print(self.sensor_data)
        self.sensor_data = re.sub(r'3\d3{3,}', self.bmak_permissions, self.sensor_data)
        self.sensor_data = re.sub(r'\D\d{3},1366', ',728,1366', self.sensor_data, count=1)
        self.sensor_data = re.sub(r'\d{3},-*\d{9,11},', '{},{},'.format(self.rval, self.rcfp), self.sensor_data)
        self.sensor_data = self.sensor_data.replace('685906754;1934461798;','1454252292;895908107;')
        self.sensor_data = self.sensor_data.replace('83.0.4103.0', '84.0.4147.89')
        self.sensor_data = self.sensor_data.replace('8212', '8286')
        self.sensor_data = self.sensor_data.replace('cwen:1', 'cwen:0')
        if 'checkout' in self.url:
            self.sensor_data = self.sensor_data.replace('0,0,0,0,1946,566,0;0,-1,0,1,2549,520,0;','0,-1,0,1,2140,937,1;0,-1,0,1,2024,821,1;0,-1,0,1,1676,473,1;0,-1,0,0,1677,474,1;0,-1,0,1,2241,1038,1;0,-1,0,1,1659,456,1;0,-1,0,1,1613,538,1;0,-1,0,1,1790,520,1;')

    def get_sensor(self):
        params = {'url': self.url, 'abck': self.session.cookies.get('_abck'), 'indx': self.indx}
        data = requests.get('http://127.0.0.1:7000/sensor', params=params).text
        print('data', data)
        data = json.loads(data)
        if data['type'] == 'cookie':
            del self.session.cookies['_abck']
            self.session.cookies.set(name='_abck', value=data['value'], domain='.footlocker.com')
            print('cookie recieved:', self.session.cookies.get('_abck'))
            return False
        elif data['type'] == 'sensor':
            self.sensor_data = data['value']
            self.modify_sensor_data()
            print(self.sensor_data)
            return True

    def alternate_page(self):
        r = self.session.get('http://127.0.0.1:7000/alternatepage')
        print(r, r.text)

    def validate_abck(self, n=0):
        print(n)
        if ('==' not in self.session.cookies.get('_abck')[-15:]):
            print('good so far', self.session.cookies.get('_abck'))
            return
        if not self.get_sensor():
            return
        headers = {
            'authority': 'www.footlocker.com',
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
            'content-type': 'text/plain;charset=UTF-8',
            'accept': '*/*',
            'origin': 'https://www.footlocker.com',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.footlocker.com/',
            'accept-language': 'en-US,en;q=0.9',
        }
        r = self.session.post('https://www.footlocker.com/assets/db28c267ui18045c24c7dce0795d42',json={'sensor_data': self.sensor_data}, headers=headers)
        print(self.session.cookies.get('_abck')[-20:])
        if '==' in self.session.cookies.get('_abck'):
            if n == 3:
                self.alternate_page()
                n=0
            time.sleep(random.randint(3,6))
            self.validate_abck(n=n+1)

    def server_abck(self):
        if ('=~' in self.session.cookies.get('_abck')[-12]) and ('==' not in self.session.cookies.get('_abck')[-12]):
            print(self.session.cookies.get('_abck'))
            return
        params = {'url': self.url, 'abck': self.session.cookies.get('_abck'), 'indx': self.indx}
        foo_cookie = self.session.get('http://127.0.0.1:7000/akamai', params=params).text
        if foo_cookie == 'error':
            print('error')
            self.validate_abck()
        del self.session.cookies['_abck']
        self.session.cookies.set(name='_abck', value= foo_cookie, domain='.footlocker.com')
        print(self.session.cookies.get('_abck'))

    def get_abck(self):
        headers = {
            'authority': 'www.footlocker.com',
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'none',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'accept-language': 'en-US,en;q=0.9',
        }
        self.session.get('https://www.footlocker.com/', headers=headers)

    def find_item(self):
        headers = {
            'authority': 'www.footlocker.com',
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        }
        params = (('query', self.query),)
        response = self.session.get('https://www.footlocker.com/search', headers=headers, params=params)
        stock = html.fromstring(response.content).xpath('.//a[contains(@class,"ProductCard-link")]')
        for _ in stock:
            fname = _.xpath('.//span[contains(@class,"ProductName-primary")]/text()')[0].lower().replace('\'','') + _.xpath('.//span[contains(@class,"ProductName-alt")]/text()')[0].lower().replace('\'','')
            if (all(word in fname for word in self.key_words.lower().split(' ')) and all(word not in fname for word in self.excluded_key_words.lower().split(' '))):
                self.product_href = _.get('href')
                self.product = ('https://www.footlocker.com/'+_.get('href'))

    def get_product_id(self):
        headers = {
            'authority': 'www.footlocker.com',
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'referer': 'https://www.footlocker.com/',
            'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        }
        response = self.session.get(self.product,headers=headers)
        print(response.content)
        page = json.loads(html.fromstring(response.content).xpath('/html/body/script[1]/text()')[0].split('\n')[2].split('=',1)[1].strip()[:-1])
        for product in page['details']['data'][self.product_href][0]['products']:
            if all(word in product['style']['value'].lower() for word in self.style.lower().split(' ')) and float(self.size) == float(product['size']['value'].strip()):
                self.product_code = product['code']
        self.x_api_key = page['config']['settings']['flapigee']['prod']

    def atc(self):#product id
        headers = {
            'authority': 'www.footlocker.com',
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'accept': 'application/json',
            'x-fl-productid': self.product_code,
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
            'content-type': 'application/json',
            'origin': 'https://www.footlocker.com',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.footlocker.com',
            'accept-language': 'en-US,en;q=0.9',
        }  # add to cart
        params = {'timestamp': time.time()}
        data = {"productQuantity": 1, "productId": self.product_code}
        response = self.session.post('https://www.footlocker.com/api/users/carts/current/entries', headers=headers, params=params, json=data, verify=False)
        print("add to cart", response.status_code, response.text)

    def session_timestamp(self):
        headers = {
            'authority': 'www.footlocker.com',
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'accept': 'application/json',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.footlocker.com/product/nike-lebron-17-low-mens/D5007101.html',
            'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        }

        params ={'timestamp': time.time()}
        response = self.session.get('https://www.footlocker.com/api/v3/session', headers=headers, params=params)
        self.csrf_token = json.loads(response.text)['data']['csrfToken']

    def get_checkout(self):
        headers = {
            'authority': 'www.footlocker.com',
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'none',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        }
        response = self.session.get('https://www.footlocker.com/checkout', headers=headers)

    def api_satori(self):
        headers = {
            'authority': 'www.footlocker.com',
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'accept': 'application/json',
            'x-csrf-token': self.csrf_token,
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
            'content-type': 'application/json',
            'origin': 'https://www.footlocker.com',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.footlocker.com/checkout',
            'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        }
        params = {'timestamp': time.time()}
        data = {"zipCode":"07093"}
        response = self.session.post('https://www.footlocker.com/api/satori/location-lookup/', headers=headers,params=params, json=data)
        print('satori', response, response.text)

    def api_verification(self):
        headers = {
            'authority': 'www.footlocker.com',
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'accept': 'application/json',
            'x-csrf-token': self.csrf_token,
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
            'content-type': 'application/json',
            'origin': 'https://www.footlocker.com',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.footlocker.com/checkout',
            'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        }

        params = {'timestamp': time.time()}
        data = '{"country":{"isocode":"US","name":"United States"},"region":{"countryIso":"US","isocode":"US-NJ","isocodeShort":"NJ","name":"New Jersey"},"line1":"7004 JFK BLVD E","line2":"38g","postalCode":"07093","town":"WEST NEW YORK"}'
        response = self.session.post('https://www.footlocker.com/api/v3/users/addresses/verification', headers=headers,params=params, data=data)
        print('verify', response, response.text)

    def api_current_entries(self):
        headers = {
            'authority': 'www.footlocker.com',
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'accept': 'application/json',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.footlocker.com/checkout',
            'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        }

        params = {
            'checkInventory': True,
            'checkPriceVariation': True,
            'timestamp': time.time()
        }
        response = self.session.get('https://www.footlocker.com/api/users/carts/current', headers=headers, params=params)
        print('current entries', response, response.text)

    def api_email(self):
        headers = {
            'authority': 'www.footlocker.com',
            'content-length': '0',
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'accept': 'application/json',
            'x-csrf-token': self.csrf_token,
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
            'origin': 'https://www.footlocker.com',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.footlocker.com/checkout',
            'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        }
        params = {'timestamp': time.time()}
        response = self.session.put('https://www.footlocker.com/api/users/carts/current/email/chouerzi@gmail.com',headers=headers, params=params)
        print('email', response, response.text)

    def api_shipping(self):
        headers = {
            'authority': 'www.footlocker.com',
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'accept': 'application/json',
            'x-csrf-token': self.csrf_token,
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
            'content-type': 'application/json',
            'origin': 'https://www.footlocker.com',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.footlocker.com/checkout',
            'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        }

        params = {'timestamp': time.time()}
        data = {"shippingAddress":
                    {"setAsBilling":True,"country":
                        {"isocode":"US","name":"United States"},
                     "id":None,
                     "region":{"countryIso":"US",
                               "isocode":"US-NJ",
                               "isocodeShort":"NJ",
                               "name":"New Jersey"},
                     "phone":"6463222013",
                     "type":"default",
                     "firstName":"omar",
                     "lastName":"hu",
                     "line1":"7004 JFK BLVD E",
                     "line2":"38g",
                     "postalCode":"07093",
                     "town":"WEST NEW YORK",
                     "email":False,
                     "regionFPO":None,
                     "shippingAddress":True,
                     "recordType":" "}}
        response = self.session.post('https://www.footlocker.com/api/users/carts/current/addresses/shipping', headers=headers, params=params, json=data)
        print('shipping', response, response.text)

    def api_set_billing(self):
        headers = {
            'authority': 'www.footlocker.com',
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'accept': 'application/json',
            'x-csrf-token': self.csrf_token,
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
            'content-type': 'application/json',
            'origin': 'https://www.footlocker.com',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.footlocker.com/checkout',
            'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        }

        params = {'timestamp': time.time()}

        data = {"setAsBilling":False,
                "country":{"isocode":"US",
                           "name":"United States"},
                "id":None,
                "region":{"countryIso":"US",
                          "isocode":"US-NJ",
                          "isocodeShort":"NJ",
                          "name":"New Jersey"},
                "phone":"6463222013",
                "type":"default",
                "firstName":"omar",
                "lastName":"hu",
                "line1":"7004 JFK BLVD E",
                "line2":"38g",
                "postalCode":"07093",
                "town":"WEST NEW YORK",
                "email":False,
                "regionFPO":None,
                "shippingAddress":True,
                "recordType":" "}
        response = self.session.post('https://www.footlocker.com/api/users/carts/current/set-billing', headers=headers,params=params, json=data)
        print('set billing',response,response.text)

    def api_origin_key(self):
        headers = {
            'authority': 'www.footlocker.com',
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'accept': 'application/json',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
            'x-api-key': self.x_api_key,
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.footlocker.com/checkout',
            'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        }
        params = {'timestamp': time.time()}
        response = self.session.get('https://www.footlocker.com/apigate/payment/origin-key', headers=headers, params=params)
        print('origin key', response, response.text)

    def card_validate(self):
        headers = {
            'authority': 'www.footlocker.com',
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'accept': 'application/json',
            'x-csrf-token': self.csrf_token,
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
            'content-type': 'application/json',
            'origin': 'https://www.footlocker.com',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.footlocker.com/checkout',
            'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        }
        params = {'timestamp': time.time()}
        data = {"cardNumber":"4207670236068972"}
        response = self.session.post('https://www.footlocker.com/paygate/cct', headers=headers, params=params, data=data)
        print('cct', response, response.text)

    def final_checkout(self):
        headers = {
            'authority': 'www.footlocker.com',
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'accept': 'application/json',
            'x-csrf-token': self.csrf_token,
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
            'content-type': 'application/json',
            'origin': 'https://www.footlocker.com',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.footlocker.com/checkout',
            'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        }

        params = {'timestamp':time.time()}
        print(self.device_id)
        data = {"preferredLanguage":"en",
                "securityCode":"",
                "deviceId":self.device_id,
                "cartId":self.session.cookies.get('cart-guid'),
                "encryptedCardNumber":self.adyen_encrypted["encryptedCardNumber"],
                "encryptedExpiryMonth":self.adyen_encrypted["encryptedExpiryMonth"],
                "encryptedExpiryYear":self.adyen_encrypted["encryptedExpiryYear"],
                "encryptedSecurityCode":self.adyen_encrypted["encryptedSecurityCode"],
                "returnUrl":"https://www.footlocker.com/adyen/checkout",
                "paymentMethod":"CREDITCARD",
                "browserInfo":{"screenWidth":1366,
                               "screenHeight":768,
                               "colorDepth":24,
                               "userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/83.0.4103.116 Safari/537.36",
                               "timeZoneOffset":240,
                               "language":"en-US",
                               "javaEnabled":False}}
        response = self.session.post('https://www.footlocker.com/api/users/orders', headers=headers, params=params, json=data)
        print('checkout', response, response.text)

ftl = footlockerbrowser(query='fear of god', keywords='moc', excluded_keywords='boys', style='beige', size='10.5')
#, proxy='204.150.214.210:65016'

