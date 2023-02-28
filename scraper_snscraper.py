#pip install snscrape
import snscrape.modules.twitter as snstwitter
import os
import pandas as pd
from datetime import datetime

all_terms = ['#LoudlyNigerian', '#nigeria', '#GODEBATE', '#EndSARS', '#PVC', '#VoteForBetterGovernment', '#almustafa', '#TheOneCampaign', '#ThinkHamza', '#NigeriaDecides2023', '#Nigeriaisnotforsale', '#RMK2023', '#2023Election', '#SoworeMagashi2023', '#noelectioninbiafrakandcome2023', '#obidientmovement', '#WeGoDoAm', '#MakeWeGoVote', '#CollectYourPVC', '#VoteAPC', '#PresidentialVoiceOfNigerians', '#PRP', '#biafraland', '#concernednigerians', "#rufa'ihanga", '#tinubu', '#tinubuinbayelsa', '#voteforatiku', '#voteLp', '#biafraexit', '#PO2023', '#LabourParty', '#PVCChallenge', '#NaijaDecides', '#NewNigeria', '#RecoverKatsinaWithAtiku', '#2023electionswemustgetsense', '#SoworeIsTheAnswer', '#breketefamily', '#PeterObi4President2023', '#ObiDatti', '#IPOB', '#Obi', '#soworeforpresident', '#AACParty', '#TinubuShettima2023', '#ProfPeterUmeadi2023', '#RMK2023', '#NNPP', '#agba', '#PeterObiForPresident2023', '#TableShaker', '#Renewedhope23', '#Obidatti2023', '#SoworeMagashi2023', '#AACTheAlternative', '#majorhamzaAlmustapha', '#NigeriaMustGrow', '#Batspace', '#RecoverImoWithPDP', '#RecoverNigeria', '#RecoveryTeam', '#CTVTownhallWithAtiku', '#AriseTVTownHall', '#AtikuMeetsCreativeIndustry', '#hamzaiscoming', '#Hamzafiles', '#BokoHaram', '#NGTheCandidates', '#ZikokoCitizen', '#BATKSM2023', '#TinubuInChattamHouse', '#BATtified', '#UmeadiPeter', '#KOrrect', '#forourpeople', '#KolaAbiola2023', '#HopeAgain2023', '#2023elections', '#2023electionwebsite', '#abuja', '#adamugarba', '#atikuiscoming', '#atikuokowa2023', '#atikuorganizingforaction', '#BAT2023', '#BATinNiger', '#BATiscoming2023', '#bayo', '#bichi', '#bolatinubu', '#cuppy', '#kaduna', '#kwankwasiyya', '#kwankwaso', '#kwankwaso2023', '#kwankwasoRM', '#nigeriadecides', '#noelectioninbiafraland', '#obidattilnkogi', '#okowatition', '#ourmandate', '#PDP2023', '#pitobi', '#recoveranambrawithatiku', '#recovernigeria', '#renewedhope', '#renewedhope2023', '#saka', '#takebacknaija', '#TakeItBack', '#tinubuinchattamhouse', '#tinubushettima', '#tinubuslagos', '#Vote4WASH', '#VoteWisely', '#votewisely', '#Atikugate', '#AtikuAtNESG', '#TinubuMeetsYouths', '#PeterObiInChathamHouse', '#PeterObiInLondon', '#renoomokri', '#POinChathamHouse', '#BATKSM2023', '@atiku', '@iyorchiayu', '@OfficialDeboO', '@DeleMomodu', '@AWTambuwal', '@IsaAshiruKudan', '@emmaikumeh', '@Hailfinger1', '@SenBalaMohammed', '@jihadwatchRS', '@BiafranTweets', '@MBuhari', '@thecableng', '@channelstv', '@ShehuSani', '@Muazuaa', '@OfficialAPCNg', '@QueenAbeeke', '@officialABAT', '@akandeoj', '@ProfOsinbajo', '@NGRPresident', '@GarShehu', '@femigbaja', '@LalongBako', '@NgLabour', '@KwankwasoRM', '@doyinokupe', '@ProfIsaPantami', '@KashimSM', '@ZShamsuna', '@ClemAgba', '@ChidiOdinkalu', '@SPNigeria', '@FemAdesina', '@AbubakarmusaDK1', '@UtomiPat', '@ubasanius', '@inecnigeria', '@RedCardMng', '@yamusa', '@UbaSaniMedia', '@GreaterKadunaNG', '@abet_caleb', '@vanguardngrnews', '@MobilePunch', '@GuardianNigeria', '@daily_trust', '@femifalana_SAN', '@renoomokri', '@elrufai', '@GovKaduna,', '@DrHadiza', '@GovUmarGanduje', '@KanostateNg', '@GombeStateGovnt', '@Dankakanda', '@GovernorMasari,', '@KatsinaState', '@Zamfara_state', '@SokotoGovtHouse', '@KBStGovt', '@abusbello', '@NigerStateNG', '@SenBalaMohammed', '@YobeStateGovt', '@ProfZulum', '@GovBorno,', '@tarabagovt,', '@GovNasarawa', '@NasarawaGovt', '@GovSamuelOrtom', '@benuestategovt', '@MrUdomEmmanuel', '@RealAARahman,', '@followKWSG', '@seyiamakinde', '@dabiodunMFR', '@AAdeleke_01', '@biodunaoyebanji', '@jidesanwoolu', '@RotimiAkeredolu', '@Hope_Uzodimma1', '@DaveUmahi', '@GovernorIkpeazu', '@CCSoludo', '@OfficialGYBKogi', '@GovernorObaseki', '@GovWike', '@IAOkowa', '@govdouyediri', '@AhmedAdamu', '@LabourMopol', '@AreaFada1', '@_dinomelaye', '@DinoMeIaye', '@fkeyamo', '@MaziNnamdiKanu', '@SenKabiruGaya', '@BarauJibrin', '@NGRSenate', '@TokunboAbiru', '@MallamShekarau', '@babbahmed', '@SenSmartAdeyemi', '@SenBettyApiafi', '@Sen_Dr_Sankara', '@ibrahimMbomai', '@Sen_EBwacha', '@ihadejia', '@AhmedAdamu', '@AreaFada1', '@fkeyamo', '@YeleSowore', '@haruna_magashi', '@aacparty', '@H_Almustapha', '@HamzaChukwuka', '@drecjohnson', '@atiku', '@OfficialPDPNig', '@DumebiKachikwu', '@dattibabaahmed', '@ineclagos', '@inecnews', '@KanostateNg', '@NgLabourSupport', '@NigeriaInec', '@PeterObi', 'Oduduwa', 'Arewa', 'Kwankwasiyya', 'Gandujjiya', 'IPOB', 'Yorufool', 'Pdpigs', 'Hausafoolanis', 'Biafrog', 'Biafrats', 'banza akuya', 'igbos rituals', 'foolanis kidnappers', 'evil Fulani', 'Arne', 'Igbosmaalo', 'Northernszoo', 'Almajiris', 'Boko Haram', 'Abokis', 'Igbozoo', 'Yorubanza', 'Yorubastard', 'Inyamuris', 'Pdpcats', 'Olosho', 'Fulani Muslim', 'Chatham house', 'Tinubu', 'Atiku', 'Peter Obi', 'Kwankwaso', 'Almustapha', 'Hausa', 'Fulani', 'BAT', 'Igbos', 'Okowa', 'Shettima', 'MNK', 'Mumu', 'PDP AND APC', 'Sokoto', "Deborah's killers", 'Wike', 'Shege', 'Almajiri', 'Ode', 'IGBO BILLIONAIRES', 'amo*ba', 'Asiwaju', 'NNPP', 'Red Caps', 'Amana', 'Decampies', 'PO-ssible', 'Beware of PDP', 'Northern Nigeria', 'INEC', 'PVC', 'Zamfara', 'PDAPC', 'Tambuwal', 'Election candidates: Ndi ndoro-ndoro ochichi', 'Election: ntuli aka', 'Voting: ịtụ vootu', 'Ofu Onye, Ofu vote (One person, one Vote)', 'Igbatago PVC gi (Have you gotten your PVC)', 'PDP uses: Tinye Aka ebe esere Umbrella', 'APC: Tinye Aka ebe esere Aziza', 'APGA: Tinye Aka ebe esere Okuko', 'APGA', 'Ofor ka anyi ji aga...', 'Jeenu nwere PVC unu ...', 'Igwe bu Ike', 'Shared by INEC:', 'Arne', 'Arna', 'Aruna', 'Ar’na', 'Kirdi (Kanuri)', 'Rochas Okorocha', 'PDPigs', 'Pitobi', 'Obidense', 'Karuwa', 'Ana ta kashe mana yan’uwa a kudu', 'mutashi mu rama, Tsutsi/Tutsi, Ewu', 'Okorohausa', 'Inyamiri', 'Dodon Doya', 'Myamiri', 'Yanmiri', 'Agwoi', 'Biafran', 'Agitators', 'Biafraud', 'Biafrauds', 'OBIdiot', 'IPOBdorian', 'Wawa', 'Ashawo', 'Product of baby factory', 'Karuwai Wanda ake buga su a kamfani', 'Kafir', 'Kafirai', 'Takafir', 'kyankyaso', 'Aboki', 'Cow', 'Malu', 'Mallam', 'Mallams', 'Hausa/Hausas', 'Almajiris', 'Islamization of Nigeria', 'Our Mumu Don Do', 'Northerners', 'Animal', 'Zombies', 'Herdsmen', 'Fulani President', 'Agafu', 'Buhari herdsmen', 'Fulani herdsman', 'Fulani kidnappers', 'Fulani criminals', 'killer herders', 'Born throwaway', 'Emi lokan', 'Àfonja', 'Wawa', 'Ashawo', 'Agafu', 'Karuwai Wanda ake buga su a kamfani', 'kyankyaso', 'Egunje', 'Gbewiri', 'INEC is a fraud', 'Mahmood is corrupt', 'INEC has been compromised', 'Arson', 'Burn down', 'INEC is a fraud', 'Mahmood is corrupt', 'Thiefnubu', 'INEC is APC', 'AthiefIKU', 'Atifku', 'INEC Cannot be trusted', 'Efulefu', 'Ndi ugwu', 'Onye apari', 'Yar iska/Shegiya', 'Dan iska', 'ubanka uwarka', 'Shege', 'Bayaraben banza', 'Malam', 'Na dem', 'Lie-Mohammaed', 'Ghandollar', 'Kangaroo-election']

all_terms = list(set(all_terms))


all_tweets = []

isExist = os.path.exists("csvs/")
if not isExist:
    os.makedirs("csvs/")


def scratch_for_keyword(kw,):
    global all_tweets

    ### depending on the time zone add an extra day to both since and until

    query = "("+kw+") until:2023-02-01 since:2022-12-31 -filter:retweets"
    print("starting for >>>>>>" +  kw)
    for tweet in snstwitter.TwitterSearchScraper(query).get_items():
        ## to check what each tweet has
        # print(vars(tweet))
        # print(tweet.retweetedTweet)

        all_tweets.append([tweet.date, tweet.user.id,tweet.id,tweet.lang,tweet.rawContent,tweet.retweetCount])
    ## to back up the data save it every 20000 tweets
    if len(all_tweets) > 20000:
        df = pd.DataFrame(all_tweets, columns = ['created_at', 'author', 'id', 'lang', 'tweet', 'retweet'])
        df.to_csv("csvs/till_"+kw[1:]+".csv")
        all_tweets = []
    print("finished for >>>>>>" +  kw)

for keyword in all_terms:
    scratch_for_keyword(keyword)

    

df = pd.DataFrame(all_tweets, columns = ['created_at', 'author', 'id', 'lang', 'tweet', 'retweet'])


### to create a folder called csvs on the same level as this file

df.to_csv("csvs/till_lastt"+all_terms[-1]+".csv")

onlyfiles = [f for f in os.listdir("csvs")]
print(onlyfiles)

columns = ["data.created_at","data.author_id","data.id","data.lang","data.text","data.retweet_number"]
new_df = []
print(columns)
for i in range(len(onlyfiles)):
    onlyfiles[i] = "csvs/" + onlyfiles[i]
    df = pd.read_csv(onlyfiles[i],index_col=0)
    df.author = df.author.apply(str)
    df.id = df.id.apply(str)

    print(df.id)
    print(df.author)
    print("____________________________")
    new_df.extend(df.values.tolist())

df = pd.DataFrame(new_df,columns=columns).reindex()

df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

df.to_csv("scrapedat_" + str(datetime.now()) + ".csv")
        
for i in range(len(onlyfiles)):
    os.remove("csvs/"+onlyfiles[i])
os.rmdir("csvs/")