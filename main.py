import requests
from bs4 import BeautifulSoup as bs
from time import sleep
headers = {"User-agent": "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0"}
links = []


file = 'Dctrs.csv'

l = ['/neonatolog/',
'/detskiy-ginekolog/',
'/detskiy-gematolog/',
'/detskiy-kardiolog/',
'/detskiy-pulmonolog/',
'/detskiy-ortoped-travmatolog/',
'/detskiy-otorinolaringolog/',
'/detskiy-dermatolog/',
'/detskiy-onkolog/',
'/detskiy-nefrolog/',
'/detskiy-infekcionist/',
'/detskiy-revmatolog/',
'/detskiy-nevrolog/',
'/detskiy-allergolog/',
'/detskiy-massagist/',
'/detskiy-psihiatr/',
'/detskiy-hirurg/',
'/detskiy-psiholog/',
'/detskiy-endokrinolog/',
'/detskiy-urolog/',
'/logoped/',
'/stomatolog-gigienist/',
'/paradontolog/',
'/pediatr/',
'/stomatolog/',
'/stomatolog-ortoped/'
'/stomatolog-hirurg/',
'/ortodont/',
'/detskiy-stomatolog/']

citys = ['moskva','stavropol','spb','barnaul','vladivostok','volgograd','voronezh','ekaterinburg','izhevsk','krasnodar','krasnoyarsk','nnovgorod','novosibirsk'
,'omsk','perm','rostov-na-donu','samara','saratov','tolyatti','ulyanovsk','ufa','chelyabinsk','yaroslavl','Abaza','Abakan','Abdulino','Abinsk','Agidel','Agryz','Adygeisk','Aznakaevo','Azov','Ak-Dovurak','Aksai','Alagir','Alapaevsk','Alatyr','Aldan','Aleisk','Alexandrov','Alexandrovsk','Alexandrovsk-Sakhalinsky','Alekseevka','Aleksin','Alzamay','Almetyevsk','Amursk','Anadyr','Anapa','Angarsk','Andreapol','Anzhero-Sudzhensk','Aniva','Apatity','Aprelevka','Apsheronsk','Aramil','Argun','Ardatov','Ardon','Arzamas','Arzamas','Arkadak','Armavir','Arseniev','Artyom','Artyomovsk','Artyomovsky','Arkhangelsk','Asbestos','Asino','Astrakhan','Atkarsk','Akhtubinsk','Achinsk','Asha','Babaevo','Babushkin','Bavly','Bagrationovsk','Baikalsk','Baimak','Bakal','Baksan','Balabanovo','Balakovo','Balakhna','Balakhna','Balashikha','Balashov','Baley','Baltiysk','Barabinsk','Barnaul','Profit','Bataysk','Bezhetsk','Belaya','Kalitva','White','Kholunitsa','Belgorod','Belebey','Belev','Belinsky','Belovo','Belogorsk','Belozersk','Belokurikha','Belomorsk','Beloretsk','Belorechensk','Belousovo','Beloyarsky','White','Berdsk','Berezniki','Berezovsky','Berezovsky','Beslan','Biysk','Bikin','Bilibino','Birobidzhan','Birsk','Biryusinsk','Biryuch','Blagoveshchensk','Blagoveshchensk','Grateful','Bobrov','Bogdanovich','Bogoroditsk','Bogorodsk','Bogorodsk','Bogotol','Boguchar','Bodaibo','Boksitogorsk','Bulgarians','Bologoye','Swamp','Bolokhovo','Bolkhov','Big','Stone','Boron','Boron','Borzya','Borisoglebsk','Borovichi','Borovsk','Borodino','Bratsk','Bronnitsy','Bryansk','Bugulma','Buguruslan','Budyonnovsk','Buzuluk','Buinsk','Buoy','Buinaksk','Buturlinovka','Valdai','Valuyki','Velizh','Velikie','Luki','Velikiy','Novgorod','Veliky','Ustyug','Velsk','Venev','Vereshchagino','Vereya','Verkhneuralsk','Verkhniy','Tagil','Verkhniy','Ufaley','Upper','Pyshma','Verkhnyaya','Salda','Verkhnyaya','Tura','Verkhoturye','Verkhoyansk','Vesyegonsk','Vetluga','Vetluga','Vidnoe','Vilyuisk','Vilyuchinsk','Vikhorevka','Vichuga','Vladivostok','Vladikavkaz','Vladimir','Volgograd','Volgodonsk','Volgorechensk','Volzhsk','Volzhsky','Vologda','Volodarsk','Volodarsk','Volokolamsk','Volosovo','Volkhov','Volchansk','Volsk','Vorkuta','Voronezh','Vorsma','Vorsma','Voskresensk','Votkinsk','Vsevolozhsk','Vuktyl','Vyborg','Vyksa','Vyksa','Vysokovsk','Vysotsk','Vytegra','Vyshny','Volochek','Vyazemsky','Vyazniki','Vyazma','Vyatskiye','Polyany','Gavrilov','Posad','Gavrilov-Yam','Gagarin','Gadzhievo','Guy','Galich','Gatchina','Gvardeysk','Gdov','Gelendzhik','Georgievsk','Glazov','Gorbatov','Gorbatov','Gorno-Altaysk','Gornozavodsk','Gornozavodsk','Miner','Gorodets','Gorodets','Settlement','Gorodovikovsk','Gorokhovets','Hot','key','Grayvoron','Gremyachinsk','Grozny','Mud','Gryazovets','Lipakha','Gubkin','Gubkinsky','Gudermes','Gukovo','Gulkevichi','Guryevsk','Guryevsk','Gusev','Gusinoozyorsk','Gus-Khrustalny','Davlekanovo','Dagestan','Lights','Dalmatovo','Dalnegorsk','Dalnerechensk','Danilov','Dankov','Degtyarsk','Dedovsk','Demidov','Derbent','Desnogorsk','Dzerzhinsk','Dzerzhinsk','Dzerzhinsky','Divnogorsk','Digora','Dimitrovgrad','Dmitriev-Lgovsky','Dmitrov','Dmitrovsk','Bottom','Dobryanka','Dolgoprudny','Dolinsk','Domodedovo','Donetsk','Donskoy','Dorogobuzh','Drezna','Dubna','Dubovka','Dudinka','Dukhovshchina','Dyurtyuli','Dyatkovo','Egorievsk','Yeisk','Ekaterinburg','Elabuga','Dace','Yelizovo','Yelnya','Emanzhelinsk','Emva','Yeniseisk','Ermolino','Ershov','Essentuki','Efremov','Zheleznovodsk','Zheleznogorsk','Zheleznogorsk','Zheleznogorsk-Ilimsky','Railway','Zherdevka','Zhigulevsk','Zhizdra','Zhirnovsk','Zhukov','Zhukovka','Zhukovsky','Zavitinsk','Zavodoukovsk','Zavolzhsk','Trans-Volga','Trans-Volga','Zadonsk','Zainsk','Zakamensk','Zaozyorny','Zaozersk','Western','Dvina','Zapolyarny','Zaraysk','Zarechny','Zarechny','Zarinsk','Zvenigovo','Zvenigorod','Zverevo','Zelenogorsk','Zelenogradsk','Zelenodolsk','Zelenokumsk','Zernograd','Zeya','Winter','Zlatoust','Sinister','Zmeinogorsk','Znamensk','Zubtsov','Zuevka','Ivangorod','Ivanovo','Ivanteevka','Ivdel','Igarka','Izhevsk','Izberbash','Abundant','Ilansky','Inza','Insar','Inta','Ipatovo','Irbit','Irkutsk','Isilkul','Iskitim','Istra','Ishim','Ishimbay','Yoshkar-Ola','Kadnikov','Kazan','Kalach','Kalachinsk','Kalach-on-Don','Kaliningrad','Kalininsk','Kaltan','Kaluga','Kalyazin','Kambarka','Kamenka','Kamennogorsk','Kamensk-Uralsky','Kamensk-Shakhtinsky','Stone-on-Obi','Kameshkovo','Kamyzyak','Kamyshin','Kamyshlov','Kanash','Kandalaksha','Kansk','Karabanovo','Karabash','Karabulak','Karasuk','Karachaevsk','Karachev','Kargat','Kargopol','Karpinsk','Kartaly','Kasimov','Kasli','Kaspiysk','Katav-Ivanovsk','Kataysk','Kachkanar','Kashin','Kashira','Cedar','Kemerovo','Kem','Kizel','Kizilyurt','Kizlyar','Kimovsk','Kimry','Kingisepp','Kinel','Kineshma','Kireevsk','Kirensk','Kirzhach','Kirillov','Kirishi','Kirov','Kirov','Kirovgrad','Kirovo-Chepetsk','Kirovsk','Kirovsk','Kearse','Kirsanov','Kiselevsk','Kislovodsk','Klimovsk','Wedge','Klintsy','Knyaginino','Knyaginino','Kovdor','Kovrov','Kovylkino','Kogalym','Kodinsk','Kozelsk','Kozlovka','Kozmodemyansk','Cola','Kologriv','Kolomna','Kolpashevo','Kolchugino','Kommunar','Komsomolsk','Komsomolsk-on-Amur','Konakovo','Kondopoga','Kondrovo','Konstantinovsk','Kopeysk','Korablino','Korenovsk','Korkino','Korolev','Short','Korsakov','Koryazhma','Kosterevo','Kostomuksha','Kostroma','Kotelnikovo','Kotelnich','Kotlas','Kotovo','Kotovsk','Kokhma','Krasavino','Krasnoarmeysk','Krasnoarmeysk','Krasnovishersk','Krasnogorsk','Krasnodar','Krasnozavodsk','Krasnoznamensk','Krasnoznamensk','Krasnokamensk','Krasnokamsk','Krasnoslobodsk','Krasnoslobodsk','Krasnoturinsk','Krasnouralsk','Krasnoufimsk','Krasnoyarsk','Red','Kut','Red','Sulin','Red','Hill','Kremlenki','Kropotkin','Krymsk','Kstovo','Kstovo','Kuvandyk','Kuvshinovo','Kudymkar','Kuznetsk','Kuibyshev','Kulebaki','Kulebaki','Kumertau','Kungur','Kupino','Mound','Kurganinsk','Kurilsk','Kurlovo','Kurovskoe','Kursk','Kurtamysh','Kurchatov','Kusa','Kushva','Kyzyl','Kyshtym','Kyakhta','Labinsk','Labytnangi','Lagan','Ladushkin','Lakinsk','Langepas','Lahdenpohja','Lebedyan','Leninogorsk','Leninsk','Leninsk-Kuznetsky','Lensk','Lermontov','Forest','Lesozavodsk','Lesosibirsk','Livny','Likino-Dulyovo','Lipetsk','Sticky','Liski','Likhoslavl','Lobnya','Lodeinoe','Pole','Losino-Petrovsky','Meadows','Lukoyanov','Lukoyanov','Lukhovitsy','Lyskovo','Lyskovo','Lysva','Lytkarino','Lgov','Lyuban','Lyubertsy','Love','Lyudinovo','Lyantor','Magadan','Magas','Magnitogorsk','Maykop','May','Makarov','Makariev','Makushino','Malaya','Vishera','Malgobek','Malmyzh','Maloarkhangelsk','Maloyaroslavets','Mamadysh','Mamonovo','Manturovo','Mariinsk','Mariinsky','Posad','Marx','Makhachkala','Mglin','Megion','Medvezhyegorsk','Mednogorsk','Medyn','Mizhhirya','Mezhdurechensk','Mezen','Melenki','Meleuz','Mendeleevsk','Menzelinsk','Meshchovsk','Miass','Mikun','Millerovo','Mineral','water','Minusinsk','Minyar','Peaceful','Peaceful','Mikhailov','Mikhailovka','Mikhailovsk','Mikhailovsk','Michurinsk','Mogocha','Mozhaisk','Mozhga','Mozdok','Monchegorsk','Morozovsk','Morshansk','Mosalsk','Moscow','Muravlenko','Murashi','Murmansk','Murom','Mtsensk','Myski','Mytischi','Myshkin','Naberezhnye','Chelny','Navashino','Navashino','Navoloki','Nadym','Nazarovo','Nazran','Nazyvaevsk','Nalchik','Narimanov','Naro-Fominsk','Nartkala','Naryan-Mar','Find','Nevel','Nevelsk','Nevinnomyssk','Nevyansk','Nelidovo','Neman','Nerekhta','Nerchinsk','Neryungri','Nesterov','Neftegorsk','Neftekamsk','Neftekumsk','Nefteyugansk','Not','me','Nizhnevartovsk','Nizhnekamsk','Nizhneudinsk','Lower','Sergi','Nizhny','Lomov','Nizhny','Novgorod','Nizhny','Novgorod','Nizhny','Tagil','Nizhnyaya','Salda','Lower','Tura','Nikolaevsk','Nikolaevsk-on-Amur','Nikolsk','Nikolsk','Nikolskoe','New','Ladoga','New','Lyalya','Novoaleksandrovsk','Novoaltaisk','Novoanninsky','Novovoronezh','Novodvinsk','Novozybkov','Novokubansk','Novokuznetsk','Novokuibyshevsk','Novomichurinsk','Novomoskovsk','Novopavlovsk','Novorzhev','Novorossiysk','Novosibirsk','Novosil','Novosokolniki','Novotroitsk','Novouzensk','Novoulyanovsk','Novouralsk','Novokhopersk','Novocheboksarsk','Novocherkassk','Novoshakhtinsk','Novy','Oskol','New','Urengoy','Noginsk','Nolinsk','Norilsk','Noyabrsk','Nurlat','Nytva','Nyurba','Nyagan','Nyazepetrovsk','Nyandoma','Obluchie','Obninsk','Oboyan','Ob','Odintsovo','Necklace','Ozersk','Ozersk','Lakes','Oktyabrsk','October','Okulovka','Olekminsk','Olenegorsk','Olonets','Omsk','Omutninsk','Onega','Opochka','Eagle','Orenburg','Orekhovo-Zuevo','Orlov','Orsk','Wasp','Osinniki','Ostashkov','Island','Ostrovnoy','Ostrogozhsk','Gratifying','Gratifying','Okha','Okhansk','Ocher','Pavlovo','Pavlovo','Pavlovsk','Pavlovsky','Posad','Pallasovka','Partizansk','Pevek','Penza','Pervomaisk','Pervomaisk','Pervouralsk','Perevoz','Perevoz','Peresvet','Pereslavl-Zalessky','Permian','Pestovo','Petrov','Val','Petrovsk','Petrovsk-Zabaikalsky','Petrozavodsk','Petropavlovsk-Kamchatsky','Petukhovo','Cockerels','Pechora','Pechory','Pikalevo','Pioneer','Pitkyaranta','Plavsk','Layer','Plyos','Povorino','Podolsk','Podporozhye','Pokachi','Cover','Pokrovsk','Polevskoy','Polessk','Polysaevo','Polar','dawns','Polar','Poronaysk','Porkhov','Pokhvistnevo','Pochep','Pochinok','Poshekhonye','Pravdinsk','Privolzhsk','Primorsk','Primorsko-Akhtarsk','Priozersk','Prokopyevsk','Proletarsk','Protvino','Chill','Pskov','Pugachev','Pudozh','Wasteland','Puchezh','Pushkino','Pushchino','Pytalovo','Pyt-Yah','Pyatigorsk','Rainbow','Rainbow','Raichikhinsk','Ramenskoe','Rasskazovo','Revda','Dir','Reutov','Rzhev','Springs','Roslavl','Rossosh','Rostov','the','Great','Rostov-on-Don','Roshal','Rtishchevo','Rubtsovsk','Rudnya','Ruza','Ruzaevka','Rybinsk','Rybnoe','Rylsk','Ryazhsk','Ryazan','Salavat','Salair','Salekhard','Salsk','Samara','St.','Petersburg','Saransk','Sarapul','Saratov','Sarov','Sarov','Sasovo','Satka','Safonovo','Sayanogorsk','Sayansk','Svetlogorsk','Svetlograd','Light','coloured','Svetogorsk','Svirsk','Free','Sebezh','Severobaikalsk','Severodvinsk','Severo-Kurilsk','Severomorsk','Severouralsk','Seversk','Sevsk','Segezha','Seltso','Semyonov','Semyonov','Semikarakorsk','Semiluki','Sengiley','Serafimovich','Sergach','Sergach','Sergiev','Posad','Serdobsk','Serov','Serpukhov','Sertolovo','Sibay','Sim','Skovorodino','Skopin','Slavgorod','Slavsk','Slavyansk-on-Kuban','Slates','Slobodskoy','Slyudyanka','Smolensk','Snezhinsk','Snezhnogorsk','Sobinka','Sovetsk','Sovetsk','Sovetsk','Sovetskaya','Gavan','Soviet','Falcon','Soligalich','Solikamsk','Solnechnogorsk','Solvychegodsk','Sol-Iletsk','Soltsy','Sorochinsk','Sorsk','Sortavala','Sosensky','Sosnovka','Sosnovoborsk','Pinery','Sosnogorsk','Sochi','Spas-Demensk','Spas-Klepiki','Spassk','Spassk-Dalny','Spassk-Ryazansky','Srednekolymsk','Sredneuralsk','Sretensk','Stavropol','Staraya','Russa','Old','lady','Starodub','Stary','Oskol','Sterlitamak','Strezhevoy','Builder','Strunino','Stupino','Suvorov','Suja','Suddenly','Suzdal','Suojärvi','Surazh','Surgut','Surovikino','Sursk','Susuman','Sukhinichi','Sukhoi','Log','Gangway','Sizran','Syktyvkar','Sysert','Sychevka','Syasstroy','Tavda','Taganrog','Taiga','Taishet','Taldom','Talitsa','Tambov','Container','Tarusa','Tatarsk','Tashtagol','Tver','Teberda','Teikovo','Temnikov','Temryuk','Terek','Tetyushi','Timashevsk','Tikhvin','Tikhoretsk','Tobolsk','Toguchin','Tolyatti','Tomari','Tommot','Tomsk','Furnaces','Torzhok','Toropets','Tosno','Totma','Trekhgorny','Troitsk','Troitsk','Trubchevsk','Tuapse','Tuymazy','Tula','Tulun','Turan','Turinsk','Tutaev','Tynda','Tyrnyauz','Tyukalinsk','Tyumen','Uvarovo','Uglegorsk','Uglich','Successful','Udomlya','Uzhur','Nodal','Ulan-Ude','Ulyanovsk','Unecha','Uray','Level','Level','Urzhum','Urus-Martan','Uryupinsk','Usinsk','Usman','Usolye','Usolye-Sibirskoe','Ussuriysk','Ust-Dzheguta','Ust-Ilimsk','Ust-Katav','Ust-Kut','Ust-Labinsk','Ustyuzhna','Ufa','Ukhta','Uchaly','Uyar','Fatezh','Fokino','Fokino','Frolovo','Fryazino','Furmanov','Khabarovsk','Khadyzhensk','Khanty-Mansiysk','Kharabali','Kharovsk','Khasavyurt','Khvalynsk','Khilok','Khimki','Hill','Kholmsk','Khotkovo','Tsivilsk','Tsimlyansk','Chadan','Tchaikovsky','Chapaevsk','Chaplygin','Chebarkul','Cheboksary','Chegem','Chekalin','Chelyabinsk','Cherdyn','Cheremkhovo','Cherepanovo','Cherepovets','Cherkessk','Chermoz','Chernogolovka','Chernogorsk','Nigella','Chernyakhovsk','Chekhov','Chistopol','Chita','Chkalovsk','Chkalovsk','Chudovo','Chulym','Chusovoy','Chukhloma','Shagonar','Shadrinsk','Shawls','Sharypovo','Sharya','Shatura','Shakhtersk','Mines','Shakhunya','Shakhunya','Shatsk','Shebekino','Shelekhov','Shenkursk','Shilka','Shimanovsk','Shihan','Shlisselb','Sumerlya','Hype','Shuya','Shchekino','Shchelkovo','Shcherbinka','Shchigry','Shchuchye','Electrogorsk','Elektrostal','Electrocoals','Elista','Engels','Ertil','Anniversary','Yugorsk','Yuzha','Yuzhno-Sakhalinsk','Yuzhno-Sukhokumsk','Yuzhnouralsk','Yurga','Yuryevets','Yuriev-Polsky','Yuryuzan','Yukhnov','Yadrin','Yakutsk','Yalutorovsk','Yanaul','Yaransk','Yarovoe','Yaroslavl','Yartsevo','Yasnogorsk','Clear','Yakhroma']

for city in citys:
	for lin in l:
		links.append(f'https://prodoctorov.ru/{city.lower()}{lin}')
		#print(f'https://prodoctorov.ru/{city.lower()}{lin}')



for o in l:
	for i in range(1,30):
		links.append(f'{o}?page={i}')


def getDoctors(url):
	try:
		r = requests.get(url,headers=headers)
		PageToHtmlBs = bs(r.content,"html.parser")
		FindMainBlock = PageToHtmlBs.find('div',class_='appointments_page')
		FindAllBlocks = FindMainBlock.find_all('div',class_='b-doctor-card')
		for BlockD in FindAllBlocks:
			TopBlock = BlockD.find('div',class_='b-doctor-card__top')
			DoctorName = (((TopBlock.find('div',class_='b-doctor-card__name')).find('span',class_='b-doctor-card__name-surname')).text).strip()
			LinkDoctor = 'https://prodoctorov.ru' + ((TopBlock.find('div',class_='b-doctor-card__name')).find('a'))['href']
			CatigoriesDoctor = ((((TopBlock.find('div',class_='b-doctor-card__spec')).text).strip()).replace('  ','',1000)).replace('\n','',10000)
			DoctorExp = (((((TopBlock.find('div',class_='b-doctor-card__experience')).find('div',class_='b-doctor-card__experience-years')).text)).strip()).replace('Стаж ','')
			GetDoctor(DoctorName,LinkDoctor,CatigoriesDoctor,DoctorExp)
	except Exception as e:
		pass

def GetDoctor(DoctorName,LinkDoctor,CatigoriesDoctor,DoctorExp):
	try:
		r = requests.get(LinkDoctor,headers=headers)
		PageToHtmlBs = bs(r.content,"html.parser")
		BlockD = PageToHtmlBs.find('div',class_='b-doctor-intro b-doctor-intro_doctor')
		Photo = 'https://prodoctorov.ru'+((BlockD.find(class_='b-doctor-intro__left-side')).find('img'))['src']
		r = requests.get(Photo)
		fd =  open(f'photos/{DoctorName}.jpg', 'wb')
		fd.write(r.content)
		RightBlockD = BlockD.find('div',class_='b-doctor-intro__right-side')
		DoctorCity = (((BlockD.find('div',class_='b-doctor-intro__right-side')).find(class_='b-doctor-intro__title-first-line')).find(class_='b-doctor-intro__title-sub')).text
		#print(DoctorCity)
		DoctorClass = ((RightBlockD.find(class_='b-doctor-intro__degree')).text).replace('\n',' ',1000)
		DoctorDescrip = (((RightBlockD.find('p',class_='b-doctor-intro__summary')).text).strip()).replace('\n',' ',1000)
		BlockPr = (PageToHtmlBs.find('div',class_='b-doctor-contacts__wp-block')).find(class_='b-doctor-contacts__wp-info')
		DoctorMed = 'https://prodoctorov.ru' + ((BlockPr.find('div',class_='b-doctor-contacts__lpu')).find('a',class_='b-doctor-contacts__lpu-name ui-text ui-text_subtitle'))['href']
		MedAdress = (((BlockPr.find('div',class_='b-doctor-contacts__lpu-address ui-text ui-text_subtitle')).text).strip()).replace('\n',' ',1000)
		DoctorPrices = (BlockPr.find('div',class_='b-doctor-contacts__prices')).find_all('div',class_='b-doctor-contacts__price-wrapper')


		BlockAboutMan = (PageToHtmlBs.find('div',class_='b-doctor-details')).find('div',class_='b-doctor-details__main')
		try:
			Po = []
			Profile = ((BlockAboutMan.find("div", id='manipulations')).find('ul')).find_all('li')
			for p in Profile:
				Po.append((p.text).strip())
			DoctorProfile = ', '.join(Po)
		except:
			DoctorProfile = ' '
		try:
			Poj = []
			Job = ((BlockAboutMan.find("div", id='job')).find('ul')).find_all('li')
			for p in Job:
				Poj.append((p.text).strip())
			DoctorJOB = ', '.join(Poj)
		except:
			DoctorJOB = ' '

		try:
			Poje = []
			Joba = ((BlockAboutMan.find("div", id='educations')).find('ul')).find_all('li')
			for p in Joba:
				Poje.append((((p.text).replace('  ','',1000)).replace('\n',' ',1000)).strip())
			DoctorEduc = ', '.join(((Poje)))
		except:
			DoctorEduc = ' '
		try:
			Pojed = []
			Jobad = ((BlockAboutMan.find("div", id='associations')).find('ul')).find_all('li')
			for p in Jobad:
				Pojed.append((((p.text).replace('  ','',1000)).replace('\n',' ',1000)).strip())
			DoctorAssoc = ', '.join(((Pojed)))
		except:
			DoctorAssoc = ' '
		print(DoctorAssoc)


		t = []
		for textt in DoctorPrices:
			t.append((((textt.text).strip()).replace('  ','',10000)).replace('\n',' ',1000))
		DoctorPrices = (' '.join(t)).replace('\n',' ',1000)
		try:
			DoctorNumber = ((BlockPr.find('div',class_='b-doctor-contacts__lpu-phone')).text).replace('\n',' ',1000)	
		except Exception as e:
			DoctorNumber = ' '
		#DoctorNumber = ((BlockPr.find('div',class_='b-doctor-contacts__lpu-phone')).text).replace('\n',' ',1000)
		OtziviAboutD = ((((PageToHtmlBs.find('div',class_='b-doctor-details')).find('div',class_='b-doctor-details__main')).find('div',class_='b-doctor-rates__body')).find('div')).find_all('div',class_='b-doctor-rates__item')
		Otz = []
		
		g = []
		for Otziv in OtziviAboutD:
			try:
				a = (((Otziv.find('div',class_='b-doctor-rates__aside')).find('div',class_='b-doctor-rates__rate-wrapper')).find('div',class_='b-doctor-rates__rate')).find(class_='b-doctor-rates__rate-num').text
				OtzText = a + ' ' + (((((Otziv.find(class_='b-doctor-rates__body')).find(class_='b-doctor-rates__comments')).find(class_='b-doctor-rates__comment-wrapper')).find(class_='b-doctor-rates__comment')).text).replace('\n',' ',10000)
				g.append(OtzText)
				#print(OtzText)
				#f.write(f';{OtzText}')
			except:
				pass
		
		'''
		recs = []
		for rec in :
			recs.append(rec)
		'''
		ew = []
		try:
			bo = (((((PageToHtmlBs.find('div',class_='b-doctor-details')).find('div',class_='b-doctor-details__main')).find('div',id='doctor_recommendations'))).find('ul')).find_all('li')
			for p in bo:
				ew.append(((((p.find('div',class_='b-review-card')).find(class_='b-review-card__main').find(class_='b-review-card__content')).text).strip()).replace('\n',' ',1000))
			DoctorRec ='-----------+------------'.join(ew)
		except Exception as e:
			DoctorRec = ''
		
		#print(DoctorRec)

		f = open(file,'a',encoding='utf-8',newline='\n')
		f.write(f"{DoctorName};{str(LinkDoctor)};{CatigoriesDoctor};{DoctorCity};{DoctorClass};{str(DoctorDescrip).strip()};{DoctorProfile};{DoctorJOB};{DoctorEduc};{DoctorAssoc};{'-----------+------------'.join(g)};{DoctorRec};\n")
		print(DoctorName)
		sleep(0.5)
	except Exception as e:
		pass

f = open(file,'w',encoding='utf-8',newline='\n')
f.write('Name;Link;Catigories;City;Level;AboutMe;Catigories;DoctorProfile;ExpJob;Education;Associations;CommentsByUsers;DocRecommendations\n')

def getAllPages(city):
	try:
		r = requests.get(f'https://prodoctorov.ru/{city}/vrach/',headers=headers)
		b = bs(r.content,'html.parser')
		g = (((b.find('div',class_='p-doctors-list-page__tabs-container b-toggle-block')).find('div',class_='b-toggle-block__toggle')).find('ul',class_='p-doctors-list-page__tab p-doctors-list-page__tab_is_active')).find_all('li')
		for kl in g:
			pages = (((kl.find('span')).text).replace('\\xa0','',10)).replace(' ','',10)
			#print(pages)
			#print
			
			link = "https://prodoctorov.ru" + (kl.find("a"))['href']
			for i in range(1,int(pages) // 20 + 1):
				links.append(f'{link}?page={i}')
		print(f'Added {city}')

	except Exception as e:
		pass

for city in citys:
	getAllPages(city.lower())

print(len(links))
for i in links:
	getDoctors(i)