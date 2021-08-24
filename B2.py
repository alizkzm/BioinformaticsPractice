import numpy as np
import Matrix as mt

def lengthOfLcs(str1, str2):
    lookup = mt.Matrix("BLOSUM62.txt")
    m = len(str1)
    n = len(str2)
    matrix = [[0] * (n + 1) for i in range(m + 1)]
    matrix[0] = -5*np.arange(0,n+1)
    for i in range(m+1):
        matrix[i][0] = -5*i
    for i in range(m + 1):
        for j in range(n + 1):
            if i!=0 and j!=0:
                matrix[i][j] = max(matrix[i-1][j]-5,#int(mt.Matrix("BLOSUM62.txt").lookup_score("-",str2[j-1]))
                                       matrix[i][j-1]-5,#int(mt.Matrix("BLOSUM62.txt").lookup_score(str1[i-1],"-"))
                                       matrix[i-1][j-1]+int(lookup.lookup_score(str1[i-1],str2[j-1])))
    return matrix

def convert(s):
    # initialization of string to ""
    s = s[::-1]
    new = ""

    # traverse in the string
    for x in s:
        new += x

        # return string
    return new

def printLcs(str1,str2):
    lookup = mt.Matrix("BLOSUM62.txt")
    string1 = [""]
    string2 = [""]
    matrix = lengthOfLcs(str1,str2)
    matrix = np.array(matrix)
    m = matrix.shape[0]
    n = matrix.shape[1]
    i = m-1
    j = n-1
    score = matrix[i][j]
    while(i+j!=0):
        #print(int(lookup.lookup_score(str1[i-1],str2[j-1])),[str1[i-1],str2[j-1]])
        a = matrix[i][j]-matrix[i][j-1]
        b = matrix[i][j]-matrix[i-1][j]
        c = matrix[i][j]-matrix[i-1][j-1]
        d = int(lookup.lookup_score(str1[i-1],str2[j-1]))
        e = -5
        if (d==c):
            string1.append(str1[i - 1])
            string2.append(str2[j - 1])
            i -= 1
            j -= 1
            continue
        if (b==e):
            string1.append(str1[i - 1])
            string2.append("-")
            i -= 1
            continue
        if (a==e):
            string2.append(str2[j - 1])
            string1.append("-")
            j -= 1
            continue
    print(convert(string1))
    print(convert(string2))

    return [score,convert(string1),convert(string2)]

X = "GQRKIMRAWKLPVTNNLQGETPCTYDEPAWMLLVIHQSWKGAEGKPNYPPVGSYCDTHDYEWFARSSILYENLDGNGSKCMKNRWTQFFHDQSVIGETIYSIVFWNAGYTKDNRHCQEEVANSDCKSTIVISGQWHYPYRWMVPSMSFVMYRTTMCHHNDWDQYLYQECTSPPGRGFTEDVTWDDWGQLDCWHGRCTEIYSITIAVVVKKFEDNGRMKPGWCDTWLCCNANMNMANFLRHGWQETIEKGTFEKCWILSTQYNLEVGDMCDEPMRKVWYFQSGVWGGKTNFHPLWYSFYSCTRFFQTILGICSDRELFGPNYDVITEDEIMNGQKMDLTIDGKDRYPQFDGFHFQTMGECWRHAANIMFGIDRVHIFSGHRCSVENSIFELFQEQEWKWYHFEIFTFTAWFCRCQLCVENQASANIYCVFHSYYVSRQFWLMQFPGEWAMHHWAIGHENQQELPWPWVWEVRMGVMLYIGHLHTGQQIKTHMAPKCEKSATRKNKYSRHSNECPPPRKHFNAYSRDLAHPAPHAGSWNQHENAGTVVPYHFQFPHEPTGTDCCFYVDECVAMCWAYWCAKCWGPFKDCIPCQTIEKDWGRSEGMSALGDEARAHKYPYPMLLDLHNMVGQQWNYQDMKWYDRTDREIKCTYLVRGSWSFWSTFSGEKCCSMFVSRDCWIADPHVECNTKLCCMGTVYDWAGPCKKPNDPLIDRKHWMFFYDSPLHIHKSAAQWGTWPADQHSCGVSVVHNCSDWPYAHSPGGMHEGSFCQNHFMQMQMHAIDYTPAEIRSFRDQTWDAPVCTNKCIYPSPWFHRMHICSVNPMNVIHGDPIGSTVISEIRFTELMVQRMYYTVEDYHANVICRDVLGNILVVAFTMYYSYVQMDWAYKHESQSEVWLKPNYVWCKERLDVIFDWIHNIQYQYAQPMRMWSEMVHPDTGYPWQRFLTGGGSIYYVTFRVFFRTWQMEHGHCICLRSHHYGRNSGLAAPNKTMERFLGEDGMKYCDAIFHHYTSCMGPFYVRPARSKSFDRSLASLIDVHTKMANGDKCFTSVSHSVVMYMLNCIIHAEQSFPLVEMSCFFRMRVEECISDLTSPCYVDSKSYEASRCIAMKHFDYLTHVWDGQYHEECKTMPHQVDLNNEPRTVYWLLEDPLHVKYKSGDQLTWGQQKPAASVAWTSYKNGSMLMIPAHAHNYPNFYGTDDAGDMMEIQHWRAFNPTADQNWHCMNQSQAFMATMRGDDKHPLYSANEKHARKIATYYFAGEAPMYWEFWNEADPGNTKMTVFCCDNRMDKFYANGIIYAWQITLCTHWNMGPQHDFQKGTDFIDCQTFMLSRLPCISLDIMQPFHPRAFEGWSPIYLDVLMGLVAPIDADWRMNGHSQFRYRPWPVLFREFFHNMFNISFPHDQNKKEYWGEMTLGMFVCHDIRPTKGFSMMARNADDKWCQTIQHLCLPFKCSMKCISFNFHMEGLIMHGTGICMLSRTLANPKDVFITEKSHYHMTCKIPCYEQWQFEWLCKMGLDTLNVLCMKHERIYVAYYEPDLDCKLDYWFSSIDPLHRQEWSASMPFYEDPPECIADFGKNEDKVCQKKCHCMCMWHKCAQAGGSHYPPMMWFTASGPKAVRITHDPKKGWVTNICQWAKVSAMPIVWALDSAVPCEHFKAQMSHKDELVSPYWSYDCRDMPYARDCCCMYYSSCKCPFLSHIPYNDPCKRTNKHRVQCYCRCLDTFATISDEPASMCWCWDDFSCKRYHRQRWLPGGGAILINCTWMENFWTPWVTFFDTPVKWKMALAMDKTSFYPLCQVRHSRLRYVGVGGHRQQMTSPDVYLMHCPLEIAFSLDVHPSDHPISNDWDWFESLRQSEPGRNCEQLSMAHNDLNHNTPVDVAGLVKMKRWMWEEKSCLYFRTFGNTMEPMHIQHLCIASDNYTCWAHAEHNYVCQISCFYGWDSRKIRGIENIIHLNFIMTGHKARICTTFMSHTKSEPWHCSAAPQNYSLPHGWDVGRIDVCKLTLYYVLWMMVGMRLTGWYKSANVRVYKRPCVWLCYSMMKVKTDMILQGYILNVTSRPYGWADEMRNIFCRYYVNKVHKSGSRWKAWCMNRVMVNNGMYCRVMYHVHGNILPIAPNRHSPMPMYRHITCQINRATTVVKHVHPLVGAFMCMSEWNWYMTPESCGHSPLDNGAVVTLDQMDKEYCLYPMSFTKKTEGEGTWYDNGYDLTMGQRMQKQMHTIHNNRVCPCQVPMVIPTVYMSNMRLEWIMYDREAYCCRRQPPKYKVNRDHINHTDKLPNRPLCAFVWYRQIFAYDLQCPSPELDHRRESNPGRGYSFIFSSSPRSNYTKYSCQCILVQDQNSFCQQGCSEMCFMQQQMKMGSSYIHIGWAIHYYAFWQTPVSSHCKYLSEIIRMHFNEFQNEWAWETTSCHGDLLWETGLFCHYQYHWKRMRQENRTGTLVNFYVQPFMPRTAMLAVWTYLTVPWWGYESKIPERCIVVCYPHREYLYLMQYNYLNWTHYFFDWKQAMMRAKFYVPWTQKIDKAVEKVRVWYTPYNYWWQDLDHDSGVWPEQPCYPKANGADFCFAHQWHTTCLEPHPYHIFFRHGCLKFHQKCLWVCKFNDHGHQCLLQMLCYNSTNDHDDSYCIFHVDASGHNHPCCMFWCAPFCLDVTRFDAQFIHQTIENFYFRGNEDVKAWEEHMHWNVSDDKCTMLRIINFFIHHTPKKWGTTCCWFYEYPDPQMYGDMGEDHPDREWWLMKDTPAWDIVHEPLKSVKSPIKWCDMFSAPFHDPNREYDCNGAVPIGNLDYHNSWWQCWGHYLHYLILMIHRQLKLKNCWTKKADFHKFPCARPWNQWFVEQMSRVQCTTPDMSTYKPTELRVYRMSECCCAYQATNARMFDAIWYSWHTSPASTGMVAGHGCVHKIYRHYSPATSIRLVNPDVSMPDSGNEASNFIYTLASTWYSHVHDATRCTFGCFASGYARFRVETQIRQWSQMWTYMEMDDAINMWGDDTHGQPQQQIYMFQVDPGFLMWHDWHTTKFTIRFGSHGTCKVNSGAHWTIKDRYRGGEKAYKMQSYKGLSAVIVRPNQFMTHFYIFKYNGESMLCPWVPQISNMYDPYAFFQHWGMACSYYANDNKRAEFGKFVFVWKPHNNDMTEGETRGPSRYTWFERNFHDGKHWNIPRLRHKFNRNGYFPWCGHGYPIFRRAVIPMCCDEDNLHLPGHKHMPGHGWEMWVRPRTHEYEEQDNMFHWTLAQVIHVNFITYQDIQWNHQGWENTGRFDHTYWLYMFWQEQNEQGRLGQGYGSTQYLRRKVTKDVPAASHKMFKTHVYPNYIQQQECHLTYQRPGLGARRNPKHCWFRLAVGQNCFDPPEPATPVDGHSIPEPLIYWHSNYVKCCQQHARYFKNHGVSGHLASPAQNLGAKTTRPGESDFKMCCRHTLHQNDHEVHKVPDGYFSIMHAGATWSANCYQLIHDYYTQDRRNMILSTDTRERLYTYDHGMDRMMDTLMWFWKSHHKQVSDFGELEWRPNETCRFFQNLHYASGIQISCKCSQNVFKIELGHAVLAEDPRIEWQRMALEFAFHTKNLMPWTDCDYDGILGHFCWFMNFNKFYFYIDEYGAPSIGEWFETWYFCQHDKERKMITIVQNSYWPHSRIRVSCPLINHITMDTCCSTYFEKPASQSGWQQPNPHDPSLKDYWTPVRRACWQVAGVHLAMMFHNLSILMNPHTISPQQINMSEYFSWFVAFLRFPDHQFFGCGKHHWSWECALPDFTPNKKDRGNVDAEGLCETFATSRLDMKRKMHWRCDWTCGRQNISRIELCDATNKNLACFQDPLFAFAVSRTNWEPVWCYPMIPSEFARPLNWCDPNMYCCLVQTQKMPTEGTEAPYYICWFWSLRKLYDGDNFGHLKQTTVGLFYQPAETYRNTSWVWSWEVNLERQQAGCKNQEASKHKNEDQTQNGRLSMWMIVHTYCYEQSDYVKTLDDDAYDDTEMAQGTAKTEQFHSYCHFNRVCTDSCISWTAHHRNAYTVHAPHANTQFMNEKWCAKLQCPSMFQNHWIIFWEGELYAKFIMQCEGYPSWNQYKMVIAEHPKAGMHHKKTEKCYEDSEDSSLRLTAMAIAERAWCPCFCLLIKYQPNKMYESEGALADRAYNINYHLPFMICSMNEEERLEPATKFDAVYKWMHMIIPCNAMMDAKEKMAHENEWLLYREHTDVIDKDSICHDSLVYSWILGNTGIGFTKCCLYIHYYYDMRNNQNTIYSYMYNGKGYNFYGLWHHEVDKEDSYAINMWDMQKRKIRPCPHCDKLMKSHCKYLTRWWCHTLYSTLWLPRSCGHKSLFKYRTYCQNPASRSYQFWIHHVQGCQTTPGKHEVHVGMDYPDEPNFK"
Y = "GCKPPCGNNLQETPCTYDLVYHQSWKGAEGKPCLEMNNETHQHKAQCTKEEWFARSSILYENGYDMPLDGNGSKCHADLWNGCLLRWTQFFMDQSQIGETIYGIVFNKDNRHCQEAPHDKCKSTVVISGQWHCTSIPYRWMVPSFNGYMYRIHLRNCMKIYECHHSDWDQPRSQPGRGFTEDVTWDDWCIAVDLKPCDTWLYGQVAKMNMANKMRFREQLRGTHPWQQTPYSNYDIYMECIPSIESTQYNLEVFTPQGFTIPDMCDEFQSGVWGGKTNFHPLKFQTILGHGVVFYPNYDVPCEDEIQKMDLTIDGKPRYPQHDGFHFQTMGGTDAGMYWPNIMFGIFQLHIFSLHQCSVENSIFEAYHFEIFTFTFVRGQLVVENQASANTGDYCVFHRYYVSRCFWLMQFPGEWAMHHTQNGSQSAIGHEGSPRMWVYLPWVWEVAMNMGVMLYIGHHTGQQIKTHMAPKCEKSATRKNKYHSNECPPPRKHFYSRDLAHMVWKFAPHAGSWNQHTNAGTVVPYILMDEPGPVDCCTGDQKRYVDECVAMCAAYWWCAKCWGPFIEKDWGRSEGMSALGWEARAHAKLNYSLTASPYPMLLDLHNMIGQQWNYETYLVRGSRSFWSTFAGEWQMWAVSIDCWIAPTADPHVECNTKLCCMGTVGGPCKKPNDPLIDRKHWMFGYNVHKTHAWTDSIKKSWVPADQHSCGVSVVHNCSVWAQSPGGMHEGSFCQNHQMQNYKLHSFRDQTWDAPFKKIAQKYTARKCIYPSPWFHRMHICSVNPMNIHGYDWFKAHPGKNELMQQRMYYTVGKENFDRDYHAGYDDVAVICRGVLGNILVVAFTMYYSWNREDMDWAAKHMSQSEVKWKLKPNNVWCKERLDVIFDWIHNIQYQYYQPMFSDQQTQWYMINMPVTGYPWQMAGSFKVFFQMEWGHCICSGRFLVIFKEDGMAIQHWMQVTKDVLYTGMWPFYVRPAHQHSKSFDRSLASLIDVHQQKGCFKMANGDKCTSVSHSVVMYLNCIIHAEQSFKNIPLSCFFRMWVHHYMGCMVEEMWPMSYWIFISPLTSPCYDVADRIDKQGWWYKTSYEFSRCLAMKHWVYHMRKHPDPMGHAVDLHYWALFALEDPLHVHYKSGDQLTWGQQQPAASVAWTSYKNGSMLMIPAHYQCPNFYGTDDAGWMMEKATTTADQNDHCMNQSQAKMVTSRGPPVRDILYMASEKHARKFATYYGAGVIFWNECDTGIWHTKMCVKCCNNRMDGEYANSAHPKTLCTMSPSHIMLIEGTNRGNTAFQKGTDFKTDGHDVRLPCISLDIMQYCFHGGGNPICLDVLMGLVAKIDADVRMNGHQEWVNDHPRRGTNKCLMREFFHNMFNISFPHDQNEIWGEMTLGWFVCHDIRPTKGFSMMARNARMTFIQHLGSFNFHMEGCMYMGESHNEIPTGICMLSRTLARGKDGYHMTYSHKAQWLDTLNVLCMRHERIWVAYYEPDLAEVMMEQCKLDYHLHRQEWKASMPFYEDPERYICDSECIADFGKGEDKVCQKKHCMCWWHKCAAGSTTIEQWHYPAMMARDPQAMRITHDVCASKPKKGRCRSKVWICRAKPIIWAFWEAQHKDYASYDCRDMPYARDCCMYYSSQFCIFHMNAASDSHIPYVDPCSAFCCENKLRTNKVRMQCDRCQDTFTCVGTFEKAIRSMCWCWMDFSCKRYHRQRWLPGGGAILINLKKEWPKWSCQFTWMENFWVTFFDTPVKWKMAQAMDHTSFYPRYYHLRYVGVGGHHQIMTSITLDVYLFQCPLEIFDSLFSLDVHPSDDPTTYQKFSSLDWDWFGHERGPLNCEQLSMAHNDLNNVFWNHPVYRLTPVKMKRYFREMHIQHLCIASDNYTCQAHWEHNYVCQISCFYGFHGKTFWDSRKMRGIENIYHLNGMTGIMSTWHEFITKSEPWHCSAAPQNQSDRCGWQPHGWFVGRIGVCKLFFVYAYRWYLYYVLWYMVGMRLTGWKKYKRPCYFAGQDNSYYYCYSMMIVKTEHGLSQQMILQGYILNVKSAPYGWADIWHRYMYAWCMRRVMVNNHMKCRVMYHVHGNIPIAPNRHSSMNGTREWMYRQITCQHNRTLTKHVHPLVGAAMCMSEWNWRRQQNVINSMTPESDGLTCSFSYDSPLDYRPGCPSRNGTPPVVTLDQMDKEYCLYPKTENQEGTVISFFGNGYWTVMYDQGLTMDMRAQIVTDNNRVCPCQVPMVITNFLTFPTVPMSNMRLEPYRMIMYPKYKGSLRNRDHMLVWHTDKLCYRQIFAYDLQRLRRESNPGPGYSSSPRSNYSCQTIQSCYESEWVQDQNSFCQQYCSEMKMKMSYIHIGTAIHYYAAWQTPVSSHCKYLSEIIRLHEWAWETTSCKGFLLWETGLFCHYQYHWKRMRQEVRTGTLVVFYVFMQRTAMLAVWTYSTVPWWGRFDVESKIPERCRVEASKGDYMHREYLYNRKHYFFDWKQAMMNKAIQADFYVPMTQKIDKAKEKVITEDVWYFLVPDCMPDLDHDSGVWPQQPCHPKKNGAHTWHTTCLEPHQYAISTMHEQFFRHGCLKKHQKCLHVCKPNDHGHQCYNSHDDSYCIFHVDESFYKTYKSGPNHPCCMFWCAPFSVRMWHDVTRFDAQFCHQTIICCTHNFYFRGNEDVKAREVHMHWNVSDDKCTMLRSAINFVEPGTVLPHHCCWFYEVPDPQDMGWWLMGWSVDWATIADMFSAPIHDPNKELPGWRGYEDDMYNGAVPIGNLFPDHYHNSQWQCWGHYLHYLILMIHRALKLKLITCWIQTYKKADCRELKFPCARVETNDTRGMSRMSTRKPTELRLCRMSELLYIRCCARPKFQLAQLYNDAIWYSWHTSPASTGAGNLQNCIVLCVLKIYCAMGLFVHYMPATSICFDNFPLRDVNDSGNLYATTFVYASNAIYTPRYIMIWLASTWYSHVHDAFGCPAFNDLKSGGGIHHEDARFETQIRQWWQMWTFWFDCRDNINMWGWATHGQPQLAIYMFQVKFTMVTNRFGHCNFHMTCTFMDIFPVNSDFTFDRYRGEKTYKMQSYKGLSAIVRNVVNIEVVNISMQLYSMLVPWVERRQHMPIYNMYDPYAFFQRWGMACSYRAEGGKFCVVQDTRFWKPHNNDYTEGETRGPSRYFWFECLGNFHYASKDQVPIRLRHKFNRGGYFPWMGHTYPIFRRSNMWTFELPGPTPLGKAMPGHGWEMWVRRTYEYEEQDNDSHEEQFHWTLADFMIMTKQWNQLVWCTQRYEWQLGQGYGSTQYLQHWMIRRKVTKDVRAASHKMYKEHVYPPFMYIQQECHLTYQRPGLGARRNPKHCWFRLAVGQNCFDPPEENYKVTGGFRNGHSIPEWHSCAWHREAYCYVAMTIVDSYLQHARIIKNHGVSGHLISPAQNLTYFVYARPFESEFKMCCRHTLKVPDGYFNIMHASANCYQLIHDYYTQDQRNMILSTDTRTLLYTYDHGMDRMMGLIANSARDHHLEWRPNETCRFFQNLRGFPDRERPVASGKVYQNVFKIENGHAVLAEDPRIEWQRMALEFAFHTKQLHNAQIQNRMPWTDCDYRGALPVCTTIPRYFCMNMNIAVIFNNKFSFEAQYGWFETRKMSYDVQNSYWPHSVIRMVSCPRINHITMDQCWQVIKPASQSGKPPDQQPNPAIDPCYQTGVCNKVRRACWQGVHLSMFHNLSILMNPHTISPQTINMSSMEFYYFSFCAFLRFPDHLFFGWECASIGRQLSLNRMAMDNVDAEGSKQESRKMHWKCDWTCGQQNISRIKLCDRGGNTNKFLAFAVWEPVVCYPAIPSEFARPHGYLRVMFLEHSHQNPCQGQKMPTEGTEAPYYICLAFKLYDGDNEKQTTIRMDGLFYQYAETYRRTKWVYIICDSIQQAGCKWNNNQEASKRKNEGEFSMWMVSHTYCYEQDDDGWDDTEMAQGDDTPTAFTEHVGVAFHSYTHFNRVCTDSCISWTVMHNWFNAYTVHAPHANTQFHSLQCPQGNYILRMMFQNHWIIFWEGELICYYMQCDNQYKMTIAEHRKAEMHKNVKKTEACYEDSEDRLTAMAIAERAWCPCGCLLIESEGANYDRAYKHMPAWITYWWLLYECFMICSMNEEEREEPATKFDAVYKWMHVIIPCNAMMLINIHQAKEKMAHENEWYLVIECRSKEYIKLKCPDVIDKDWIICHDSLVNKYSAFVSWILVNTGIGFEKCRLYIHYYYDMRNNQTTIYSYMYNGKNYNLQFDMHDFYGLWREMIYFEVDQKRKIRPQPHCDKLMKSHCKYLTRWWCHTLYSTFYPKSLMKIRTYCQNPASRSNQFWIHHVQGCTTTPGHDHEVHVGPDYNSVKVDGFEPNFK"
print(printLcs(X, Y))

a = mt.Matrix("BLOSUM62.txt").lookup_score("N","N")
print(a)